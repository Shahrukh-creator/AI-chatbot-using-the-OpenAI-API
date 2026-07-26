from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.routers import chat

settings = get_settings()

print("API Key Loaded:", bool(settings.openai_api_key))
print("API Key Prefix:", settings.openai_api_key[:10] if settings.openai_api_key else "Not Found")
print("Model:", settings.openai_model)

app = FastAPI(
    title="AI Chatbot API",
    description="Python FastAPI backend for an Angular chatbot using OpenAI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
