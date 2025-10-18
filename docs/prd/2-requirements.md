# 2. Requirements

## 2.1 Functional Requirements

**FR1**: The bot MUST accept audio file attachments in formats .mp3, .wav, .m4a, and .ogg via Discord messages

**FR2**: Upon receiving an audio file, the bot MUST send an immediate confirmation message to the same channel indicating the file is being processed

**FR3**: The bot MUST upload received audio files to AssemblyAI for transcription processing

**FR4**: The bot MUST support transcription of audio files up to 2 hours in duration

**FR5**: Users MUST be able to specify a custom prompt/instruction alongside the audio file to guide LLM analysis

**FR6**: The bot MUST process the transcription text using Google Gemini LLM with the user-provided prompt

**FR7**: Upon completion, the bot MUST post two separate messages to the same Discord channel:
- Message 1: Complete transcription text
- Message 2: LLM-processed analysis result based on user prompt

**FR8**: The bot MUST process multiple audio files concurrently from different users without blocking or conflicts

**FR9**: The bot MUST handle processing failures gracefully and notify users of errors (transcription failed, LLM processing failed, etc.)

**FR10**: The bot MUST implement a mock/fake storage layer for transcriptions to prepare for future database integration

**FR11**: The bot MUST clean up local audio files after successful processing to manage disk space

**FR12**: The bot MUST maintain the existing `!ping` test command functionality

## 2.2 Non-Functional Requirements

**NFR1**: **Performance** - The bot MUST begin processing audio files within 5 seconds of receiving the Discord attachment

**NFR2**: **Scalability** - The system MUST support at least 5 concurrent audio processing jobs without degradation

**NFR3**: **Reliability** - The bot MUST maintain 99% uptime for Discord message handling (existing functionality must not be degraded)

**NFR4**: **Response Time** - User confirmation messages MUST be sent within 2 seconds of audio file reception

**NFR5**: **API Usage** - The system MUST use free-tier APIs (AssemblyAI free tier, Gemini free tier with large context window) to minimize costs during Phase 2

**NFR6**: **Error Handling** - All external API calls (AssemblyAI, Gemini) MUST include retry logic with exponential backoff

**NFR7**: **Logging** - The system MUST log all processing steps (file received, transcription started, transcription completed, LLM processing completed) for debugging

**NFR8**: **Code Quality** - New code MUST follow Python PEP 8 style guidelines and include type hints

**NFR9**: **Security** - API keys for AssemblyAI and Gemini MUST be stored in environment variables, never hardcoded

**NFR10**: **Maintainability** - Processing logic MUST be modular and testable, with clear separation between transcription and LLM processing

## 2.3 Compatibility Requirements

**CR1**: **Existing Bot Functionality** - All existing Discord message handling and file reception logic MUST continue to work without modification or regression

**CR2**: **Discord.py Integration** - New async processing MUST integrate seamlessly with discord.py's async event loop without blocking message handling

**CR3**: **File Format Support** - MUST maintain support for existing audio formats (.mp3, .wav, .m4a, .ogg) without introducing breaking changes

**CR4**: **Environment Configuration** - MUST continue to use existing configuration patterns (environment variables, python-dotenv) for all secrets

**CR5**: **Deployment Compatibility** - Enhancement MUST be deployable to the same server environment as Phase 1 without additional infrastructure requirements (beyond API access)

**CR6**: **Message Interface** - MUST maintain existing Discord message-based interface pattern; users should interact with the bot the same way

---
