from transformers import pipeline
from keybert import KeyBERT

# Load models once
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

kw_model = KeyBERT()


def generate_summary(text: str) -> str:
    if len(text.split()) < 50:
        return text  # Too small to summarize properly

    summary = summarizer(
        text,
        max_length=120,
        min_length=60,
        do_sample=False
    )[0]["summary_text"]

    return summary


def generate_bullet_points(text: str):
    summary = summarizer(
        text,
        max_length=150,
        min_length=80,
        do_sample=False
    )[0]["summary_text"]

    sentences = summary.split(". ")
    bullets = [s.strip() for s in sentences if len(s.split()) > 6]

    return bullets[:5]


def extract_keywords(text: str):
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        top_n=6
    )
    return [kw[0] for kw in keywords]
