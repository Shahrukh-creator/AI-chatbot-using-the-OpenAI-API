import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load .env file
load_dotenv()

# Create LLM
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

question = input("Ask something: ")

response = llm.invoke([
    HumanMessage(content=question)
])

print("\nAnswer:\n")
print(response.content)