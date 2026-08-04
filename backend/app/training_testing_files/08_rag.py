import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# -----------------------------
# Load Environment Variables
# -----------------------------

load_dotenv()


# -----------------------------
# Load PDF
# -----------------------------

loader = PyPDFLoader("python-docs.pdf")

documents = loader.load()


# -----------------------------
# Split PDF
# -----------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)


# -----------------------------
# Local Embedding Model
# -----------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -----------------------------
# Chroma Vector Store
# -----------------------------

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="pdf_chatbot"
)


# -----------------------------
# OpenAI LLM
# -----------------------------

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)


print("\nPDF ChatBot Ready!")

while True:

    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    # -----------------------------
    # Retrieve Similar Chunks
    # -----------------------------

    results = vector_store.similarity_search(
        question,
        k=3
    )

    # -----------------------------
    # Build Context
    # -----------------------------

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the information below.

If the answer is not in the context, say:

"I couldn't find that information in the uploaded PDF."

Context:
{context}

Question:
{question}
"""

    # -----------------------------
    # Ask GPT
    # -----------------------------

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    print("\nAnswer:\n")

    print(response.content)