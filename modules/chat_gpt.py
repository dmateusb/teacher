import openai
from typing import Text


class ChatGPT:
    def __init__(self, model: Text ="gpt-3.5-turbo"):
        self.__open_ai = openai
        self.__model = model
        self.__open_ai.api_key = "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"

    def send_prompt(self, text: Text, callback=None):
        try:
            chat_completion = openai.ChatCompletion.create(
                model=self.__model, 
                messages=[{"role": "user", "content": text}]
            )
            return chat_completion.choices[0].message.content
        
        except Exception as e:
            callback( **{"error": str(e)} )