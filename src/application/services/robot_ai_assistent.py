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
		audio_adapter: SpeechRecognitionAdapter,
		speech_adapter: SpeechAdapter,
		llm: LLMService,
		logging_service: LoggingService,
	) -> None:
		self._audio_adapter = audio_adapter
		self._speech_adapter = speech_adapter
		self._llm = llm
		self._logging = logging_service

	def start(self) -> None:
		try:
			self._logging.info("RobotAIAssistent started (boilerplate).")
			self._logging.info("Services wired: STT, TTS, LLM.")

			self._speech_adapter.speak("Starting AI Assistent")

			while True:
				audio = self._audio_adapter.get_audio()

				if not audio:
					continue

				user_interaction = self._audio_adapter.get_text_from_audio(audio)
				if not str(user_interaction).strip():
					self._logging.info("No audio was detected")
					continue

				llm_response = self._llm.get_llm_response(text=user_interaction)
				self._logging.info("Speaking LLM response.")
				self._speech_adapter.speak(text=llm_response)
				self._logging.info("Finished speaking.")
		except KeyboardInterrupt:
			exit()
