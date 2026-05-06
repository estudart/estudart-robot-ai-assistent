from __future__ import annotations

import os
from typing import Dict, Optional

from src.application.services.logging_service import LoggingService
from src.application.services.robot_ai_assistent import RobotAIAssistent
from src.infrastructure.llm_adapter import LLMService
from src.infrastructure.speech_adapter import SpeechAdapter
from src.infrastructure.audio_adapter import SpeechRecognitionAdapter


_logging_by_name: Dict[str, LoggingService] = {}
_audio_adapter: Optional[SpeechRecognitionAdapter] = None
_speech_adapter: Optional[SpeechAdapter] = None
_llm: Optional[LLMService] = None
_assistant: Optional[RobotAIAssistent] = None


def get_logging_service(name: str) -> LoggingService:
	global _logging_by_name
	if name not in _logging_by_name:
		level = os.getenv("LOG_LEVEL", "INFO")
		_logging_by_name[name] = LoggingService(name=name, level=level)
	return _logging_by_name[name]


def get_speech_adapter() -> SpeechAdapter:
	global _speech_adapter
	if _speech_adapter is None:
		_speech_adapter = SpeechAdapter(logging_service=get_logging_service("SpeechAdapter"))
	return _speech_adapter

def get_audio_adapter() -> SpeechRecognitionAdapter:
	global _audio_adapter
	if _audio_adapter is None:
		_audio_adapter = SpeechRecognitionAdapter(
			logging_service=get_logging_service("SpeechRecognition"),
		)
	return _audio_adapter

def get_llm_service() -> LLMService:
	global _llm
	if _llm is None:
		_llm = LLMService(logging_service=get_logging_service("LLM"))
	return _llm

def get_robot_ai_assistent() -> RobotAIAssistent:
	global _assistant
	if _assistant is None:
		_assistant = RobotAIAssistent(
			audio_adapter=get_audio_adapter(),
			speech_adapter=get_speech_adapter(),
			llm=get_llm_service(),
			logging_service=get_logging_service("RobotAIAssistent"),
		)
	return _assistant

