import PyPDF2
from docx import Document

def extract_text_from_file(filepath: str) -> str:
    ext = filepath.split('.')[-1].lower()
    
    if ext == 'pdf':
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text
    elif ext == 'docx':
        doc = Document(filepath)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif ext == 'txt':
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        raise ValueError("Unsupported file type")