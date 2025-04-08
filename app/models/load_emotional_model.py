from langchain_together import Together
from app.config import TOGETHER_API_KEY

llm = Together(
    model="NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
    temperature=0.8,
    together_api_key=TOGETHER_API_KEY,
    max_tokens=1500,
)
