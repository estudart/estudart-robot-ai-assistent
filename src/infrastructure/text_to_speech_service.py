from __future__ import annotations

from src.application.services.logging_service import LoggingService


class TextToSpeechService:
	"""
	Boilerplate TTS service.

	Implementations might use Piper, Coqui TTS, espeak-ng, or a cloud provider.
	"""

	def __init__(self, *, logging_service: LoggingService) -> None:
		self._logging = logging_service

	def speak(self, text: str) -> None:
		self._logging.info(f"TextToSpeechService.speak() called (stub): {text!r}")

