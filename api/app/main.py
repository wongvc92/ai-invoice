from fastapi import FastAPI
from .database import init_db

app = FastAPI(title="AI Invoice Backend")

@app.on_event("startup")
def on_startup():
    # Optional: create tables for now; later switch to Alembic migrations
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}