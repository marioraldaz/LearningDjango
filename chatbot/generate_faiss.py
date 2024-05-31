
from langchain.tools.retriever import create_retriever_tool #type:ignore
from langchain_community.document_loaders import WebBaseLoader, TextLoader #type:ignore
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter #type:ignore
from langchain_openai import OpenAIEmbeddings #type:ignore
from langchain_community.vectorstores import FAISS #type:ignore
import os


os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_KEY')

loader = TextLoader("./nutrition_info.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)
db.save_local("nutrition_vector_database") #Save database

loader = TextLoader("./database_info.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)
db.save_local("database_info_vector_database") #Save database

