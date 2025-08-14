import streamlit as st
from utils.pdf_reader import extract_text_from_pdfs
from utils.qa import ask_question
from utils.summarizer import generate_summary
from utils.quiz_generator import generate_quiz

st.set_page_config(page_title="StudyMate - AI PDF Assistant", layout="wide")

st.title("📚 StudyMate - AI PDF-Based Q&A System")

uploaded_files = st.file_uploader("Upload your PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Reading PDFs..."):
        all_text = extract_text_from_pdfs(uploaded_files)
    st.success("✅ PDFs loaded successfully!")

    option = st.sidebar.radio("Choose an option", ["Ask a Question", "Get Summary", "Generate Quiz"])

    if option == "Ask a Question":
        question = st.text_input("Enter your question:")
        if st.button("Get Answer"):
            with st.spinner("Searching for the answer..."):
                answer = ask_question(all_text, question)
            st.write("### Answer:")
            st.write(answer)

    elif option == "Get Summary":
        if st.button("Generate Summary"):
            with st.spinner("Summarizing PDFs..."):
                summary = generate_summary(all_text)
            st.write("### Summary:")
            st.write(summary)

    elif option == "Generate Quiz":
        num_qs = st.slider("Number of questions", 3, 10, 5)
        if st.button("Generate Quiz"):
            with st.spinner("Creating quiz..."):
                quiz = generate_quiz(all_text, num_qs)
            st.write("### Quiz Questions:")
            for i, q in enumerate(quiz, 1):
                st.write(f"*Q{i}.* {q}")
