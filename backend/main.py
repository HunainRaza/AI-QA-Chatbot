from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.utils import extract_text_from_file
from backend.chains import get_answer
import os

app = FastAPI()

UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI Q&A Chatbot Backend Running"}

# Store uploaded document context globally (for simplicity)
DOCUMENT_CONTEXT = {}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    try:
        text = extract_text_from_file(file_path)
        DOCUMENT_CONTEXT['text'] = text
        return {"status": "Document uploaded and processed."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask/")
async def ask_question(request: dict):
    if 'text' not in DOCUMENT_CONTEXT:
        raise HTTPException(status_code=400, detail="No document uploaded yet.")
    answer = get_answer(DOCUMENT_CONTEXT['text'], request['question'])
    return {"answer": answer}
