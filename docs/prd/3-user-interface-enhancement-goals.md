# 3. User Interface Enhancement Goals

## 3.1 Integration with Existing UI

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

## 3.2 Modified/New User Interactions

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

## 3.3 UI Consistency Requirements

**UCR1**: All bot messages MUST use the existing emoji-based visual language (🎙️, 📝, ⚠️, 🤖)

**UCR2**: Message formatting MUST use Discord markdown (code blocks, bold, etc.) consistently

**UCR3**: Error messages MUST follow existing pattern: `⚠️ Ocorreu um erro: [specific error]`

**UCR4**: Portuguese language MUST be maintained in all bot responses for consistency with existing implementation

---
