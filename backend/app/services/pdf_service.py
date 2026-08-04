from langchain_community.document_loaders import PyPDFLoader


class PDFService:

    def load_pdf(self, pdf_path: str):

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()

        return documents