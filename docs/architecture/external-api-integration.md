# External API Integration

## AssemblyAI API

- **Purpose:** Professional-grade audio transcription for uploaded files
- **Documentation:** https://www.assemblyai.com/docs
- **Base URL:** https://api.assemblyai.com
- **Authentication:** Bearer token (API key in Authorization header)
- **Integration Method:** Python SDK wrapping REST API

**Key Endpoints Used:**
- `POST /v2/upload` - Upload audio file
- `POST /v2/transcript` - Create transcription job
- `GET /v2/transcript/{id}` - Poll transcription status (or use streaming)

**Error Handling:**
- Retry logic with exponential backoff (max 3 retries) for transient failures
- User-friendly Portuguese error messages on permanent failures
- Timeout: 10 minutes for long audio files

---

## Gemini API

- **Purpose:** LLM-powered analysis of transcriptions with custom user prompts
- **Documentation:** https://ai.google.dev/docs
- **Base URL:** Via google-generativeai SDK
- **Authentication:** API key configuration via SDK
- **Integration Method:** Official Python SDK

**Key Endpoints Used:**
- `generateContent` - Send prompt + transcription, receive analysis

**Error Handling:**
- Retry logic with exponential backoff (max 3 retries)
- Handle token limit errors (1M context window should be sufficient for 2-hour audio)
- Graceful failure: if LLM fails, transcription still posted to Discord

---
