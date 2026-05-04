from __future__ import annotations

from src.application.services.logging_service import LoggingService
from src.application.services.speech_to_text_service import SpeechToTextService
from src.application.services.text_to_speech_service import TextToSpeechService
from src.infrastructure.llm_adapter import LLMService


class RobotAIAssistent:
	"""
	High-level orchestrator for an on-device assistant.

	This is boilerplate only: no business logic is implemented yet.
	"""

	def __init__(
		self,
		*,
		speech_to_text: SpeechToTextService,
		text_to_speech: TextToSpeechService,
		llm: LLMService,
		logging_service: LoggingService,
	) -> None:
		self._stt = speech_to_text
		self._tts = text_to_speech
		self._llm = llm
		self._logging = logging_service

	def start(self) -> None:
		self._logging.info("RobotAIAssistent started (boilerplate).")
		self._logging.info("Services wired: STT, TTS, LLM.")

