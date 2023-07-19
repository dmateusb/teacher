import whisper
from typing import Text

class AudioTranscriptor:
    
    def __init__(self, model: Text = "base") -> None:
        self.__model = whisper.load_model(model)

    def transcript(self, audio_path: Text):
        transcription = self.__model.transcribe(audio_path)
        return transcription.get("text")
