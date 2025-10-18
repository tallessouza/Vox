"""AssemblyAI transcription service.

This module provides integration with AssemblyAI's transcription API,
handling audio file uploads and streaming transcription results with
Portuguese language support and speaker identification.
"""

import os
import logging
from typing import Optional, Dict, List, Any
import assemblyai as aai


logger = logging.getLogger(__name__)


class AssemblyAIError(Exception):
    """Exception raised for AssemblyAI API errors."""
    pass


class AssemblyAIService:
    """Service for transcribing audio files using AssemblyAI API.

    Configured for Portuguese language with speaker labels for better
    transcription quality and conversation understanding.
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize AssemblyAI service with Portuguese configuration.

        Args:
            api_key: AssemblyAI API key. If None, reads from ASSEMBLYAI_API_KEY env var.

        Raises:
            AssemblyAIError: If API key is not provided or found in environment.
        """
        self.api_key = api_key or os.getenv("ASSEMBLYAI_API_KEY")
        if not self.api_key:
            raise AssemblyAIError(
                "AssemblyAI API key not found. Set ASSEMBLYAI_API_KEY environment variable."
            )

        # Configure AssemblyAI client
        aai.settings.api_key = self.api_key

        # Configure transcription for Portuguese with speaker labels
        self.config = aai.TranscriptionConfig(
            language_code="pt",  # Portuguese language
            speech_model=aai.SpeechModel.best,  # Best quality model
            speaker_labels=True  # Enable speaker identification
        )

        self.transcriber = aai.Transcriber()
        logger.info("AssemblyAI service initialized with Portuguese config and speaker labels")

    async def transcribe_audio(self, file_path: str) -> Dict[str, Any]:
        """Transcribe audio file using AssemblyAI with speaker labels.

        This method uploads the audio file and returns complete transcription
        data including speaker-separated utterances.

        Args:
            file_path: Path to local audio file (.mp3, .wav, .m4a, .ogg)

        Returns:
            Dictionary with transcription data:
            {
                "text": str,  # Full transcription text
                "audio_duration": int,  # Duration in milliseconds
                "confidence": float,  # Overall confidence score
                "utterances": List[Dict],  # Speaker-separated segments
                "formatted_text": str  # Text formatted by speaker
            }

        Raises:
            AssemblyAIError: If transcription fails or file cannot be uploaded
        """
        if not os.path.exists(file_path):
            raise AssemblyAIError(f"Audio file not found: {file_path}")

        try:
            logger.info(f"Starting transcription with speaker labels for: {file_path}")

            # Upload and transcribe with Portuguese config (with retry logic)
            max_retries = 3
            retry_count = 0
            last_error = None

            while retry_count < max_retries:
                try:
                    transcript = self.transcriber.transcribe(file_path, config=self.config)
                    break  # Success, exit retry loop
                except Exception as e:
                    retry_count += 1
                    last_error = e
                    if retry_count < max_retries:
                        logger.warning(f"Transcription attempt {retry_count} failed: {e}. Retrying...")
                        import time
                        time.sleep(2 ** retry_count)  # Exponential backoff: 2s, 4s, 8s
                    else:
                        logger.error(f"All {max_retries} transcription attempts failed")
                        raise last_error

            # Check for transcription errors
            if transcript.status == aai.TranscriptStatus.error:
                error_msg = transcript.error if hasattr(transcript, 'error') else "Unknown error"
                logger.error(f"Transcription failed: {error_msg}")
                raise AssemblyAIError(f"Transcription failed: {error_msg}")

            if not transcript.text:
                raise AssemblyAIError("Transcription returned empty text")

            # Extract utterances with speaker information
            utterances = []
            if transcript.utterances:
                for u in transcript.utterances:
                    utterances.append({
                        "text": u.text,
                        "speaker": u.speaker,
                        "start": u.start,
                        "end": u.end
                    })
                logger.info(f"Extracted {len(utterances)} utterances from transcription")

            # Format text by speaker for better readability
            formatted_text = self._format_by_speaker(utterances)

            # Build complete transcription data
            transcription_data = {
                "text": transcript.text,
                "audio_duration": transcript.audio_duration,
                "confidence": transcript.confidence if hasattr(transcript, 'confidence') else None,
                "utterances": utterances,
                "formatted_text": formatted_text
            }

            logger.info(f"Transcription completed successfully for {file_path}")
            return transcription_data

        except aai.types.TranscriptError as e:
            logger.error(f"AssemblyAI transcript error: {e}")
            raise AssemblyAIError(f"Transcription error: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error during transcription: {e}")
            raise AssemblyAIError(f"Unexpected transcription error: {str(e)}")

    def _format_by_speaker(self, utterances: List[Dict[str, Any]]) -> str:
        """Format utterances by speaker for Discord display.

        Args:
            utterances: List of utterance dictionaries with speaker info

        Returns:
            Formatted text with speaker labels
        """
        if not utterances:
            return ""

        formatted_lines = []
        current_speaker = None

        for utterance in utterances:
            speaker = utterance["speaker"]
            text = utterance["text"]

            # Add speaker label when speaker changes
            if speaker != current_speaker:
                formatted_lines.append(f"\n**[{speaker}]**")
                current_speaker = speaker

            formatted_lines.append(text)

        return "\n".join(formatted_lines).strip()
