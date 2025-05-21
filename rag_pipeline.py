from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import DataFrameLoader
from langchain.chains import RetrievalQA
from langchain_huggingface.llms import HuggingFacePipeline

import pandas as pd
from transformers import pipeline
from data_loader import load_data

def create_rag_chain(csv_path: str):
    """
    Takes CSV file path as input, builds database with embeddings and makes chain for RAG model
    :param csv_path: Path of CSV file that has the FAQs
    :return: Built Question Answer Chain to use to invoke the queries
    """
    # Load data
    df = load_data(csv_path)
    loader = DataFrameLoader(df, page_content_column="answer")
    documents = loader.load()

    # breaking texts by 500 char factor
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Making embeddings and storing them in VectorDatabase
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

    # Using a small open-source LLM
    qa_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_new_tokens=256
    )

    # Making LLM pipeline
    llm = HuggingFacePipeline(pipeline=qa_pipeline)

    # Making a Final QA chain to pass queries
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
