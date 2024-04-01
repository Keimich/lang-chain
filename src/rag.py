from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from vectordb import url_to_retriever, pdf_to_retriever
from chatgpt import llm

prompt = ChatPromptTemplate.from_template("""Responda a pergunta com base apenas no contexto:
    {context}
    Pergunta: {input}
    """)

document_chain = create_stuff_documents_chain(llm, prompt)
#retriever = url_to_retriever("https://python.langchain.com/docs/modules/data_connection/document_transformers/recursive_text_splitter")
retriever = pdf_to_retriever("/home/user/Downloads/harry-potter-e-a-pedra-filosofal.pdf")
retriever_chain = create_retrieval_chain(retriever, document_chain)
response = retriever_chain.invoke({"input": "Descreva fisicamente o Rony Wesley?"})

print(response["answer"])