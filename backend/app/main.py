from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.students import router as student_router
from backend.app.api.academics import router as academics_router
from backend.app.api.skills import router as skills_router
from backend.app.api.projects import router as projects_router
from backend.app.api.career_goals import router as career_goals_router
from backend.app.api.auth import router as auth_router

from backend.app.models.student import Student
from backend.app.models.academic import AcademicRecord
from backend.app.models.skill import Skill
from backend.app.models.project import Project
from backend.app.models.career_goal import CareerGoal

from backend.app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    general_exception_handler,
)

from backend.app.core.logger import logger
from backend.app.core.middleware import RequestLoggingMiddleware


app = FastAPI(
    title="CampusAI API",
    description="Backend API for CampusAI Student Success & Career Platform",
    version="0.3.0"
)


# -----------------------------
# Middleware
# -----------------------------
app.add_middleware(RequestLoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Global Exception Handlers
# -----------------------------
app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    Exception,
    general_exception_handler
)


# -----------------------------
# Routers
# -----------------------------
app.include_router(auth_router)
app.include_router(student_router)
app.include_router(academics_router)
app.include_router(skills_router)
app.include_router(projects_router)
app.include_router(career_goals_router)


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def root():
    logger.info("Root endpoint accessed")

    return {
        "message": "Welcome to CampusAI API",
        "status": "running"
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# -----------------------------
# Testing Endpoints
# -----------------------------
@app.get("/test-http")
def test_http():
    raise HTTPException(
        status_code=404,
        detail="This is a test"
    )


@app.get("/test-error")
def test_error():
    return 10 / 0