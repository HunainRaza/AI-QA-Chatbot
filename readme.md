# 🤖 AI Q&A Chatbot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)

A document-based question-answering chatbot built with **FastAPI**, **Streamlit**, and **LangChain**. This application allows users to upload documents and ask context-specific questions using Retrieval-Augmented Generation (RAG) to get highly accurate, AI-powered answers.

---

## 🚀 Live Demo

Try the application live directly on Hugging Face Spaces:  
👉 **[AI-QA-Chatbot on Hugging Face](https://huggingface.co/spaces/HunainRaza/AI-QA-Chatbot)**

---

## ✨ Features

* 📄 **Multi-Format Support**: Upload `.pdf`, `.docx`, or `.txt` documents easily.
* 🧠 **Contextual Q&A**: Ask detailed questions based on the exact contents of your uploaded documents.
* ⚙️ **RAG Architecture**: Leverages Retrieval-Augmented Generation to ensure AI responses are grounded in your data.
* 🎨 **Modern Interface**: A clean, intuitive web UI powered by Streamlit.

---

## 🛠️ Tech Stack

* **Backend**: FastAPI, LangChain, Hugging Face Transformers
* **Frontend**: Streamlit
* **AI Model**: FLAN-T5 (for high-quality text generation)
* **Vector Store**: FAISS (for rapid, efficient document retrieval)
* **Embeddings**: Sentence Transformers

---

## 📂 Project Structure

```text
AI-QA-Chatbot/
├── backend/
│   ├── main.py          # FastAPI backend server
│   ├── frontend.py      # Streamlit UI frontend
│   ├── chains.py        # LangChain RAG & Q&A logic
│   ├── utils.py         # File processing & chunking utilities
│   └── models.py        # Pydantic data models
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 💻 Quick Start (Local Development)

Follow these steps to run the application on your local machine.

### 1. Clone the repository
```bash
git clone https://github.com/HunainRaza/AI-QA-Chatbot.git
cd AI-QA-Chatbot
```

### 2. Install dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Start the Backend Server
Navigate to the backend folder and start the FastAPI server:
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Start the Frontend Application
Open a **new terminal window/tab**, navigate to the backend folder again, and launch Streamlit:
```bash
cd backend
streamlit run frontend.py
```
> 🌐 The application will automatically open in your browser at `http://localhost:8501`.

---

## 📖 Using the App

1.  **Upload a Document**: Use the sidebar to upload a `.pdf`, `.docx`, or `.txt` file.
2.  **Wait for Processing**: Wait until the UI displays an "uploaded successfully" confirmation.
3.  **Ask Questions**: Type any question related to the document's content in the chat input.
4.  **Get Answers**: The AI will retrieve the relevant context from your file and generate an accurate response!

---

## 🤝 Contributing

Contributions are always welcome! If you have an idea to improve this project, follow these steps:

1.  Fork the repository
2.  Create a feature branch: `git checkout -b feature/amazing-feature`
3.  Commit your changes: `git commit -m 'Add amazing feature'`
4.  Push to the branch: `git push origin feature/amazing-feature`
5.  Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## 🙏 Acknowledgments

* Built using the powerful [LangChain](https://langchain.com/) framework.
* Powered by [Hugging Face Transformers](https://huggingface.co/docs/transformers/index).
* Beautiful UI made effortlessly with [Streamlit](https://streamlit.io/).