# backend/app/routes/issues.py

from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.issue import Issue
from app.services.image_classifier import classify_image
from app.services.text_classifier import classify_text
from app.services.speech_to_text import transcribe_audio
import shutil
import os
import uuid

router = APIRouter()

@router.post("/submit")
async def submit_issue(
    user_id: str = Form(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
    description: str = Form(None),
    image: UploadFile = File(None),
    audio: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    image_path, audio_path, text_input = None, None, description or ""

    if image:
        img_id = str(uuid.uuid4()) + "_" + image.filename
        image_path = f"data/uploads/{img_id}"
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_label, confidence = classify_image(image_path)
    else:
        image_label, confidence = None, 0.0

    if audio:
        audio_id = str(uuid.uuid4()) + "_" + audio.filename
        audio_path = f"data/uploads/{audio_id}"
        with open(audio_path, "wb") as buffer:
            shutil.copyfileobj(audio.file, buffer)
        transcript = transcribe_audio(audio_path)
        text_input += " " + transcript

    if not image_label:
        image_label, confidence = classify_text(text_input)

    issue = Issue(
        user_id=user_id,
        description=text_input,
        image_path=image_path,
        audio_path=audio_path,
        classification=image_label,
        confidence=confidence,
        latitude=latitude,
        longitude=longitude
    )
    db.add(issue)
    db.commit()
    db.refresh(issue)

    return {
        "issueId": issue.id,
        "classification": image_label,
        "confidence": confidence,
        "status": issue.status
    }
