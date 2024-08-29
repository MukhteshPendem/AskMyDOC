import os

from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import openai
from langchain.vectorstores import faiss
# Import conversational chain class (check the correct class name in documentation)
from langchain.chains import conversational_retrieval
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY


def get_pdf_text(docs):
    text = ""
    for doc in docs:
        pdf_reader = PdfReader(doc)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text


def get_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=20)
    chunks=text_splitter.split_text(text)
    return chunks


def get_vector_store(chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = faiss.from_texts(chunks,embeddings=embeddings)
    return vector_store


def get_conversational_chunk(vector_store):
    llm = openai()
    memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)
    conversation_chain = conversational_retrieval




