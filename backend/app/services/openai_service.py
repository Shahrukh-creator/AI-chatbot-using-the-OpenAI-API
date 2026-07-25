from openai import OpenAI

from app.config import Settings
from app.models.chat import ChatMessage


class OpenAIService:

    def __init__(self, settings: Settings):

        self.client = OpenAI(
            api_key=settings.openai_api_key
        )

        self.model = settings.openai_model

    def chat(
        self,
        message: str,
        history: list[ChatMessage]
    ):

        messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ]

        for item in history:

            messages.append({
                "role": item.role,
                "content": item.content
            })

        messages.append({
            "role": "user",
            "content": message
        })

        response = self.client.responses.create(
            model=self.model,
            input=messages
        )

        return response.output_text, self.model