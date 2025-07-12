AI Q&A Chatbot
A document-based question-answering chatbot built with FastAPI, Streamlit, and LangChain.
Features

Upload PDF, DOCX, or TXT documents
Ask questions about uploaded documents
Get AI-powered answers using Retrieval-Augmented Generation (RAG)
Modern web interface with Streamlit

Quick Start
Local Development

Clone the repository

bashgit clone https://github.com/HunainRaza/AI-QA-Chatbot.git
cd AI-QA-Chatbot

Install dependencies

bashpip install -r requirements.txt

Start the backend

bashcd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000

Start the frontend (in a new terminal)

bashcd backend
streamlit run frontend.py

Open your browser and go to http://localhost:8501

Using the App

Upload a document (PDF, DOCX, or TXT)
Wait for the "uploaded successfully" message
Ask questions about your document
Get AI-powered answers!

Tech Stack

Backend: FastAPI, LangChain, HuggingFace Transformers
Frontend: Streamlit
AI Model: FLAN-T5 for text generation
Vector Store: FAISS for document retrieval
Embeddings: Sentence Transformers

Project Structure
AI-QA-Chatbot/
├── backend/
│   ├── main.py          # FastAPI backend
│   ├── frontend.py      # Streamlit frontend
│   ├── chains.py        # LangChain Q&A logic
│   ├── utils.py         # File processing utilities
│   └── models.py        # Pydantic models
├── requirements.txt     # Python dependencies
└── README.md           # This file

Live Demo
🚀 Try it live on Hugging Face Spaces: [Your App URL]
Contributing

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Built with LangChain
Powered by Hugging Face Transformers
UI created with Streamlit
