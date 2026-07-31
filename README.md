# Website Q&A Chatbot (RAG)

A **Retrieval-Augmented Generation (RAG)** based chatbot that answers user questions using the content of a website. The application retrieves relevant information from the website and provides accurate, context-aware responses using **Google Gemini**, **LangChain**, and **FAISS**.

---

## Features

* Load and process website content
* Split content into manageable text chunks
* Generate embeddings using Google Gemini
* Store embeddings in a FAISS vector database
* Retrieve the most relevant content for each query
* Generate context-aware answers using RAG
* Interactive command-line chatbot

---

## Tech Stack

* Python
* LangChain
* Google Gemini
* FAISS
* WebBaseLoader
* RecursiveCharacterTextSplitter
* Python Dotenv

---

## Project Workflow

1. Load website content.
2. Clean and split the text into chunks.
3. Create embeddings for each chunk.
4. Store embeddings in a FAISS vector database.
5. Convert the user's question into an embedding.
6. Retrieve the most relevant chunks.
7. Send the retrieved context and user query to the LLM.
8. Generate an accurate answer based only on the retrieved website content (RAG).

---

## Project Structure

```text
Website-Q-A-Chatbot-RAG/
│── app.py
│── .env
│── requirements.txt
│── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Gyanendra-Gupta/Website-Q-A-Chatbot-RAG-.git
cd Website-Q-A-Chatbot-RAG-
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
USER_AGENT=WebsiteRAGBot
```

---

## Run the Project

```bash
python app.py
```

---

## Example

```text
You: What services does the website provide?

Bot: The website provides ...
```

---

## Future Improvements

* Chat history support
* Multiple website support
* PDF and document support
* ChromaDB integration
* Streamlit web interface
* Conversation memory
* Source citations
* Deploy on Render or Hugging Face Spaces

---

## Author

**Gyanendra Gupta**

GitHub: https://github.com/Gyanendra-Gupta/Website-Q-A-Chatbot-RAG-

---

## License

This project is intended for learning and educational purposes.
