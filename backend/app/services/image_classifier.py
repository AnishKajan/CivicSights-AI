from transformers import pipeline
import os

classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

def classify_image(image_path: str):
    if not os.path.exists(image_path):
        return "Invalid image path", 0.0
    result = classifier(image_path)
    label = result[0]['label']
    score = float(result[0]['score'])
    return label, round(score, 4)
