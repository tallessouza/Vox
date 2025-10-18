# Next Steps

## Story Manager Handoff

**Prompt for Story Manager:**

> Based on the Vox Phase 2 Brownfield Architecture (docs/architecture/vox-phase2-architecture.md) and PRD (docs/prd/vox-phase2-prd.md), create detailed implementation stories following the epic structure defined in the PRD.
>
> **Key Integration Requirements:**
> - All changes must preserve existing `!ping` functionality
> - Async processing pipeline must not block Discord message handling
> - Follow service layer pattern (services/, repositories/)
> - Use dependency injection for repository (enables future database swap)
>
> **Existing System Constraints:**
> - Python 3.8+, discord.py 2.6.4 async event loop
> - No database in Phase 1 (use mock repository)
> - Portuguese language for all user messages
> - Server deployment (no containerization required)
>
> **First Story to Implement:**
> Story 1.1: AssemblyAI Transcription Integration
> - Create `services/assemblyai_service.py` with `transcribe_audio()` method
> - Extend `on_message()` in bot.py to call service asynchronously
> - Add error handling and Portuguese user feedback
> - **Integration Checkpoint:** Verify `!ping` still responds during transcription processing
>
> **Emphasis:** Maintain existing system integrity throughout. Each story must include Integration Verification steps that test existing bot functionality.

## Developer Handoff

**Prompt for Developers:**

> You are implementing Phase 2 enhancements for the Vox Discord Bot. Reference the architecture document (docs/architecture/vox-phase2-architecture.md) for technical decisions and integration patterns.
>
> **Coding Standards (from actual project analysis):**
> - Python PEP 8 style: `snake_case` for functions/variables, `PascalCase` for classes
> - Type hints mandatory for all function signatures
> - Google-style docstrings for all public functions
> - Async/await for all I/O operations (never block discord.py event loop)
> - Logging with job IDs: `logger.info(f"[{job_id}] Message")`
>
> **Integration Requirements (validated with existing codebase):**
> - Extend `on_message()` in bot.py, never modify `on_ready()` or `!ping` handler
> - Use `asyncio.create_task()` for background processing
> - Always use `TranscriptionRepository` interface for data persistence
> - Maintain Portuguese language in all user-facing messages
> - Follow emoji patterns: 🎙️ (processing), 📝 (transcription), 🤖 (LLM), ⚠️ (error)
>
> **Key Technical Decisions:**
> - Service layer pattern: `services/assemblyai_service.py`, `services/gemini_service.py`
> - Repository pattern: `repositories/transcription_repo.py` with interface + mock implementation
> - Async pipeline: `process_audio_task()` orchestrates transcription → LLM → Discord post → cleanup
> - Error handling: Retry with exponential backoff (max 3), graceful degradation (post transcription even if LLM fails)
>
> **Compatibility Requirements (specific verification steps):**
> - After implementing each story, test `!ping` command responds within 2 seconds
> - Verify concurrent audio uploads don't block message handling
> - Check that existing audio file handling (saving to `audios/`) still works
> - Validate startup with missing API keys fails gracefully with clear error message
>
> **Clear Sequencing:**
> 1. Story 1.1: AssemblyAI integration (transcription only)
> 2. Story 1.2: Gemini integration (LLM processing)
> 3. Story 1.3: Async pipeline (concurrency, semaphore limiting)
> 4. Story 1.4: Repository (mock persistence, file cleanup)
> 5. Story 1.5: Error handling, logging, documentation
>
> This sequence minimizes risk: each story builds on the previous, with integration checkpoints ensuring existing functionality never breaks.

---

**End of Architecture Document**
