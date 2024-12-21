from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load sentiment model
tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
sentiment_labels = ['negative', 'neutral', 'positive']

def analyze_sentiment(description):
    if not description.strip():
        return "neutral"
    inputs = tokenizer(description, return_tensors="pt", truncation=True, max_length=512)
    outputs = model(**inputs)
    return sentiment_labels[torch.argmax(outputs.logits).item()]
