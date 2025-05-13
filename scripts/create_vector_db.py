from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
)
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
import sys, os

vector_db_path = None
pdf_data_path = None


def create_vector_db_from_text() -> FAISS:
    text = """"""
    text_splitter = CharacterTextSplitter(
        chunk_size=500, chunk_overlap=100, length_function=len, separator="\n"
    )

    texts = text_splitter.split_text(text)
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_texts(texts, embedding)
    db.save_local(vector_db_path)

    return db


def create_vector_db_from_file() -> FAISS:
    loader = PyPDFLoader(pdf_data_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = text_splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.from_documents(texts, embedding)
    db.save_local(vector_db_path)

    return db


folder_path = f"./data/courses/{sys.argv[1]}"
pdf_files = [f for f in os.listdir(folder_path) if f.lower()]

for file in pdf_files:
    pdf_data_path = f"./data/courses/{sys.argv[1]}/{file}"
    vector_db_path = f"./data/vectorstores/{sys.argv[1]}/{file[:-4]}"
    create_vector_db_from_file()
    print(f"Vector DB created successfully for file {file}")
