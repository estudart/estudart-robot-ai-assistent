# RobotAIAssistent (PiCrawler Robot)

Service intended to run on a **Raspberry Pi** alongside the **Sunfounder PiCrawler AI** robot, providing the scaffolding for an on-device “AI assistant”.

This repository is **boilerplate only**: it wires components and defines the service boundaries, but does **not** implement any speech/LLM logic yet.

## What it contains

- **SpeechToText**: stub service for capturing audio and producing text (`SpeechToTextService`)
- **TextToSpeech**: stub service for speaking text (`TextToSpeechService`)
- **LLM**: stub service for generating responses (`LLMService`)
- **Assistant orchestrator**: a single application service that wires STT + TTS + LLM (`RobotAIAssistent`)
- **Composition root**: dependency wiring in `src/presentation/dependencies.py`

## Run with Docker (recommended)

```bash
make run
```

Follow logs:

```bash
make logs
```

Stop:

```bash
make down
```

## Run locally (no Docker)

```bash
python -m pip install -r requirements.txt
python -m src.presentation.main
```

## Project layout

- `src/application/services/`: application-level orchestration (`RobotAIAssistent`)
- `src/infrastructure/`: external service adapters (STT/TTS/LLM stubs)
- `src/presentation/`: composition root (dependency injection)

## Next steps (when you’re ready)

- Implement audio input + STT (on-device or cloud)
- Implement TTS output (on-device or cloud)
- Implement LLM backend (local or remote)
- Add an API surface for clients (e.g., WebSocket or REST) if needed by your architecture

