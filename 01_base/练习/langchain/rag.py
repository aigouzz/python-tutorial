import os
from dotenv import load_dotenv

load_dotenv()

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5")

# llm = OpenAI(model="deepseek-chat", api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com", model_kwargs={"ignore_model_check": True})
llm = ChatOpenAI(model="deepseek-chat", api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com", temperature=0, )

from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader

loaders = PyPDFLoader('./data/new.pdf')

documents = loaders.load()

from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = splitter.split_documents(documents)
db = Chroma.from_documents(documents=split_docs, embedding=embeddings)
retriever = db.as_retriever()

from langchain.chains import RetrievalQA

qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

while True:
    query = input("请咨询关于文档的相关信息，输入exit退出：")
    if query.lower() == 'exit':
        break
    if not query.strip():
        continue
    response = qa.run(query)
    print("deepSeek回答", response)