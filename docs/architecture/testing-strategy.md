# Testing Strategy

## Integration with Existing Tests

**Existing Test Framework:** None (Phase 2 introduces pytest)
**Test Organization:** `tests/` directory with test files matching source structure
**Coverage Requirements:** Target 80% code coverage for new code (services, repository)

## New Testing Requirements

### Unit Tests for New Components

- **Framework:** pytest (async support via pytest-asyncio)
- **Location:** `tests/test_assemblyai_service.py`, `tests/test_gemini_service.py`, `tests/test_repository.py`
- **Coverage Target:** 80% for service layer and repository
- **Integration with Existing:** N/A (no existing tests)

**Test Examples:**
```python
@pytest.mark.asyncio
async def test_assemblyai_service_transcribe_success(mock_assemblyai_api):
    """Test successful transcription with mocked AssemblyAI API."""
    service = AssemblyAIService(api_key="test_key")
    result = await service.transcribe_audio("test.mp3")
    assert result == "Expected transcription text"

@pytest.mark.asyncio
async def test_gemini_service_handles_api_failure():
    """Test graceful handling of Gemini API failure."""
    service = GeminiService(api_key="test_key")
    with pytest.raises(GeminiError):
        await service.process_with_llm("text", "prompt")
```

### Integration Tests

- **Scope:** End-to-end flow from Discord message to posted results (with mocked APIs)
- **Existing System Verification:** Test that `!ping` continues to work after Phase 2 changes
- **New Feature Testing:** Test full audio processing pipeline with mocked AssemblyAI and Gemini

**Example:**
```python
@pytest.mark.asyncio
async def test_full_audio_processing_pipeline(mock_discord_client, mock_assemblyai, mock_gemini):
    """Test complete flow: audio upload → transcription → LLM → Discord post."""
    # Simulate Discord message with audio attachment
    # Verify transcription message posted
    # Verify LLM analysis message posted
    # Verify file cleanup
```

### Regression Testing

- **Existing Feature Verification:** Automated tests for `!ping` command and basic message handling
- **Automated Regression Suite:** Run on every code change
- **Manual Testing Requirements:** Test with real Discord bot in test channel before production deployment

---
