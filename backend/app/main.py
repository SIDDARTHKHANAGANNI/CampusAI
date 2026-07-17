from fastapi import FastAPI

from backend.app.api.students import router as student_router
from backend.app.models.student import Student
from backend.app.models.academic import AcademicRecord
from backend.app.models.skill import Skill
from backend.app.models.project import Project
from backend.app.models.career_goal import CareerGoal
from backend.app.api.academics import router as academics_router
from backend.app.api.skills import router as skills_router
from backend.app.api.projects import router as projects_router
from backend.app.api.career_goals import router as career_goals_router
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.auth import router as auth_router




app = FastAPI(
    title="CampusAI API",
    description="Backend API for CampusAI Student Success & Career Platform",
    version="0.3.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(student_router)
app.include_router(academics_router)
app.include_router(skills_router)
app.include_router(projects_router)
app.include_router(career_goals_router)
app.include_router(auth_router)

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