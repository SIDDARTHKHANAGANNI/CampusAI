from fastapi import FastAPI

from backend.app.api.students import router as student_router
from backend.app.database.database import Base, engine
from backend.app.models.student import Student


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CampusAI API",
    description="Backend API for CampusAI Student Success & Career Platform",
    version="0.3.0"
)


app.include_router(student_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to CampusAI API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }