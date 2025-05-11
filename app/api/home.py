from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get("/")
async def ask_question() -> dict:
    try:
        return {"result": "Hello, World!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
