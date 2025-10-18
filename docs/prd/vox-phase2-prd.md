# Vox Discord Bot - Phase 2 Enhancement PRD

**Product Requirements Document**
**Version**: 1.0
**Date**: 2025-10-18
**Type**: Brownfield Enhancement

---

## 1. Intro Project Analysis and Context

### 1.1 Existing Project Overview

#### Analysis Source
- **Type**: IDE-based fresh analysis
- **Analysis Date**: 2025-10-18
- **Project Access**: Full source code available

#### Current Project State

**Vox** is a Discord bot built with Python that currently provides basic audio file handling capabilities:

- **Primary Purpose**: Receives audio file attachments from Discord users and provides a foundation for audio transcription
- **Current Implementation**:
  - Listens to Discord messages via discord.py 2.6.4
  - Detects audio file attachments (.mp3, .wav, .m4a, .ogg)
  - Saves audio files locally to `audios/` directory
  - Contains placeholder transcription function (not yet implemented)
  - Has commented-out OpenAI Whisper integration code
- **Current Status**: Phase 1 (basic deployment) is assumed to be operational

**Key Files**:
- `bot.py`: Main Discord bot logic with message handling
- `transcription.py`: Placeholder transcription module
- `requirements.txt`: Python dependencies (discord.py, aiohttp, python-dotenv)

### 1.2 Available Documentation Analysis

**Available Documentation**: ✗ Minimal

- ✗ Tech Stack Documentation
- ✗ Source Tree/Architecture
- ✗ Coding Standards
- ✗ API Documentation
- ✗ External API Documentation
- ✗ UX/UI Guidelines
- ✗ Technical Debt Documentation

**Note**: This PRD will serve as the primary planning document for Phase 2 enhancement. Architecture documentation will be created separately if needed.

### 1.3 Enhancement Scope Definition

#### Enhancement Type
- ✓ **New Feature Addition** (Primary)
- ✓ **Integration with New Systems** (AssemblyAI + Gemini LLM)
- ✗ Major Feature Modification
- ✗ Performance/Scalability Improvements
- ✗ UI/UX Overhaul
- ✗ Technology Stack Upgrade
- ✗ Bug Fix and Stability Improvements

#### Enhancement Description

Phase 2 adds intelligent audio transcription and LLM-powered analysis capabilities to the existing Vox Discord bot. Users will be able to upload audio files (including long-duration recordings of 1-2 hours), receive automatic transcriptions via AssemblyAI, and get customized LLM analysis using user-specified prompts processed by Google Gemini.

The enhancement transforms Vox from a simple audio receiver into a comprehensive audio intelligence platform for Discord communities.

#### Impact Assessment
- ✗ Minimal Impact (isolated additions)
- ✓ **Moderate Impact** (some existing code changes)
- ✗ Significant Impact (substantial existing code changes)
- ✗ Major Impact (architectural changes required)

**Impact Details**:
- Existing Discord message handling will be extended (not replaced)
- New async processing pipeline will be added
- File handling logic will be enhanced for long-duration files
- Mock database layer will be introduced for future persistence

### 1.4 Goals and Background Context

#### Goals

- Enable automatic transcription of audio files using AssemblyAI API
- Allow users to specify custom LLM prompts for analyzing transcribed content
- Support processing of long-duration audio files (1-2 hours) asynchronously
- Provide clear, formatted output with both transcription and LLM analysis
- Handle concurrent audio processing from multiple users
- Prepare infrastructure for future database persistence (via mock layer)
- Maintain reliability and user experience of existing Discord bot functionality

#### Background Context

The current Vox bot successfully handles basic audio file reception but lacks the core intelligence features that make it valuable for Discord communities. Users frequently need to:

1. **Transcribe meeting recordings**: Discord voice channel recordings, team meetings, or interviews shared as audio files
2. **Extract insights**: Get summaries, action items, key decisions, or specific information from lengthy audio content
3. **Flexible analysis**: Apply different analytical lenses (summarization, sentiment analysis, topic extraction) depending on the audio content type

Phase 2 addresses these needs by integrating professional-grade transcription (AssemblyAI) with powerful LLM reasoning (Google Gemini), while maintaining the simple Discord-based interface that users already understand.

**Why This Enhancement Matters**:
- Converts passive audio storage into active audio intelligence
- Reduces manual transcription time for community members
- Enables knowledge extraction from voice-based collaboration
- Positions Vox as a productivity tool rather than just a utility

#### Change Log

| Change | Date | Version | Description | Author |
|--------|------|---------|-------------|--------|
| Initial PRD | 2025-10-18 | 1.0 | Created Phase 2 enhancement PRD based on user requirements | PM Agent |

---

## 2. Requirements

### 2.1 Functional Requirements

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

### 2.2 Non-Functional Requirements

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

### 2.3 Compatibility Requirements

**CR1**: **Existing Bot Functionality** - All existing Discord message handling and file reception logic MUST continue to work without modification or regression

**CR2**: **Discord.py Integration** - New async processing MUST integrate seamlessly with discord.py's async event loop without blocking message handling

**CR3**: **File Format Support** - MUST maintain support for existing audio formats (.mp3, .wav, .m4a, .ogg) without introducing breaking changes

**CR4**: **Environment Configuration** - MUST continue to use existing configuration patterns (environment variables, python-dotenv) for all secrets

**CR5**: **Deployment Compatibility** - Enhancement MUST be deployable to the same server environment as Phase 1 without additional infrastructure requirements (beyond API access)

**CR6**: **Message Interface** - MUST maintain existing Discord message-based interface pattern; users should interact with the bot the same way

---

## 3. User Interface Enhancement Goals

### 3.1 Integration with Existing UI

**Discord Message Interface**: The enhancement maintains the existing Discord message-based interface pattern:

- Users continue to interact by sending messages to channels where the bot is present
- Audio files are attached using Discord's standard attachment mechanism
- Custom prompts are provided in the message text accompanying the audio attachment
- All bot responses use Discord's standard message format

**New Interaction Pattern**:
```
User: [Attaches audio.mp3]
      "Summarize this meeting and extract action items"

Bot:  "🎙️ Recebi o arquivo `audio.mp3`, processando..."

[Processing occurs asynchronously...]

Bot:  "📝 Transcrição:
      [Full transcription text]"

Bot:  "🤖 Análise:
      [LLM-processed result based on user's prompt]"
```

### 3.2 Modified/New User Interactions

**Enhanced Audio Message Handler**:
- Existing: Bot confirms audio receipt and attempts placeholder transcription
- New: Bot confirms receipt, extracts user prompt, initiates async processing pipeline

**New Response Format**:
- Two-message output pattern (transcription + analysis)
- Clear emoji indicators (🎙️ for processing, 📝 for transcription, 🤖 for LLM analysis)
- Error messages with actionable information (⚠️ for failures)

**Status Updates**:
- Immediate confirmation on file receipt
- Final results posted when complete (no intermediate progress updates for Phase 2)

### 3.3 UI Consistency Requirements

**UCR1**: All bot messages MUST use the existing emoji-based visual language (🎙️, 📝, ⚠️, 🤖)

**UCR2**: Message formatting MUST use Discord markdown (code blocks, bold, etc.) consistently

**UCR3**: Error messages MUST follow existing pattern: `⚠️ Ocorreu um erro: [specific error]`

**UCR4**: Portuguese language MUST be maintained in all bot responses for consistency with existing implementation

---

## 4. Technical Constraints and Integration Requirements

### 4.1 Existing Technology Stack

**Languages**: Python 3.x (version 3.8+)

**Frameworks**:
- discord.py 2.6.4 (Discord API client)
- aiohttp 3.13.1 (Async HTTP client)

**Database**: None (Phase 2 will introduce mock layer)

**Infrastructure**:
- Server deployment (assumed operational from Phase 1)
- Local file system for temporary audio storage (`audios/` directory)

**External Dependencies**:
- Discord API (via discord.py)
- python-dotenv for environment variable management

**New Dependencies for Phase 2**:
- AssemblyAI Python SDK (for transcription)
- Google Generative AI SDK (for Gemini LLM access)

### 4.2 Integration Approach

**Database Integration Strategy**:
- Implement mock/fake repository pattern in Phase 2
- Create `TranscriptionRepository` interface with in-memory mock implementation
- Design for easy swap to real database (PostgreSQL/MongoDB) in future phase
- Store: `{user_id, filename, transcription, llm_result, timestamp}`

**API Integration Strategy**:
- **AssemblyAI**:
  - Use official Python SDK
  - Handle large files via AssemblyAI's upload API
- **Gemini LLM**:
  - Use google-generativeai SDK
  - Leverage free tier with large context window (1M tokens)
  - Pass full transcription + user prompt as context

**Frontend Integration Strategy**:
- N/A (Discord interface only)
- Maintain existing message event handling
- Extend `on_message` handler with new processing pipeline

**Testing Integration Strategy**:
- Unit tests for transcription module
- Unit tests for LLM processing module
- Mock external APIs in tests
- Integration test with real Discord message simulation

### 4.3 Code Organization and Standards

**File Structure Approach**:
```
vox/
├── bot.py                    # Main Discord bot (existing)
├── transcription.py          # Transcription logic (to be implemented)
├── llm_processing.py         # NEW: LLM processing module
├── services/                 # NEW: Service layer
│   ├── assemblyai_service.py
│   └── gemini_service.py
├── repositories/             # NEW: Data layer (mock)
│   └── transcription_repo.py
├── utils/                    # NEW: Utilities
│   └── async_helpers.py
├── tests/                    # NEW: Test suite
│   ├── test_transcription.py
│   ├── test_llm_processing.py
│   └── test_integration.py
├── requirements.txt          # Updated dependencies
└── .env                      # Environment variables (not committed)
```

**Naming Conventions**:
- Python PEP 8 style: `snake_case` for functions/variables, `PascalCase` for classes
- Service classes: `*Service` suffix (e.g., `AssemblyAIService`)
- Repository classes: `*Repository` suffix
- Async functions: prefix with `async def`

**Coding Standards**:
- Type hints for all function signatures
- Docstrings for all public functions (Google style)
- Maximum line length: 100 characters
- Use `black` formatter for consistency
- Use `pylint` for linting (score > 8.0)

**Documentation Standards**:
- README.md with setup instructions and API key configuration
- Inline comments for complex logic
- Function docstrings with param descriptions and return types

### 4.4 Deployment and Operations

**Build Process Integration**:
- No build step required (interpreted Python)
- `pip install -r requirements.txt` for dependency installation
- Environment variable validation on startup

**Deployment Strategy**:
- Single-server deployment (same as Phase 1)
- No additional infrastructure required
- Requires network access to AssemblyAI and Gemini APIs
- Environment variables: `DISCORD_TOKEN`, `ASSEMBLYAI_API_KEY`, `GEMINI_API_KEY`

**Monitoring and Logging**:
- Python `logging` module with INFO level for production
- Log rotation to prevent disk space issues
- Key events to log:
  - Audio file received
  - Transcription job submitted
  - Transcription completed
  - LLM processing completed
  - Errors and retries

**Configuration Management**:
- Continue using `.env` file pattern with python-dotenv
- New required environment variables:
  - `ASSEMBLYAI_API_KEY`
  - `GEMINI_API_KEY`
  - `GEMINI_MODEL` (default: "gemini-1.5-flash")
- Optional configuration:
  - `MAX_CONCURRENT_JOBS` (default: 5)
  - `AUDIO_STORAGE_PATH` (default: "audios/")

### 4.5 Risk Assessment and Mitigation

**Technical Risks**:
- **Risk**: AssemblyAI free tier rate limits exceeded
  - **Mitigation**: Implement request queuing, monitor usage, add user feedback for rate limiting
- **Risk**: Gemini API latency for large transcriptions
  - **Mitigation**: Use async processing, set reasonable timeouts (5 minutes), inform user of delays
- **Risk**: Large audio files exhaust disk space
  - **Mitigation**: Implement cleanup logic, add disk space monitoring, reject files > 200MB

**Integration Risks**:
- **Risk**: Discord.py async event loop blocking during processing
  - **Mitigation**: Use asyncio.create_task() for background processing, never block in on_message
- **Risk**: Multiple concurrent jobs overload server CPU/memory
  - **Mitigation**: Implement semaphore-based concurrency limiting (max 5 concurrent)

**Deployment Risks**:
- **Risk**: API key configuration errors on deployment
  - **Mitigation**: Startup validation script, clear error messages, documentation
- **Risk**: Network connectivity issues to external APIs
  - **Mitigation**: Retry logic with exponential backoff, timeout configurations, user-friendly error messages

**Mitigation Strategies**:
1. Comprehensive error handling with user notifications
2. Graceful degradation (if one service fails, inform user clearly)
3. Logging for post-mortem debugging
4. Configuration validation on startup
5. Resource cleanup (files, API connections) in all code paths

---

## 5. Epic and Story Structure

### 5.1 Epic Approach

**Epic Structure Decision**: Single comprehensive epic with sequential stories

**Rationale**:
This enhancement, while adding substantial new functionality, is focused on a single cohesive feature: audio transcription and LLM analysis. All components (AssemblyAI integration, Gemini integration, async processing) work together to deliver one user-facing capability. Breaking this into multiple epics would create artificial boundaries and dependencies.

A single epic with well-sequenced stories allows for:
- Incremental development and testing
- Clear dependency management between integration components
- Easier rollback if issues arise
- Focused scope for Phase 2 delivery

---

## 6. Epic 1: Intelligent Audio Transcription and Analysis

**Epic Goal**: Enable Vox Discord bot to automatically transcribe audio files and provide AI-powered analysis based on user-specified prompts, supporting long-duration recordings with concurrent processing.

**Integration Requirements**:
- Seamless integration with existing Discord message handling
- Non-blocking async processing to maintain bot responsiveness
- Clean integration points for future database persistence
- Respect Discord API rate limits and message size constraints

---

### Story 1.1: AssemblyAI Transcription Integration

**As a** Discord user,
**I want** to upload an audio file and receive an automatic transcription,
**so that** I can read the content without manually transcribing.

#### Acceptance Criteria

1. Bot successfully initializes AssemblyAI client with API key from environment variable
2. When user attaches supported audio file (.mp3, .wav, .m4a, .ogg), bot uploads file to AssemblyAI
3. Bot awaits AssemblyAI API synchronously for transcription, its an stream
4. Upon completion, bot posts transcription text to Discord channel with "📝 Transcrição:" prefix
5. Bot handles transcription errors gracefully with clear error messages to user
6. Bot deletes local audio file after successful transcription
7. Transcription process does not block other Discord message handling

#### Integration Verification

**IV1**: Existing functionality verification - `!ping` command continues to respond with "🏓 Pong!" during transcription processing

**IV2**: Integration point verification - Multiple users can send audio files simultaneously without message handling delays or conflicts

**IV3**: Performance impact verification - Bot responds to new messages within 2 seconds even while processing transcription in background

---

### Story 1.2: Gemini LLM Processing Integration

**As a** Discord user,
**I want** to specify a custom prompt with my audio file,
**so that** I can get tailored analysis (summary, action items, etc.) of the transcribed content.

#### Acceptance Criteria

1. Bot extracts user's message text (custom prompt) accompanying the audio file attachment
2. If no prompt is provided, bot uses default prompt: "Analise o seguinte conteúdo"
3. Bot successfully initializes Gemini client with API key from environment variable
4. Bot sends transcription text + user prompt to Gemini API for processing
5. Bot receives and formats Gemini's response
6. Bot posts LLM result to Discord channel with "🤖 Análise:" prefix as separate message after transcription
7. Bot handles LLM processing errors gracefully (API failures, token limits) with clear user notifications
8. Bot respects Gemini free tier context window (1M tokens)

#### Integration Verification

**IV1**: Existing functionality verification - Audio file handling from Story 1.1 continues to work; transcription is posted before LLM analysis

**IV2**: Integration point verification - LLM processing failure does not prevent transcription from being posted to channel

**IV3**: Performance impact verification - Large transcriptions (1-2 hour audio) are successfully processed by Gemini without timeouts

---

### Story 1.3: Async Processing Pipeline and Concurrency

**As a** system administrator,
**I want** the bot to handle multiple audio files concurrently without blocking,
**so that** multiple users can use the bot simultaneously without delays.

#### Acceptance Criteria

1. Bot implements async task creation using `asyncio.create_task()` for background processing
2. Bot sends immediate confirmation message to user before starting async processing
3. Bot implements semaphore-based concurrency limiting (max 5 concurrent jobs)
4. If concurrency limit reached, bot queues additional jobs and notifies user of queue position
5. Each async task handles its own error cases without affecting other concurrent tasks
6. Bot maintains clean task lifecycle (no orphaned tasks or memory leaks)
7. Bot logs start and completion of each processing task with unique job ID

#### Integration Verification

**IV1**: Existing functionality verification - Discord message event handling remains non-blocking; bot responds to all messages promptly

**IV2**: Integration point verification - 5 concurrent audio processing jobs complete successfully without resource exhaustion or crashes

**IV3**: Performance impact verification - Bot memory usage remains stable during concurrent processing; CPU usage returns to baseline after job completion

---

### Story 1.4: Mock Database Layer and Cleanup

**As a** developer,
**I want** a mock database layer for transcription storage,
**so that** we can easily integrate a real database in the future without refactoring core logic.

#### Acceptance Criteria

1. Implement `TranscriptionRepository` interface with methods: `save()`, `get_by_id()`, `get_by_user()`
2. Implement `InMemoryTranscriptionRepository` as mock with in-memory dictionary storage
3. Repository stores: user_id, filename, transcription_text, llm_result, timestamp, job_id
4. Bot saves transcription and LLM results to mock repository after successful processing
5. Repository implementation is easily swappable (dependency injection pattern)
6. Bot implements cleanup logic: delete local audio file after successful transcription
7. Bot handles cleanup errors gracefully (file already deleted, permission issues)

#### Integration Verification

**IV1**: Existing functionality verification - All transcription and LLM processing workflows continue to work with repository layer added

**IV2**: Integration point verification - Mock repository can be swapped with a different implementation (tested with a second mock) without code changes to bot logic

**IV3**: Performance impact verification - Disk space for `audios/` directory returns to baseline after processing; no audio files remain after successful jobs

---

### Story 1.5: Error Handling, Logging, and Documentation

**As a** developer and user,
**I want** comprehensive error handling and documentation,
**so that** I can debug issues easily and users understand how to use the bot.

#### Acceptance Criteria

1. All external API calls (AssemblyAI, Gemini) include try-except blocks with specific error messages
2. Bot implements retry logic with exponential backoff for transient API failures (max 3 retries)
3. Bot logs all significant events (file received, transcription started/completed, LLM started/completed, errors) with timestamps and job IDs
4. User-facing error messages are in Portuguese and provide actionable information
5. README.md includes setup instructions, required environment variables, and usage examples
6. Code includes docstrings for all public functions with param and return type documentation
7. Startup validation checks for required environment variables (DISCORD_TOKEN, ASSEMBLYAI_API_KEY, GEMINI_API_KEY)

#### Integration Verification

**IV1**: Existing functionality verification - Error handling does not interfere with successful processing paths; happy path remains performant

**IV2**: Integration point verification - Simulated API failures (mock AssemblyAI timeout) trigger retry logic and eventually provide clear user error message

**IV3**: Performance impact verification - Logging overhead is negligible (< 50ms per processing job); log files do not grow unbounded

---

## Appendix: Technical Notes

### User Prompt Extraction Pattern

Discord message format when user attaches audio with prompt:
```
Message.content = "Summarize this meeting and extract action items"
Message.attachments[0] = [audio.mp3 file object]
```

Extraction logic:
```python
if message.attachments:
    user_prompt = message.content.strip() if message.content else "Analise o seguinte conteúdo"
    audio_file = message.attachments[0]
```

### Async Processing Flow

```
1. on_message event triggered
2. Validate audio attachment
3. Send confirmation message (sync)
4. asyncio.create_task(process_audio_task(message, attachment, user_prompt))
5. Return from on_message immediately
6. [Background task]:
   a. Upload to AssemblyAI
   b. Await for transcription completion
   c. Post transcription message
   d. Send to Gemini with prompt
   e. Post LLM analysis message
   f. Save to mock repository
   g. Cleanup local file
```

### API Usage Estimates

**AssemblyAI Free Tier**:
- Limit: Varies by plan
- Usage: 1 API call per audio file upload + polling calls
- 2-hour audio ≈ 1-5 minutes processing time

**Gemini Free Tier**:
- Context window: 1M tokens
- 2-hour transcription ≈ 50k-150k tokens (est.)
- Well within free tier limits

---

**End of PRD**
