# 📚 StudyMate – PDF Q&A, Summarizer & Quiz Generator

*StudyMate* is an interactive tool that lets you upload one or more PDF files (like lecture notes, research papers, or books) and:
- Ask *concept-based questions* directly from your documents
- Get *accurate summaries* of the content
- Generate *quiz questions* to test your understanding

It uses *Natural Language Processing (NLP), **semantic search, and **vector embeddings* to deliver meaningful answers.

---

## 🚀 Features
- 📄 *Multiple PDF Upload* – Combine and search through multiple documents
- 🔍 *Semantic Search* – Finds meaningfully related content, not just keyword matches
- 📝 *Summarization* – Condenses long documents into easy-to-read summaries
- ❓ *Quiz Generation* – Creates quiz questions based on your uploaded content
- ⚡ *Fast Retrieval* – Powered by [FAISS](https://github.com/facebookresearch/faiss) for quick search

---

## 🛠 Technologies Used
| Technology | Purpose |
|------------|---------|
| **[PyMuPDF](https://pymupdf.readthedocs.io/)** | Extracts text from PDFs |
| **[SentenceTransformers](https://www.sbert.net/)** | Generates embeddings (vector representations) |
| **[FAISS](https://github.com/facebookresearch/faiss)** | Vector similarity search engine |
| **[NumPy](https://numpy.org/)** | Efficient numerical operations |
| **[Streamlit](https://streamlit.io/)** | Web app UI framework |
| **[Transformers](https://huggingface.co/transformers/)** | Summarization & quiz generation models |

---

## 📂 Project Structure
studymate/
│
├── pdf_utils.py # Extract text and split into chunks
├── retriever.py # FAISS-based search and retrieval
├── streamlit_app.py # Streamlit web interface
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/studymate.git
cd studymate
2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
▶ Usage
Run the Streamlit app:

bash
Copy
Edit
streamlit run streamlit_app.py
This will open the app in your browser at http://localhost:8501

📖 How It Works
Upload PDFs → The app extracts and combines text from all uploaded files.

Chunking → Splits the text into overlapping segments for better retrieval.

Embedding & Indexing → Each chunk is converted into a vector and stored in FAISS.

Asking Questions → Your query is embedded and compared with stored chunks to find the most relevant answers.

Summarization & Quizzes → The summarization model condenses the document, and the quiz generator creates questions from the text.

🧪 Example Use Cases
Study lecture notes for an exam

Summarize long research papers

Create quick quizzes for self-testing

Extract key points from books or reports

📌 Requirements
Python 3.8+

Internet connection for downloading models
