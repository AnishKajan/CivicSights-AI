from transformers import pipeline
import os

# Load model once
image_classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

def classify(image_path: str):
    if not os.path.exists(image_path):
        return "Invalid image path", 0.0
    result = image_classifier(image_path)
    label = result[0]["label"]
    confidence = float(result[0]["score"])
    return label, round(confidence, 4)
