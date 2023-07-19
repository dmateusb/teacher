from typing import Any, Text
from modules.chat_gpt import ChatGPT
from modules.audio_player import AudioPlayer
from modules.audio_transcriptor import AudioTranscriptor
from modules.voice_recorder import VoiceRecorder
from modules.text_to_speech import TextToSpeech

class Main:

    __AUDIO_PATH = "res/audio/dialogue.mp3"

    def __init__(self) -> None:
        self.__gpt = ChatGPT()
        self.__audio_player = AudioPlayer()
        self.__audio_transcriptor = AudioTranscriptor()
        self.__voice_recorder = VoiceRecorder(self.__AUDIO_PATH)
        self.__text_to_speech = TextToSpeech()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        first_prompt ="""I want you to act as an interviewer.
        I will be the candidate and you will ask me the interview questions for a fullstack or backend developer position.
        I want you to only reply as the interviewer. Do not write all the conservation at once. I want you to only do the interview with me. Ask me 5 questions and wait for my answers. Do not write explanations. Ask me questions one by one like a human interviewer does and wait for my answers.
        My first sentence is """
        res=self.__gpt.send_prompt(first_prompt, self.handle_error)
        self.__text_to_speech.create_speech(res, self.__AUDIO_PATH)
        self.__audio_player.play(self.__AUDIO_PATH)
        
        while True:
            self.__voice_recorder.record()
            transcription = self.__audio_transcriptor.transcript(self.__AUDIO_PATH)
            res=self.__gpt.send_prompt(transcription, self.handle_error)
            self.__text_to_speech.create_speech(res, self.__AUDIO_PATH)
            self.__audio_player.play(self.__AUDIO_PATH)

    def handle_error(self, *args, **kwargs):
        print(kwargs.get("error"))
        exit()

Main()()