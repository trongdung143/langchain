import fitz
import os
from app.config import PDF_DATA_PATH


def extract_text_from_pdf_path(course_id, lesson_id) -> str:
    pdf_path = PDF_DATA_PATH.format(course_id=course_id, lesson_id=lesson_id)
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found at: {pdf_path}")

    with fitz.open(pdf_path) as doc:
        text = "".join(page.get_text() for page in doc)

    return text
