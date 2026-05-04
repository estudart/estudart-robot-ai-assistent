from __future__ import annotations

import os
from typing import Optional

from src.application.services.logging_service import LoggingService
from src.application.services.robot_ai_assistent import RobotAIAssistent
from src.application.services.speech_to_text_service import SpeechToTextService
from src.application.services.text_to_speech_service import TextToSpeechService
from src.infrastructure.llm_adapter import LLMService
from src.infrastructure.speech_adapter import SpeechAdapter


_logging: Optional[LoggingService] = None
_stt: Optional[SpeechToTextService] = None
_tts: Optional[TextToSpeechService] = None
_llm: Optional[LLMService] = None
_assistant: Optional[RobotAIAssistent] = None
_speech_adapter: Optional[SpeechAdapter] = None


def get_logging_service(name: str) -> LoggingService:
	global _logging
	if _logging is None:
		level = os.getenv("LOG_LEVEL", "INFO")
		_logging = LoggingService(name=name, level=level)
	return _logging


def get_speech_to_text_service() -> SpeechToTextService:
	global _stt
	if _stt is None:
		_stt = SpeechToTextService(logging_service=get_logging_service("SpeechToText"))
	return _stt


def get_text_to_speech_service() -> TextToSpeechService:
	global _tts
	if _tts is None:
		_tts = TextToSpeechService(
			speech_adapter=get_speech_adapter(),
			logging_service=get_logging_service("TextToSpeech"),
		)
	return _tts


def get_speech_adapter() -> SpeechAdapter:
	global _speech_adapter
	if _speech_adapter is None:
		_speech_adapter = SpeechAdapter(logging_service=get_logging_service("SpeechAdapter"))
	return _speech_adapter


def get_llm_service() -> LLMService:
	global _llm
	if _llm is None:
		_llm = LLMService(logging_service=get_logging_service("LLM"))
	return _llm


def get_robot_ai_assistent() -> RobotAIAssistent:
	global _assistant
	if _assistant is None:
		_assistant = RobotAIAssistent(
			speech_to_text=get_speech_to_text_service(),
			text_to_speech=get_text_to_speech_service(),
			llm=get_llm_service(),
			logging_service=get_logging_service("RobotAIAssistent"),
		)
	return _assistant

