# Projeto LangChain OpenAI

## Visão Geral
Este projeto combina as capacidades da biblioteca LangChain com a API da OpenAI para criar aplicações avançadas de processamento de linguagem natural, incluindo resposta a perguntas e recuperação de informações a partir de documentos e conteúdos online.

## Pré-requisitos
- Python 3.x
- Uma chave API válida da OpenAI

## Instalação
1. Clone o repositório ou faça download dos arquivos necessários.
2. Crie e ative um ambiente virtual Python, se desejar.
3. Instale as dependências utilizando o comando: `pip install -r requirements.txt`.
4. Configure o arquivo `.env` com sua chave API da OpenAI seguindo o exemplo do `.env.example`.

## Funcionalidades

### Geração de Respostas a Perguntas (chatgpt.py)
Utilize a funcionalidade de Q&A para interagir com um modelo de linguagem treinado, enviando perguntas e recebendo respostas contextualizadas.

### Recuperação de Documentos e Informações (vectordb.py)
Capacidade de processar e recuperar informações de documentos em vários formatos, como páginas web e PDFs, dividindo-os em pedaços gerenciáveis para análise e recuperação de dados.

### Integração de Recuperação de Informações com Geração de Texto (rag.py)
Combine documentos e geração de texto para responder a perguntas com base em informações extraídas de documentos específicos, automatizando a carga, processamento e análise de conteúdos.

## Contribuindo
Contribuições são bem-vindas. Para contribuir, faça um fork do repositório, adicione suas alterações e submeta um pull request.

## Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

**Nota Importante**: Mantenha suas credenciais de API seguras e não as exponha publicamente.