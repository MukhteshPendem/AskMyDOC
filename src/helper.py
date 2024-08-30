import os

from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings

from langchain_google_vertexai import VertexAI

from  langchain_community.vectorstores import FAISS

from langchain.chains.question_answering import load_qa_chain
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
    embeddings = GooglePalmEmbeddings()
    vector_store = FAISS.from_texts(chunks,embedding=embeddings)
    return vector_store


def get_conversational_chain():
    
    
    llm = VertexAI(model_name="gemini-pro",project_id='original-seeker-426515-t5')
    conversation_chain = load_qa_chain(llm=llm,chain_type='stuff')
    return conversation_chain

def get_answer(query):
    conversation_chain = get_conversational_chain()
    memory = ConversationBufferMemory()
    answer = conversation_chain.run(query, memory=memory)
    return answer

