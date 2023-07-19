import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from typing import Text


class VoiceRecorder:
    
    __FS = 44100 # Hz
    __recording = True
    __data = []

    def __init__(self, file_path: Text) -> None:
        self.__file_path = file_path
        self.__stream = sd.InputStream(samplerate=self.__FS, channels=2, callback=self.__callback)

    def record(self):
        self.__stream.start()
        input("Press Enter to stop recording...")
        self.__stop()

    def __stop(self):
        self.__stream.stop()
        audio = np.concatenate(self.__data)
        write(self.__file_path, self.__FS, audio)
        print(f"Saved file: {self.__file_path}")

    def __callback(self, indata, frames, time, status):
        if self.__recording:
            self.__data.append(indata.copy())
