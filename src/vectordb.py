from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

def docs_to_retriever(docs):
    # quebra o texto em pedaços (chunks)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    documents = text_splitter.split_documents(docs)

    # cria uma instância embeddings (da OpenAI)
    embeddings = OpenAIEmbeddings()

    # cria uma instância do banco de dados vetorial (FAISS) e armazena os vetores (embeddings) dos chunks (documents)
    vector = FAISS.from_documents(documents, embeddings)

    # cria uma instância do retriever (metodo esperados pelas LLMs nas chains, com o contexto do seu prompt baseado nos chunks dos documents)
    retriever = vector.as_retriever()

    return retriever

def url_to_retriever(url):
    loader = WebBaseLoader(url)
    docs = loader.load()

    return docs_to_retriever(docs)

def pdf_to_retriever(path):
    loader = PyPDFLoader(path)
    docs = loader.load()

    return docs_to_retriever(docs)