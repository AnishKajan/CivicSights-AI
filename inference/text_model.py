from transformers import pipeline

text_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
CATEGORIES = ["Pothole", "Graffiti", "Trash", "Broken Light", "Water Leak", "Noise Complaint", "Other"]

def classify(text: str):
    result = text_classifier(text, CATEGORIES)
    label = result["labels"][0]
    confidence = float(result["scores"][0])
    return label, round(confidence, 4)
