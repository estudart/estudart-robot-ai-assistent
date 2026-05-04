from __future__ import annotations

from src.application.services.logging_service import LoggingService
from src.infrastructure.speech_adapter import SpeechAdapter


class TextToSpeechService:
	"""
	Boilerplate TTS service.

	Implementations might use Piper, Coqui TTS, espeak-ng, or a cloud provider.
	"""

	def __init__(self, *, speech_adapter: SpeechAdapter, logging_service: LoggingService) -> None:
		self._speech_adapter = speech_adapter
		self._logging = logging_service

	def speak(self, text: str) -> None:
		self._logging.info(f"TextToSpeechService.speak() called: {text!r}")
		self._speech_adapter.speak(text)

