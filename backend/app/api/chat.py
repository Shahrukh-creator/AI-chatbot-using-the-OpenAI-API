from fastapi import APIRouter

from app.models.chat_request import ChatRequest
from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService
from app.services.chatbot_service import ChatbotService

router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)

embedding_service = EmbeddingService()

vector_service = VectorStoreService(
    embedding_service.get_embedding_model()
)

# Load the existing Chroma database
vector_service.load_vector_store()

chatbot = ChatbotService(vector_service)


@router.post("/chat")
async def chat(request: ChatRequest):

    answer = chatbot.ask(request.question)

    return {
        "answer": answer
    }