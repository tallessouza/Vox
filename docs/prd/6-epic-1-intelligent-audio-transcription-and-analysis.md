# 6. Epic 1: Intelligent Audio Transcription and Analysis

**Epic Goal**: Enable Vox Discord bot to automatically transcribe audio files and provide AI-powered analysis based on user-specified prompts, supporting long-duration recordings with concurrent processing.

**Integration Requirements**:
- Seamless integration with existing Discord message handling
- Non-blocking async processing to maintain bot responsiveness
- Clean integration points for future database persistence
- Respect Discord API rate limits and message size constraints

---

## Story 1.1: AssemblyAI Transcription Integration

**As a** Discord user,
**I want** to upload an audio file and receive an automatic transcription,
**so that** I can read the content without manually transcribing.

### Acceptance Criteria

1. Bot successfully initializes AssemblyAI client with API key from environment variable
2. When user attaches supported audio file (.mp3, .wav, .m4a, .ogg), bot uploads file to AssemblyAI
3. Bot awaits AssemblyAI API synchronously for transcription, its an stream
4. Upon completion, bot posts transcription text to Discord channel with "📝 Transcrição:" prefix
5. Bot handles transcription errors gracefully with clear error messages to user
6. Bot deletes local audio file after successful transcription
7. Transcription process does not block other Discord message handling

### Integration Verification

**IV1**: Existing functionality verification - `!ping` command continues to respond with "🏓 Pong!" during transcription processing

**IV2**: Integration point verification - Multiple users can send audio files simultaneously without message handling delays or conflicts

**IV3**: Performance impact verification - Bot responds to new messages within 2 seconds even while processing transcription in background

---

## Story 1.2: Gemini LLM Processing Integration

**As a** Discord user,
**I want** to specify a custom prompt with my audio file,
**so that** I can get tailored analysis (summary, action items, etc.) of the transcribed content.

### Acceptance Criteria

1. Bot extracts user's message text (custom prompt) accompanying the audio file attachment
2. If no prompt is provided, bot uses default prompt: "Analise o seguinte conteúdo"
3. Bot successfully initializes Gemini client with API key from environment variable
4. Bot sends transcription text + user prompt to Gemini API for processing
5. Bot receives and formats Gemini's response
6. Bot posts LLM result to Discord channel with "🤖 Análise:" prefix as separate message after transcription
7. Bot handles LLM processing errors gracefully (API failures, token limits) with clear user notifications
8. Bot respects Gemini free tier context window (1M tokens)

### Integration Verification

**IV1**: Existing functionality verification - Audio file handling from Story 1.1 continues to work; transcription is posted before LLM analysis

**IV2**: Integration point verification - LLM processing failure does not prevent transcription from being posted to channel

**IV3**: Performance impact verification - Large transcriptions (1-2 hour audio) are successfully processed by Gemini without timeouts

---

## Story 1.3: Async Processing Pipeline and Concurrency

**As a** system administrator,
**I want** the bot to handle multiple audio files concurrently without blocking,
**so that** multiple users can use the bot simultaneously without delays.

### Acceptance Criteria

1. Bot implements async task creation using `asyncio.create_task()` for background processing
2. Bot sends immediate confirmation message to user before starting async processing
3. Bot implements semaphore-based concurrency limiting (max 5 concurrent jobs)
4. If concurrency limit reached, bot queues additional jobs and notifies user of queue position
5. Each async task handles its own error cases without affecting other concurrent tasks
6. Bot maintains clean task lifecycle (no orphaned tasks or memory leaks)
7. Bot logs start and completion of each processing task with unique job ID

### Integration Verification

**IV1**: Existing functionality verification - Discord message event handling remains non-blocking; bot responds to all messages promptly

**IV2**: Integration point verification - 5 concurrent audio processing jobs complete successfully without resource exhaustion or crashes

**IV3**: Performance impact verification - Bot memory usage remains stable during concurrent processing; CPU usage returns to baseline after job completion

---

## Story 1.4: Mock Database Layer and Cleanup

**As a** developer,
**I want** a mock database layer for transcription storage,
**so that** we can easily integrate a real database in the future without refactoring core logic.

### Acceptance Criteria

1. Implement `TranscriptionRepository` interface with methods: `save()`, `get_by_id()`, `get_by_user()`
2. Implement `InMemoryTranscriptionRepository` as mock with in-memory dictionary storage
3. Repository stores: user_id, filename, transcription_text, llm_result, timestamp, job_id
4. Bot saves transcription and LLM results to mock repository after successful processing
5. Repository implementation is easily swappable (dependency injection pattern)
6. Bot implements cleanup logic: delete local audio file after successful transcription
7. Bot handles cleanup errors gracefully (file already deleted, permission issues)

### Integration Verification

**IV1**: Existing functionality verification - All transcription and LLM processing workflows continue to work with repository layer added

**IV2**: Integration point verification - Mock repository can be swapped with a different implementation (tested with a second mock) without code changes to bot logic

**IV3**: Performance impact verification - Disk space for `audios/` directory returns to baseline after processing; no audio files remain after successful jobs

---

## Story 1.5: Error Handling, Logging, and Documentation

**As a** developer and user,
**I want** comprehensive error handling and documentation,
**so that** I can debug issues easily and users understand how to use the bot.

### Acceptance Criteria

1. All external API calls (AssemblyAI, Gemini) include try-except blocks with specific error messages
2. Bot implements retry logic with exponential backoff for transient API failures (max 3 retries)
3. Bot logs all significant events (file received, transcription started/completed, LLM started/completed, errors) with timestamps and job IDs
4. User-facing error messages are in Portuguese and provide actionable information
5. README.md includes setup instructions, required environment variables, and usage examples
6. Code includes docstrings for all public functions with param and return type documentation
7. Startup validation checks for required environment variables (DISCORD_TOKEN, ASSEMBLYAI_API_KEY, GEMINI_API_KEY)

### Integration Verification

**IV1**: Existing functionality verification - Error handling does not interfere with successful processing paths; happy path remains performant

**IV2**: Integration point verification - Simulated API failures (mock AssemblyAI timeout) trigger retry logic and eventually provide clear user error message

**IV3**: Performance impact verification - Logging overhead is negligible (< 50ms per processing job); log files do not grow unbounded

---
