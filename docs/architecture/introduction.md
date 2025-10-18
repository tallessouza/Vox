# Introduction

This document outlines the architectural approach for enhancing Vox Discord Bot with intelligent audio transcription and LLM-powered analysis capabilities. Its primary goal is to serve as the guiding architectural blueprint for AI-driven development of new features while ensuring seamless integration with the existing system.

## Relationship to Existing Architecture

This document supplements the existing Vox bot architecture by defining how new components (AssemblyAI transcription, Gemini LLM processing, async pipeline, mock repository) will integrate with the current Discord message handling system. The architecture prioritizes non-breaking, additive changes that preserve the reliability of the existing bot while delivering substantial new value.

## Existing Project Analysis

### Current Project State

- **Primary Purpose:** Discord bot for receiving and storing audio file attachments
- **Current Tech Stack:** Python 3.x, discord.py 2.6.4, aiohttp 3.13.1, python-dotenv
- **Architecture Style:** Event-driven (Discord message events), monolithic single-file bot
- **Deployment Method:** Server-based deployment (Phase 1 assumed operational)

### Available Documentation

- Brownfield PRD (docs/prd/vox-phase2-prd.md) - Comprehensive requirements for Phase 2
- Minimal existing project documentation (to be created during implementation)
- Source code (bot.py, transcription.py) serves as primary documentation

### Identified Constraints

- **Async Event Loop:** Must not block discord.py's event loop during long-running operations
- **File System:** Local storage in `audios/` directory with manual cleanup required
- **No Database:** Current system has no persistence layer
- **Single Server:** No distributed architecture; all processing on one server
- **Portuguese Language:** All user-facing messages must be in Portuguese
- **Free Tier APIs:** Must use AssemblyAI and Gemini free tiers to minimize costs

## Change Log

| Change | Date | Version | Description | Author |
|--------|------|---------|-------------|--------|
| Initial Architecture | 2025-10-18 | 1.0 | Created Phase 2 enhancement architecture based on PRD and codebase analysis | Architect Agent |

---
