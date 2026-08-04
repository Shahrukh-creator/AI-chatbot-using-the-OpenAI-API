from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity


# Create the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Our sentences
sentence1 = "Python is a programming language."

sentence2 = "Python is used for software development."

sentence3 = "The weather is very cold today."


# Convert sentences into vectors
vector1 = embeddings.embed_query(sentence1)

vector2 = embeddings.embed_query(sentence2)

vector3 = embeddings.embed_query(sentence3)


# Calculate similarity
similarity_1_2 = cosine_similarity(
    [vector1],
    [vector2]
)[0][0]


similarity_1_3 = cosine_similarity(
    [vector1],
    [vector3]
)[0][0]


print("Sentence 1:")
print(sentence1)

print("\nSentence 2:")
print(sentence2)

print("\nSimilarity between Sentence 1 and Sentence 2:")
print(similarity_1_2)


print("\nSentence 3:")
print(sentence3)

print("\nSimilarity between Sentence 1 and Sentence 3:")
print(similarity_1_3)