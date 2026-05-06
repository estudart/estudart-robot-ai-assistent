from __future__ import annotations

from src.application.services.logging_service import LoggingService



class SpeechAdapter:
	"""
	Speech adapter for PiCrawler.

	Single-class adapter:
	- If `robot_hat` is available, uses it.
	- Otherwise, falls back to logging only (no hardware required).
	"""

	def __init__(self, *, logging_service: LoggingService) -> None:
		self._logging = logging_service

	def speak(self, text: str) -> None:
		self._logging.info("SpeechAdapter.speak() (robot_hat).")
		tts = TTS()
		tts.say(text)