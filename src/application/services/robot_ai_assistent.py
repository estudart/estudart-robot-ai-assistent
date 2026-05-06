from __future__ import annotations

from src.application.services.logging_service import LoggingService
from src.infrastructure.audio_adapter import SpeechRecognitionAdapter
from src.infrastructure.speech_adapter import SpeechAdapter
from src.infrastructure.llm_adapter import LLMService


class RobotAIAssistent:
	"""
	High-level orchestrator for an on-device assistant.

	This is boilerplate only: no business logic is implemented yet.
	"""

	def __init__(
		self,
		*,
		speech_to_text: SpeechRecognitionAdapter,
		text_to_speech: SpeechAdapter,
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

		while True:
			audio = self._stt.get_audio()

			if not audio:
				continue

			user_interaction = self._speech_recognition_adapter.get_text_from_adudio(audio)
			llm_response = self._llm.get_llm_response(text=user_interaction)
			self._tts.speak(text=llm_response)


