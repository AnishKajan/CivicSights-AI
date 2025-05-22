from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
candidate_labels = ["Pothole", "Graffiti", "Trash", "Broken Light", "Water Leak", "Noise Complaint", "Other"]

def classify_text(text: str):
    result = classifier(text, candidate_labels)
    label = result["labels"][0]
    score = float(result["scores"][0])
    return label, round(score, 4)
