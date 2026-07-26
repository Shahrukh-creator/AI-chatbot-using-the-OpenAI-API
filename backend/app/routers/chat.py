from fastapi import APIRouter, Depends, HTTPException

from app.config import Settings, get_settings
from app.models.chat import ChatRequest, ChatResponse
from app.services.openai_service import OpenAIService

router = APIRouter(
    prefix="/api",
    tags=["Chat"],
)


def get_openai_service(
    settings: Settings = Depends(get_settings),
) -> OpenAIService:
    return OpenAIService(settings)


@router.post("/chat", response_model=ChatResponse)
def chat(
    payload: ChatRequest,
    service: OpenAIService = Depends(get_openai_service),
):
    try:
        reply, model = service.chat(
            payload.message,
            payload.history,
        )

        return ChatResponse(
            reply=reply,
            model=model,
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )