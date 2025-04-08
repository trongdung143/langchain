from fastapi import FastAPI
from app.api import ask, rewrite, home

app = FastAPI()

app.include_router(ask.router)
app.include_router(rewrite.router)
app.include_router(home.router)
