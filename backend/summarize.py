from transformers import pipeline

# Load summarization model once
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text: str) -> str:
    if len(text.strip()) < 40:
        return text

    summary = summarizer(
        text,
        max_length=60,
        min_length=25,
        do_sample=False
    )

    return summary[0]["summary_text"]
