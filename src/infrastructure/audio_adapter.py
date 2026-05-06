from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import speech_recognition as sr

if TYPE_CHECKING:
	from src.application.services.logging_service import LoggingService


class SpeechRecognitionAdapter:
	"""Microphone capture + Google Speech-to-Text (speech_recognition)."""

	def __init__(
		self,
		*,
		language: str = "pt-BR",
		logging_service: Optional["LoggingService"] = None,
	) -> None:
		self._logging = logging_service
		self.recognizer = sr.Recognizer()
		self.language = language
		self._wake_word = "PiCrawler"

		self.recognizer.pause_threshold = 2
		self.recognizer.energy_threshold = 300

	def _log(self, message: str) -> None:
		if self._logging:
			self._logging.info(message)
		else:
			print(message)

	def is_wake_word(self, audio: sr.AudioData) -> bool:
		try:
			text = self.recognizer.recognize_google(audio, language=self.language)
			return self._wake_word in text
		except sr.UnknownValueError:
			return False
		except sr.RequestError as exc:
			self._log(f"SpeechRecognitionAdapter.is_wake_word request error: {exc}")
			return False

	def get_audio(self) -> Optional[sr.AudioData]:
		try:
			with sr.Microphone() as source:
				self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
				return self.recognizer.listen(
					source,
					timeout=5,
					phrase_time_limit=10,
				)
		except sr.WaitTimeoutError:
			return None
		except OSError as exc:
			self._log(f"No microphone or audio backend error: {exc}")
			return None

	def get_text_from_audio(self, audio: sr.AudioData) -> str:
		try:
			text = self.recognizer.recognize_google(audio, language=self.language)
			self._log(f"You said: {text}")
			return text
		except sr.UnknownValueError:
			return ""
		except sr.RequestError as exc:
			self._log(f"SpeechRecognitionAdapter recognition error: {exc}")
			return ""
