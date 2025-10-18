# Source Tree Integration

## Existing Project Structure

```
vox/
├── bot.py                    # Main Discord bot (67 lines)
├── transcription.py          # Placeholder transcription (12 lines)
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not committed)
├── .gitignore
├── readme.md
└── audios/                   # Local audio storage (created at runtime)
```

## New File Organization

```
vox/
├── bot.py                         # Main Discord bot (MODIFIED: extended on_message)
├── transcription.py               # REMOVED: replaced by services/
├── requirements.txt               # UPDATED: add assemblyai, google-generativeai
├── .env                           # UPDATED: add ASSEMBLYAI_API_KEY, GEMINI_API_KEY
├── .gitignore                     # UPDATED: ensure audios/ ignored
├── readme.md                      # UPDATED: Phase 2 setup instructions
├── audios/                        # Existing local storage (temporary files)
├── services/                      # NEW: Service layer
│   ├── __init__.py
│   ├── assemblyai_service.py    # AssemblyAI integration
│   └── gemini_service.py         # Gemini LLM integration
├── repositories/                  # NEW: Data layer (mock)
│   ├── __init__.py
│   ├── transcription_repo.py    # Repository interface + InMemoryTranscriptionRepository
│   └── models.py                 # Transcription data model
├── utils/                         # NEW: Utilities
│   ├── __init__.py
│   └── async_helpers.py          # Async pipeline helpers (if needed)
└── tests/                         # NEW: Test suite
    ├── __init__.py
    ├── test_assemblyai_service.py
    ├── test_gemini_service.py
    ├── test_repository.py
    └── test_integration.py        # End-to-end tests with mocked APIs
```

## Integration Guidelines

- **File Naming:** `snake_case` for all Python files (PEP 8)
- **Folder Organization:** Service layer pattern (services/, repositories/, utils/, tests/)
- **Import/Export Patterns:**
  - Services and repositories export public classes via `__init__.py`
  - Bot.py imports from services and repositories
  - Circular imports prevented via dependency injection

---
