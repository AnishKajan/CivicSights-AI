# backend/app/db/seed.py

from app.db.database import Base, engine
from app.models.issue import Issue
from app.models.user import User

def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()
