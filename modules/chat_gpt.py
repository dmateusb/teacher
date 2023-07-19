import openai
from typing import Text
import os
from dotenv import load_dotenv

class ChatGPT:
    def __init__(self, model: Text ="gpt-3.5-turbo"):
        load_dotenv()
        self.__open_ai = openai
        self.__model = model
        self.__open_ai.api_key = os.getenv("OPEN_AI_API_KEY")

    def send_prompt(self, text: Text, callback=None):
        try:
            chat_completion = openai.ChatCompletion.create(
                model=self.__model, 
                messages=[{"role": "user", "content": text}]
            )
            return chat_completion.choices[0].message.content
        
        except Exception as e:
            callback( **{"error": str(e)} )