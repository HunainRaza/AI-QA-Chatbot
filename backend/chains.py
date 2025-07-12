from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline, AutoModelForCausalLM
import torch

_llm = None

def load_llm():
    global _llm
    if _llm is None:
        # Better model options (choose one):
        
        # Option 1: Slightly larger T5 model (better answers)
        model_id = "google/flan-t5-large"  # Better than base, still manageable
        
        # Option 2: Small but capable causal LM (uncomment to use)
        # model_id = "microsoft/DialoGPT-medium"
        
        # Option 3: Instruction-tuned model (best for Q&A)
        # model_id = "google/flan-t5-xl"  # Much better but heavier
        
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        
        # For T5 models
        if "t5" in model_id.lower():
            model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
            task = "text2text-generation"
        else:
            # For causal LM models
            model = AutoModelForCausalLM.from_pretrained(model_id)
            task = "text-generation"
        pipe = pipeline(
            task,
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True,
            device=0 if torch.cuda.is_available() else -1
        )
        _llm = HuggingFacePipeline(pipeline=pipe)
    return _llm

def get_answer(context: str, question: str):
    llm = load_llm()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    texts = text_splitter.split_text(context)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"}
    )
    db = FAISS.from_texts(texts, embeddings)
    
    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}  # Retrieve more relevant chunks
    )
    chain = RetrievalQA.from_chain_type(
        llm=llm, 
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={
            "prompt_template": "Context: {context}\n\nQuestion: {question}\n\nProvide a detailed and helpful answer based on the context above:"
            }
    )

    response = chain.invoke({"query": question})
    return response["result"]