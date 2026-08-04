from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

from sklearn.metrics.pairwise import cosine_similarity


# --------------------------------------------------
# 1. LOAD PDF
# --------------------------------------------------

pdf_path = "Back.pdf"

loader = PyPDFLoader(pdf_path)

documents = loader.load()

print("Documents:", len(documents))


# --------------------------------------------------
# 2. SPLIT PDF INTO CHUNKS
# --------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print("Chunks:", len(chunks))


# --------------------------------------------------
# 3. CREATE EMBEDDING MODEL
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 4. CREATE EMBEDDINGS FOR ALL CHUNKS
# --------------------------------------------------

chunk_texts = [
    chunk.page_content
    for chunk in chunks
]

chunk_vectors = embeddings.embed_documents(chunk_texts)


print("Created embeddings for all chunks.")


# --------------------------------------------------
# 5. ASK A QUESTION
# --------------------------------------------------

question = input("\nAsk a question about your PDF: ")

print("\nQuestion:", question)


# --------------------------------------------------
# 6. CREATE EMBEDDING FOR QUESTION
# --------------------------------------------------

question_vector = embeddings.embed_query(question)


# --------------------------------------------------
# 7. COMPARE QUESTION WITH EVERY CHUNK
# --------------------------------------------------

similarities = cosine_similarity(
    [question_vector],
    chunk_vectors
)[0]


# --------------------------------------------------
# 8. GET TOP 3 CHUNKS
# --------------------------------------------------

top_indices = similarities.argsort()[-3:][::-1]


# --------------------------------------------------
# 9. DISPLAY RESULTS
# --------------------------------------------------

print("\n\n===== MOST RELEVANT CHUNKS =====")


for index in top_indices:

    print("\n--------------------------------")
    
    print("Similarity:", similarities[index])

    print(
        "Page:",
        chunks[index].metadata.get("page")
    )

    print("\nContent:")

    print(chunks[index].page_content)