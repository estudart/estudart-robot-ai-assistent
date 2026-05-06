import speech_recognition as sr



class SpeechRecognitionAdapter(IAudioInput):
    def __init__(self, language="pt-BR"):
        self.recognizer = sr.Recognizer()
        self.language = language
        self._wake_word = "PiCrawler"

        self.recognizer.pause_threshold = 1.0
        self.recognizer.energy_threshold = 300

    def is_wake_word(self, audio) -> bool:
        text = self.recognizer.recognize_google(audio, language=self.language)
        if self._wake_word in text:
            return True
        return False

    def get_audio(self) -> sr.AudioData:
        with sr.Microphone() as source:
            try:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )
                return audio
            except sr.UnknownValueError:
                return None
            except sr.RequestError:
                raise

    def get_text_from_adudio(self, audio: sr.AudioData) -> str:
        try:
            text = self.recognizer.recognize_google(audio, language=self.language)
            print(f"Você disse: {text}")
            return text
        except Exception as err:
            raise
