from langchain_together import Together
from app.config import TOGETHER_API_KEY

llm = Together(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    temperature=0.1,
    top_p=0.9,
    repetition_penalty=1.3,
    max_tokens=512,
    together_api_key=TOGETHER_API_KEY,
)
