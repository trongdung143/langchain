from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import ask, rewrite, home

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(ask.router)
app.include_router(rewrite.router)
app.include_router(home.router)
