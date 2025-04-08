from langchain.prompts import PromptTemplate
from app.services.templates import templates


def create_prompt(template) -> PromptTemplate:
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])
    return prompt


def create_prompt_emotion() -> PromptTemplate:
    prompt = PromptTemplate(
        input_variables=["style", "content"],
        template=templates[4],
    )
    return prompt
