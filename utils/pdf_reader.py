import fitz  # PyMuPDF

def extract_text_from_pdfs(uploaded_files):
    full_text = ""
    for file in uploaded_files:
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        for page in pdf:
            full_text += page.get_text()
    return full_text
