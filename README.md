# 📚 RAG Chatbot (Open Source LLM)

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-blue?logo=streamlit)](https://rag-chatbot-nr54szjhrfkjszz3opmwj4.streamlit.app/)

This is a **Retrieval-Augmented Generation (RAG) chatbot** built with **LangChain**, **open-source LLMs**, and **Streamlit**. It answers user queries based on a static knowledge base (`faq.csv`), combining semantic search and generation.

---

## 🚀 Live Demo

👉 **Try it here**: [https://rag-chatbot-nr54szjhrfkjszz3opmwj4.streamlit.app](https://rag-chatbot-nr54szjhrfkjszz3opmwj4.streamlit.app/)

---

## ✨ Features

- 🔎 Retrieval-Augmented Generation using LangChain + FAISS
- 🤖 Open-source LLM (FLAN-T5) for answer generation
- 📚 Static FAQ knowledge base (`faq.csv`)
- 🧼 Clear chat button
- 🔄 Scrollable chat history
- ⚡ Efficient local inference via HuggingFace Transformers

---

## 🗂️ Project Structure

```
├── app.py              # Streamlit UI
├── rag_pipeline.py     # Pipeline: load CSV, embed docs, run RAG
├── faq.csv             # Knowledge base (user-defined FAQ)
├── requirements.txt    # Dependencies
├── README.md           # You're here
```

---

## 🧠 How It Works

1. Loads the `faq.csv` file (must have an `answer` column)
2. Splits content into chunks
3. Uses SentenceTransformers to create vector embeddings
4. Stores in a FAISS vectorstore for fast retrieval
5. Queries are embedded → relevant chunks retrieved
6. FLAN-T5 generates an answer based on retrieved context

---

## 🛠️ Installation

```bash
git clone https://github.com/Abhisek-Tiwari/RAG-Chatbot.git
cd RAG-Chatbot
pip install -r requirements.txt
streamlit run app.py
```

---

## 🧾 Sample `faq.csv` Format

```csv
question,answer
What is your return policy?,You can return any item within 30 days.
How long does shipping take?,Shipping takes 3-5 business days.
```

Only the **`answer`** column is used in the current implementation.

---

## 📦 Tech Stack

- [LangChain](https://www.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)
- [Transformers (HuggingFace)](https://huggingface.co/)
- [Streamlit](https://streamlit.io/)

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).
