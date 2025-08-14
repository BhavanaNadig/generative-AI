from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    chunks = [text[i:i+1024] for i in range(0, len(text), 1024)]
    summary = ""
    for chunk in chunks:
        part = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary += part[0]['summary_text'] + " "
    return summary.strip()
