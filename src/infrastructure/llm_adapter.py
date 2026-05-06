from __future__ import annotations

from src.application.services.logging_service import LoggingService


class LLMService:
	"""
	Boilerplate LLM service.

	Implementations might call a local model (e.g. llama.cpp / Ollama) or a cloud API.
	"""

	def __init__(self, *, logging_service: LoggingService) -> None:
		self._logging = logging_service

		self._prompt = """

		"""

	def get_llm_response(self, text: str) -> str:
		self._logging.info(f"LLMService.complete() called (stub), prompt_len={len(self._prompt)}")
		return text

