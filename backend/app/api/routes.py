import os
import shutil

from fastapi import APIRouter, UploadFile, File

from app.services.pdf_service import PDFService
from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService

router = APIRouter()

pdf_service = PDFService()
embedding_service = EmbeddingService()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    # Create uploads folder if it doesn't exist
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    # Save uploaded PDF
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Load PDF
    documents = pdf_service.load_pdf(file_path)

    # Split into chunks
    chunks = embedding_service.split_documents(documents)

    # Create vector store
    vector_service = VectorStoreService(
        embedding_service.get_embedding_model()
    )

    vector_service.create_vector_store(chunks)

    return {
        "message": "PDF uploaded successfully.",
        "chunks": len(chunks)
    }