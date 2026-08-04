from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


text = "Python is a programming language."


vector = embeddings.embed_query(text)


print("Number of dimensions:", len(vector))

print("First 10 numbers:", vector[:10])