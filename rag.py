from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def split_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    return chunks

def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(
        chunks,
        embeddings
    )

    return vectorstore

def get_answer(vectorstore, question):

    docs = vectorstore.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

    prompt = f"""
You are an expert resume analyst.

Analyze the provided resume content and answer the user's question.

If the user asks what role the resume is suited for,
identify likely job titles based on:
- skills
- projects
- technologies
- education

Context:
{context}

Question:
{question}

Provide a detailed answer.
"""

    response = llm.invoke(prompt)

    return response.content