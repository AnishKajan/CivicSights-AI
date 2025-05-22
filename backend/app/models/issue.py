# backend/app/models/issue.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.database import Base
from datetime import datetime

class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    description = Column(String)
    image_path = Column(String)
    audio_path = Column(String)
    classification = Column(String)
    confidence = Column(Float)
    urgency_score = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    status = Column(String, default="Pending")
    timestamp = Column(DateTime, default=datetime.utcnow)
