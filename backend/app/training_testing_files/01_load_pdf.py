from langchain_community.document_loaders import PyPDFLoader


pdf_path = "01_load.pdf"

loader = PyPDFLoader(pdf_path)

# LangChain converted your PDF into a list of Document objects.
documents = loader.load()


print("Number of documents:", len(documents))

for document in documents:

    print("\n-------------------------")

    print("Page:", document.metadata.get("page"))

    print("Content:")

    print(document.page_content[:500])