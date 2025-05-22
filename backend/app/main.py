# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import issues, inference, users

app = FastAPI(title="CivicSight AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(issues.router, prefix="/api/v1/issues", tags=["Issues"])
app.include_router(inference.router, prefix="/api/v1/inference", tags=["Inference"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Welcome to CivicSight AI backend"}
