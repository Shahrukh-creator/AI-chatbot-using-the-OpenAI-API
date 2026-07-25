from fastapi import APIRouter, Depends

from app.models.chat import ChatRequest, ChatResponse
from app.services.ai_service import AIService

router = APIRouter(prefix="/api", tags=["Chat"])


def get_ai_service():
    return AIService()


@router.post("/chat", response_model=ChatResponse)
def chat(
    payload: ChatRequest,
    service: AIService = Depends(get_ai_service),
):

    reply, model = service.chat(
        payload.message,
        payload.history,
    )

    return ChatResponse(
        reply=reply,
        model=model,
    )