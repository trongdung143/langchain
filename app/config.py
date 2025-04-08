from dotenv import load_dotenv
import os

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
PDF_DATA_PATH = os.getenv("PDF_DATA_PATH")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH")
