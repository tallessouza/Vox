# Data Models and Schema Changes

## New Data Models

### Transcription Model

**Purpose:** Represent a completed transcription job with LLM analysis results

**Integration:** Mock in-memory storage (Phase 2), future database persistence (Phase 3+)

**Key Attributes:**
- `job_id`: str (UUID) - Unique identifier for the transcription job
- `user_id`: int - Discord user ID who submitted the audio
- `filename`: str - Original audio filename
- `transcription_text`: str - Full transcription from AssemblyAI
- `user_prompt`: str - Custom LLM prompt provided by user
- `llm_result`: str - Analysis result from Gemini
- `timestamp`: datetime - Job creation time
- `status`: str (enum: pending, processing, completed, failed) - Job status

**Relationships:**
- **With Existing:** None (no existing data models)
- **With New:** Standalone model for Phase 2

## Schema Integration Strategy

**Database Changes Required:**
- **New Tables:** None (Phase 2 uses in-memory mock)
- **Modified Tables:** None
- **New Indexes:** None
- **Migration Strategy:** Future migration will create `transcriptions` table from repository interface

**Backward Compatibility:**
- Mock repository is purely additive; removal does not affect existing bot functionality
- No breaking changes to Discord message interface

---
