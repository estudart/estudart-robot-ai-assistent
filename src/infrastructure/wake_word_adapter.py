class WakeWordAdapter:
	def monitor_wake_word(self):
		while True:
			audio = self._speech_recognition_adapter.get_audio()
			if self._speech_recognition_adapter.is_wake_word(audio):
				# logic to start AI Assistent
				pass