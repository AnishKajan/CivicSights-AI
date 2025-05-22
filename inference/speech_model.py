from transformers import pipeline
import os

asr = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def transcribe(audio_path: str):
    if not os.path.exists(audio_path):
        return ""
    result = asr(audio_path)
    return result.get("text", "")
