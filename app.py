from transformers import pipeline
import re

# 1. Initialize Hugging Face sentiment pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# 2. Define your filler words
FILLER_WORDS = {"um", "uh", "like", "you know", "erm", "ah"}

def load_transcript(path: str) -> list[tuple[str, str]]:
    """
    Reads transcript.txt and returns a list of (speaker, utterance) tuples.
    Expects lines like: "Speaker A: text..."
    """
    turns = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            speaker, text = line.split(":", 1)
            turns.append((speaker.strip(), text.strip()))
    return turns

def compute_sentiment(text: str) -> dict:
    """
    Uses HF pipeline to return a dict:
      {
        'label': 'POSITIVE'|'NEGATIVE'|'NEUTRAL',
        'score': float
      }
    """
    result = sentiment_analyzer(text[:512])[0]
    # Hugging Face’s default labels are 'POSITIVE'/'NEGATIVE';
    # you could bucket around score=0.5 for a 'NEUTRAL' label if desired.
    return {"label": result["label"], "score": result["score"]}

def compute_filler_ratio(text: str) -> float:
    """
    Counts filler words / total words.
    """
    # Normalize and split
    words = re.findall(r"\b\w[\w']*\b", text.lower())
    if not words:
        return 0.0
    filler_count = sum(1 for w in words if w in FILLER_WORDS)
    return filler_count / len(words)

if _name_ == "_main_":
    # Quick smoke test
    transcript = load_transcript("transcript.txt")
    for speaker, utterance in transcript:
        sent = compute_sentiment(utterance)
        filler_ratio = compute_filler_ratio(utterance)
        print(f"{speaker}: {utterance}")
        print(f"  → Sentiment: {sent['label']} ({sent['score']:.2f})")
        print(f"  → Filler ratio: {filler_ratio:.2%}\n")
