# Appendix: Technical Notes

## User Prompt Extraction Pattern

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

## Async Processing Flow

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

## API Usage Estimates

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
