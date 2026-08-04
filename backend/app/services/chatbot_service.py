from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


class ChatbotService:

    def __init__(self, vector_store_service):

        self.vector_store_service = vector_store_service

        self.llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0
        )

    def ask(self, question: str):

        # Retrieve relevant chunks
        documents = self.vector_store_service.similarity_search(
            question,
            k=3
        )

        # Build context
        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

        # Prompt
        prompt = f"""
You are a helpful PDF assistant.

Answer ONLY from the context below.

If the answer is not available in the context, reply:

"I couldn't find that information in the uploaded PDF."

Context:
{context}

Question:
{question}
"""

        # Ask GPT
        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content