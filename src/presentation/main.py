from __future__ import annotations

from src.presentation.dependencies import get_robot_ai_assistent


def main() -> None:
	assistant = get_robot_ai_assistent()
	assistant.start()


if __name__ == "__main__":
	main()

