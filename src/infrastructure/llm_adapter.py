from __future__ import annotations

from openai import OpenAI

from src.application.services.logging_service import LoggingService
from src.config import open_ai_key


class LLMService:
	"""
	Boilerplate LLM service.

	Implementations might call a local model (e.g. llama.cpp / Ollama) or a cloud API.
	"""

	def __init__(self, logging_service: LoggingService, model: str = "gpt-4o-mini") -> None:
		self._logging = logging_service
		self._client = OpenAI(api_key=open_ai_key)
		self._model = model

		self._history = [
			{
				"role": "system",
				"content": (
					"You are PiCrawler, a real-time voice assistant running on a local machine. "
					"You speak in a natural, concise, and conversational way. "
					"Keep responses short and clear, suitable for spoken output. "
					"Avoid long paragraphs, lists, or complex formatting. "
					"If the user asks something unclear, ask a short follow-up question. "
					"Be helpful, slightly informal, and efficient."
				)
			}
		]

	def get_llm_response(self, text: str) -> str:
		self._history.append({
			"role": "user",
			"content": text
		})
		response = self._client.responses.create(
			model=self._model,
			input=self._history
		)
		reply = response.output_text.strip()
		self._history.append({
			"role": "assistant",
			"content": reply
		})

		return reply
