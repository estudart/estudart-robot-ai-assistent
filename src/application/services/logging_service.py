from __future__ import annotations

import logging


class LoggingService:
	def __init__(self, *, name: str, level: str = "INFO") -> None:
		self._logger = logging.getLogger(name)
		if not self._logger.handlers:
			handler = logging.StreamHandler()
			formatter = logging.Formatter(
				"[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
			)
			handler.setFormatter(formatter)
			self._logger.addHandler(handler)

		self._logger.setLevel(getattr(logging, level.upper(), logging.INFO))

	def info(self, message: str) -> None:
		self._logger.info(message)

	def warning(self, message: str) -> None:
		self._logger.warning(message)

	def error(self, message: str, *, exc: Exception | None = None) -> None:
		if exc is None:
			self._logger.error(message)
		else:
			self._logger.error(f"{message}: {exc}")

