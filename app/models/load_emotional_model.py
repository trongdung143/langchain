from langchain_together import Together
from app.config import TOGETHER_API_KEY

# llm = ChatOpenAI(
#     model="gpt-4",
#     temperature=0.8,
#     openai_api_key=OPENAI_API_KEY,
#     max_tokens=2048,
# )

llm = Together(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    temperature=0.9,
    top_p=0.9,
    top_k=50,
    repetition_penalty=1.15,
    together_api_key=TOGETHER_API_KEY,
    max_tokens=3072,
)
