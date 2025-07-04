from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders.text import TextLoader

import os
from langchain import hub

from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader
import bs4  # BeautifulSoup for parsing HTML

load_dotenv()  # take environment variables

# from .env file
# Load environment variables from .env file

token = os.getenv("OPENAI_SECRET")  # Replace with your actual token
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

loader = WebBaseLoader(
    web_paths=("https://lt.wikipedia.org/wiki/Vilnius",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer()
    ),
)
wiki = loader.load()

MEMORY_FILE = "Vilnius.txt"
    
text_loader = TextLoader(MEMORY_FILE, encoding="utf-8")
content = text_loader.load()

loader = WebBaseLoader(
    web_paths=("https://faktograma.lt/faktu-rinkinys-6-faktai-apie-vilniu/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer()
    ),
)
faktograma = loader.load()

all_info = wiki + content + faktograma

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
splits = text_splitter.split_documents(all_info)

embeddings=OpenAIEmbeddings(
    model="text-embedding-3-small",
    base_url="https://models.inference.ai.azure.com",
    api_key=token, # type: ignore
)

vectorstore = InMemoryVectorStore(embeddings)

_ = vectorstore.add_documents(documents=splits)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
prompt = hub.pull("rlm/rag-prompt")

def format_all_info(all_info):
    print(all_info)
    return "\n\n".join(doc.page_content for doc in all_info)

st.title("Streamlit LangChain Demo")

def generate_response(input_text):
    llm = ChatOpenAI(base_url=endpoint, temperature=0.7, api_key=token, model=model)

    fetched_all_info = vectorstore.search(input_text, search_type="similarity", k=3)

    rag_chain = (
        {"context": retriever | format_all_info, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
        )
    
    
    st.info(rag_chain.invoke(input_text))

    st.subheader("📚 Sources")
    for i, doc in enumerate(fetched_all_info, 1):
        with st.expander(f"Source {i}"):
            st.write(f"**Content:** {doc.page_content}")

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "Paklauskite klausimo apie Vilniu?",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
