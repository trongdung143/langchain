from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import VECTOR_DB_PATH


def read_vertors_db(course_id, lesson_id) -> FAISS:
    vector_db_path = VECTOR_DB_PATH.format(course_id=course_id, lesson_id=lesson_id)
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    db = FAISS.load_local(
        vector_db_path, embedding, allow_dangerous_deserialization=True
    )
    return db
