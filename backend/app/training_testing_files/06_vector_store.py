from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


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
# 4. CREATE VECTOR STORE
# --------------------------------------------------

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="pdf_chatbot"
)


print("Vector store created successfully!")


# --------------------------------------------------
# 5. ASK A QUESTION
# --------------------------------------------------

question = input("\nAsk a question about your PDF: ")


# --------------------------------------------------
# 6. SEARCH VECTOR STORE
# --------------------------------------------------

results = vector_store.similarity_search(
    question,
    k=3
)


# --------------------------------------------------
# 7. DISPLAY RESULTS
# --------------------------------------------------

print("\n===== RELEVANT CHUNKS =====")


for i, document in enumerate(results):

    print(f"\n--- Result {i + 1} ---")

    print("Page:", document.metadata.get("page"))

    print("\nContent:")

    print(document.page_content)