from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# 1. Load the PDF
pdf_path = "sample.pdf"

loader = PyPDFLoader(pdf_path)

documents = loader.load()


print("Number of documents:", len(documents))


# 2. Create the text splitter
# chunk_size=1000 is the each 1000 char of the Orginal text
# chunk_overlap --- So the next chunk contains 200 characters from the previous chunk + new characters.
# chunk_overlap
#     ↓
# How much information should be repeated
# between neighboring chunks? So the overal overall context should be understood

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)


# 3. Split documents into chunks
chunks = text_splitter.split_documents(documents)


print("Number of chunks:", len(chunks))


# 4. Display the chunks
for i, chunk in enumerate(chunks):

    print("\n==============================")
    print("CHUNK:", i + 1)
    print("==============================")

    print("Page:", chunk.metadata.get("page"))

    print("Text length:", len(chunk.page_content))

    print("Content:")
    print(chunk.page_content)