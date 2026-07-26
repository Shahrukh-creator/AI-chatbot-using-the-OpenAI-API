from openai import OpenAI

from app.config import Settings
from app.models.chat import ChatMessage


class OpenAIService:

    def __init__(self, settings: Settings):

        if not settings.openai_api_key:
            raise ValueError("OPENAI_API_KEY is missing.")

        self.client = OpenAI(
            api_key=settings.openai_api_key
        )

        self.model = settings.openai_model

    def chat(
        self,
        message: str,
        history: list[ChatMessage]
    ) -> tuple[str, str]:

        messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ]

        # Previous conversation
        for item in history:
            messages.append(
                {
                    "role": item.role,
                    "content": item.content
                }
            )

        # Current user message
        messages.append(
            {
                "role": "user",
                "content": message
            }
        )

        response = self.client.responses.create(
            model=self.model,
            input=messages
        )

        reply = response.output_text or ""

        return reply, self.model