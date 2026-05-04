from __future__ import annotations

from src.application.services.logging_service import LoggingService


class SpeechToTextService:
	"""
	Boilerplate STT service.

	Implementations might use on-device Whisper, Vosk, or a cloud provider.
	"""

	def __init__(self, *, logging_service: LoggingService) -> None:
		self._logging = logging_service

	def transcribe_once(self) -> str:
		self._logging.info("SpeechToTextService.transcribe_once() called (stub).")
		return ""

