# Tech Stack Alignment

## Existing Technology Stack

| Category | Current Technology | Version | Usage in Enhancement | Notes |
|----------|-------------------|---------|----------------------|-------|
| Language | Python | 3.x (3.8+) | All new code | Type hints mandatory for Phase 2 |
| Discord API Client | discord.py | 2.6.4 | Event handling integration | Existing async event loop |
| Async HTTP | aiohttp | 3.13.1 | Potentially for API calls | May be replaced by SDK clients |
| Config Management | python-dotenv | 1.1.1 | New API key storage | Add ASSEMBLYAI_API_KEY, GEMINI_API_KEY |
| Logging | Python logging | stdlib | Enhanced logging | Add structured logging with job IDs |

## New Technology Additions

| Technology | Version | Purpose | Rationale | Integration Method |
|-----------|---------|---------|-----------|-------------------|
| AssemblyAI Python SDK | Latest | Audio transcription | Official SDK for AssemblyAI API, handles streaming | Wrapper service class |
| Google Generative AI SDK | Latest (google-generativeai) | LLM processing with Gemini | Official Google SDK for Gemini, 1M token context | Wrapper service class |
| asyncio (stdlib) | 3.8+ | Async task management | Required for non-blocking long-duration processing | Direct usage in bot.py |

---
