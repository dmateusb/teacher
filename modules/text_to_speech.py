from gtts import gTTS
from typing import Text

class TextToSpeech:
    
    def create_speech(self,
        text: Text,
        path:Text ,
        lang:Text="en",
        slow:bool=False
        ) -> None:
        
        myobj = gTTS(text=text, lang=lang, slow=slow)
        myobj.save(path)