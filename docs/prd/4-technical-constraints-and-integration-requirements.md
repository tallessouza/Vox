# 4. Technical Constraints and Integration Requirements

## 4.1 Existing Technology Stack

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

## 4.2 Integration Approach

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

## 4.3 Code Organization and Standards

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

## 4.4 Deployment and Operations

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

## 4.5 Risk Assessment and Mitigation

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
