from fastapi import APIRouter
from app.services.image_classifier import classify_image
from app.services.text_classifier import classify_text
from app.services.speech_to_text import transcribe_audio

router = APIRouter()

@router.get("/image")
def test_image(path: str):
    return classify_image(path)

@router.get("/text")
def test_text(input: str):
    return classify_text(input)

@router.get("/audio")
def test_audio(path: str):
    return transcribe_audio(path)
