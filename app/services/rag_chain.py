from langchain.chains import RetrievalQA


def create_qa_chain(vector_db, llm, prompt) -> RetrievalQA:
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt},
    )
    return qa_chain
