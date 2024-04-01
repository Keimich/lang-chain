from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# carrega a chave da OpenAI do arquivo .env
load_dotenv()

def ask(question):
    # cria o prompt para ser usado no LLM da OpenAI
    prompt = PromptTemplate(
        input_variables=["question"],
        template="Pergunta: {question}")

    # cria uma chain vinculando o LLM e o prompt
    chain = LLMChain(llm=llm, prompt=prompt)

    # retorna a resposta do LLM para o prompt
    return chain.invoke({"question": question})

# cria uma instância do LLM da OpenAI (temperatura = de 0 a 1, quanto mais perto do 1 mais criativa as respostas)
llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo-instruct")