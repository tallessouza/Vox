# 1. Intro Project Analysis and Context

## 1.1 Existing Project Overview

### Analysis Source
- **Type**: IDE-based fresh analysis
- **Analysis Date**: 2025-10-18
- **Project Access**: Full source code available

### Current Project State

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

## 1.2 Available Documentation Analysis

**Available Documentation**: ✗ Minimal

- ✗ Tech Stack Documentation
- ✗ Source Tree/Architecture
- ✗ Coding Standards
- ✗ API Documentation
- ✗ External API Documentation
- ✗ UX/UI Guidelines
- ✗ Technical Debt Documentation

**Note**: This PRD will serve as the primary planning document for Phase 2 enhancement. Architecture documentation will be created separately if needed.

## 1.3 Enhancement Scope Definition

### Enhancement Type
- ✓ **New Feature Addition** (Primary)
- ✓ **Integration with New Systems** (AssemblyAI + Gemini LLM)
- ✗ Major Feature Modification
- ✗ Performance/Scalability Improvements
- ✗ UI/UX Overhaul
- ✗ Technology Stack Upgrade
- ✗ Bug Fix and Stability Improvements

### Enhancement Description

Phase 2 adds intelligent audio transcription and LLM-powered analysis capabilities to the existing Vox Discord bot. Users will be able to upload audio files (including long-duration recordings of 1-2 hours), receive automatic transcriptions via AssemblyAI, and get customized LLM analysis using user-specified prompts processed by Google Gemini.

The enhancement transforms Vox from a simple audio receiver into a comprehensive audio intelligence platform for Discord communities.

### Impact Assessment
- ✗ Minimal Impact (isolated additions)
- ✓ **Moderate Impact** (some existing code changes)
- ✗ Significant Impact (substantial existing code changes)
- ✗ Major Impact (architectural changes required)

**Impact Details**:
- Existing Discord message handling will be extended (not replaced)
- New async processing pipeline will be added
- File handling logic will be enhanced for long-duration files
- Mock database layer will be introduced for future persistence

## 1.4 Goals and Background Context

### Goals

- Enable automatic transcription of audio files using AssemblyAI API
- Allow users to specify custom LLM prompts for analyzing transcribed content
- Support processing of long-duration audio files (1-2 hours) asynchronously
- Provide clear, formatted output with both transcription and LLM analysis
- Handle concurrent audio processing from multiple users
- Prepare infrastructure for future database persistence (via mock layer)
- Maintain reliability and user experience of existing Discord bot functionality

### Background Context

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

### Change Log

| Change | Date | Version | Description | Author |
|--------|------|---------|-------------|--------|
| Initial PRD | 2025-10-18 | 1.0 | Created Phase 2 enhancement PRD based on user requirements | PM Agent |

---
