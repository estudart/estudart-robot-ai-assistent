from __future__ import annotations

import os

from src.application.services.logging_service import LoggingService


class SpeechAdapter:
	def __init__(self, *, logging_service: LoggingService) -> None:
		self._logging = logging_service

	def speak(self, text: str) -> None:
		text = str(text).strip()
		if not text:
			self._logging.info("SpeechAdapter: skipped empty utterance.")
			return
		os.system(f'say "{text}"')

		
