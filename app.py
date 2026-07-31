from dotenv import load_dotenv

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

website_url = "https://ABC.com"

print("Loading website...")

loader = WebBaseLoader(website_url)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)

vectorstore = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings
)

retriever = vectorstore.as_retriever()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3
)

system_prompt = """
You are a helpful AI assistant.

Answer the user's question only using the provided context.

If the answer is not available in the context, simply reply:
"I don't know."

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

document_chain = create_stuff_documents_chain(
    llm,
    prompt
)

rag_chain = create_retrieval_chain(
    retriever,
    document_chain
)

print("\nWebsite Chatbot Ready!")
print("Type 'exit' to stop.\n")

while True:

    query = input("You : ")

    if query.lower() == "exit":
        break

    response = rag_chain.invoke(
        {
            "input": query
        }
    )

    print("\nBot :", response["answer"])