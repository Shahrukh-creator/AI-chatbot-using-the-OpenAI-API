from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.pdf_service import PDFService
from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService

router = APIRouter(prefix="/api", tags=["PDF"])

pdf_service = PDFService()
embedding_service = EmbeddingService()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    documents = pdf_service.load_pdf(file_path)

    chunks = embedding_service.split_documents(documents)

    vector_service = VectorStoreService(
        embedding_service.get_embedding_model()
    )

    vector_service.create_vector_store(chunks)

    return {
        "message": "PDF Uploaded Successfully"
    }