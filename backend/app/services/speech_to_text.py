from transformers import pipeline
import os

asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def transcribe_audio(audio_path: str):
    if not os.path.exists(audio_path):
        return ""
    result = asr_pipeline(audio_path)
    return result.get("text", "")
