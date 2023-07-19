from pygame import mixer, time as tm
from typing import Text


class AudioPlayer:

    def play(self, file_path: Text):    
        mixer.init()
        mixer.music.load(file_path)
        mixer.music.play()
        
        while mixer.music.get_busy():
            tm.wait(100) 
        
        mixer.music.stop()
        mixer.quit()