import streamlit as st
import requests

st.title("AI Q&A Chatbot")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])

if uploaded_file:
    try:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        res = requests.post("http://localhost:8000/upload/", files=files)
        
        if res.status_code == 200:
            st.success(f"{uploaded_file.name} uploaded successfully.")
        else:
            st.error(f"Upload failed. Status code: {res.status_code}")
            st.error(f"Response: {res.text}")
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to backend. Make sure the FastAPI server is running on localhost:8000")
    except Exception as e:
        st.error(f"Upload error: {str(e)}")

question = st.text_input("Ask a question about the document:")

if st.button("Get Answer"):
    if not question:
        st.warning("Please enter a question.")
    else:
        try:
            res = requests.post("http://localhost:8000/ask/", json={"question": question})
            
            if res.status_code == 200:
                answer = res.json()["answer"]
                st.write("Answer:", answer)
            else:
                st.error(f"Error: {res.status_code}")
                st.error(f"Response: {res.text}")
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to backend. Make sure the FastAPI server is running on localhost:8000")
        except requests.exceptions.JSONDecodeError:
            st.error("Invalid response from server")
            st.error(f"Response text: {res.text}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Show connection status
if st.button("Test Backend Connection"):
    try:
        res = requests.get("http://localhost:8000/")
        if res.status_code == 200:
            st.success("✅ Backend is running!")
            st.json(res.json())
        else:
            st.error(f"Backend returned status code: {res.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to backend on localhost:8000")
    except Exception as e:
        st.error(f"Connection test failed: {str(e)}")
