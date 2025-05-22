from transformers import pipeline

zero_shot = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify(text: str, labels: list):
    result = zero_shot(text, labels)
    return result
