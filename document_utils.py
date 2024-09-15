import PyPDF2
import streamlit as st

def process_uploaded_files(uploaded_files):
    documents = []
    if uploaded_files:
        for file in uploaded_files:
            try:
                if file.type == "application/pdf":
                    reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in range(len(reader.pages)):
                        text += reader.pages[page].extract_text()
                    documents.append({"name": file.name, "content": text})
                else:
                    documents.append({"name": file.name, "content": file.getvalue().decode('utf-8')})
            except Exception as e:
                st.error(f"Failed to process file: {file.name}. Error: {str(e)}")
    return documents
