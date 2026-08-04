from langchain_chroma import Chroma
import os
import shutil


class VectorStoreService:

    def __init__(self, embedding_model):

        self.embedding_model = embedding_model

        self.persist_directory = "chroma_db"

        self.collection_name = "pdf_chatbot"

        self.vector_store = None

    def create_vector_store(self, chunks):

        self.vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=self.persist_directory,
            collection_name=self.collection_name
        )

        return self.vector_store

    def load_vector_store(self):

        self.vector_store = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_model,
            collection_name=self.collection_name
        )

        return self.vector_store

    def similarity_search(self, question, k=3):

        return self.vector_store.similarity_search(
            question,
            k=k
        )


def initialize(self, chunks=None):

    if os.path.exists(self.persist_directory):

        print("Loading existing Chroma database...")

        self.load_vector_store()

    else:

        print("Creating new Chroma database...")

        self.create_vector_store(chunks)


def delete_vector_store(self):

    if os.path.exists(self.persist_directory):
        shutil.rmtree(self.persist_directory)
        