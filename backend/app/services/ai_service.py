from app.models.chat import ChatMessage


class AIService:

    def chat(
        self,
        message: str,
        history: list[ChatMessage],
    ) -> tuple[str, str]:

        text = message.lower().strip()

        if text in ["hi", "hello", "hey"]:
            return (
                "Hello 👋 How can I help you today?",
                "mock-ai-v1",
            )

        elif "name" in text:
            return (
                "I'm your AI assistant built with Angular and FastAPI.",
                "mock-ai-v1",
            )

        elif "python" in text:
            return (
                "Python is an excellent language for AI and backend development.",
                "mock-ai-v1",
            )

        elif "angular" in text:
            return (
                "Angular is a powerful framework for building enterprise web applications.",
                "mock-ai-v1",
            )

        elif "time" in text:
            from datetime import datetime

            return (
                f"The current server time is {datetime.now().strftime('%H:%M:%S')}.",
                "mock-ai-v1",
            )

        return (
            f"You said: '{message}'. This is a mock response. Later this service will call OpenAI or Ollama.",
            "mock-ai-v1",
        )