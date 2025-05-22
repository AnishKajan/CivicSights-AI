# backend/app/routes/users.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User

router = APIRouter()

@router.post("/create")
def create_user(user_id: str, name: str, email: str, db: Session = Depends(get_db)):
    user = User(id=user_id, name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
