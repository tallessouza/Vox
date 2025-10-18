# Coding Standards and Conventions

## Existing Standards Compliance

**Code Style:** PEP 8 (Python Enhancement Proposal 8)
**Linting Rules:** None currently enforced (recommend adding `pylint` or `black` for Phase 2)
**Testing Patterns:** No existing tests (Phase 2 introduces pytest)
**Documentation Style:** Minimal inline comments; Phase 2 requires Google-style docstrings

## Enhancement-Specific Standards

- **Type Hints:** Mandatory for all function signatures in new code
  ```python
  async def transcribe_audio(file_path: str) -> str:
      """Transcribe audio file using AssemblyAI."""
  ```
- **Async/Await:** All I/O-bound operations must use `async`/`await` to prevent blocking
- **Error Handling:** Explicit try-except with specific exceptions; never bare `except:`
- **Logging:** Structured logging with job IDs for traceability
  ```python
  logger.info(f"[{job_id}] Transcription started for {filename}")
  ```
- **Docstrings:** Google-style docstrings for all public functions
  ```python
  async def process_audio_task(message: discord.Message, attachment: discord.Attachment, user_prompt: str) -> None:
      """Process audio file with transcription and LLM analysis.

      Args:
          message: Discord message containing the audio attachment
          attachment: Audio file attachment object
          user_prompt: User's custom prompt for LLM analysis

      Returns:
          None (posts results to Discord channel)

      Raises:
          AssemblyAIError: If transcription fails after retries
          GeminiError: If LLM processing fails after retries
      """
  ```

## Critical Integration Rules

- **Existing API Compatibility:** Never modify `on_ready()` or `!ping` handler; only extend `on_message()`
- **Database Integration:** Always use TranscriptionRepository interface, never direct database calls
- **Error Handling:** Graceful degradation - if LLM fails, still post transcription; if transcription fails, post clear error
- **Logging Consistency:** Use existing `logging` module with INFO level; add DEBUG for development

---
