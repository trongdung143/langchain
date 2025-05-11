from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.load_emotional_model import llm
from app.services.document_loader import extract_text_from_pdf_path
from app.services.create_prompt import create_prompt_emotion

router = APIRouter()


class PdfRequest(BaseModel):
    emotion: str
    course_id: str
    lesson_id: str


@router.post("/rewrite-pdf-emotion")
async def rewrite_pdf_emotion(request: PdfRequest) -> dict:
    try:
        prompt = create_prompt_emotion()
        text = extract_text_from_pdf_path(request.course_id, request.lesson_id)
        chain = prompt | llm
        rewritten_text = chain.invoke({"style": request.emotion, "content": text})
        return {"rewritten_text": rewritten_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
