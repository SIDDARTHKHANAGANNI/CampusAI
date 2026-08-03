from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from backend.app.schemas.ml import (
    ResumeAnalysisRequest, ResumeAnalysisResponse,
    ResumeMatchRequest, ResumeMatchResponse,
    PlacementReadinessRequest, PlacementReadinessResponse,
    AcademicRiskResponse,
    LearningPathRequest, LearningPathResponse,
    CareerRecommendationRequest, CareerRecommendationResponse
)
from backend.app.services.ml_service import MLService
from backend.app.core.dependencies import get_current_student
from backend.app.database.database import get_db
from backend.app.core.logger import logger

from backend.app.models.skill import Skill
from backend.app.models.project import Project
from backend.app.models.academic import AcademicRecord
from backend.app.models.career_goal import CareerGoal

router = APIRouter(prefix="/ml", tags=["ML Features"])

@router.post("/resume-analysis", response_model=ResumeAnalysisResponse)
async def analyze_resume(
    request: ResumeAnalysisRequest,
    current_student = Depends(get_current_student)
):
    try:
        logger.info(f"Analyzing resume for student: {current_student.id}")
        result = MLService.analyze_resume(request.resume_text, request.target_role)
        return ResumeAnalysisResponse(**result)
    except Exception as e:
        logger.error(f"Error analyzing resume: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to analyze resume")

@router.post("/resume-matching", response_model=ResumeMatchResponse)
async def match_resume(
    request: ResumeMatchRequest,
    current_student = Depends(get_current_student)
):
    try:
        logger.info(f"Matching resume to JD for student: {current_student.id}")
        result = MLService.match_resume_to_job(request.resume_text, request.job_description)
        return ResumeMatchResponse(**result)
    except Exception as e:
        logger.error(f"Error matching resume: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to match resume")

@router.post("/placement-readiness", response_model=PlacementReadinessResponse)
async def placement_readiness(
    request: PlacementReadinessRequest,
    current_student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    try:
        logger.info(f"Calculating placement readiness for student: {current_student.id}")
        skills = db.query(Skill).filter(Skill.student_id == current_student.id).all()
        projects = db.query(Project).filter(Project.student_id == current_student.id).all()
        academics = db.query(AcademicRecord).filter(AcademicRecord.student_id == current_student.id).all()
        
        result = MLService.predict_placement_readiness(current_student, skills, projects, academics)
        return PlacementReadinessResponse(**result)
    except Exception as e:
        logger.error(f"Error calculating placement readiness: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to calculate placement readiness")

@router.get("/academic-risk", response_model=AcademicRiskResponse)
async def academic_risk(
    current_student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    try:
        logger.info(f"Predicting academic risk for student: {current_student.id}")
        academics = db.query(AcademicRecord).filter(AcademicRecord.student_id == current_student.id).all()
        
        result = MLService.predict_academic_risk(current_student, academics)
        return AcademicRiskResponse(**result)
    except Exception as e:
        logger.error(f"Error predicting academic risk: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to predict academic risk")

@router.post("/learning-path", response_model=LearningPathResponse)
async def learning_path(
    request: LearningPathRequest,
    current_student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    try:
        logger.info(f"Generating learning path for student: {current_student.id}, role: {request.target_role}")
        skills = db.query(Skill).filter(Skill.student_id == current_student.id).all()
        skill_names = [skill.name for skill in skills]
        
        result = MLService.generate_learning_path(request.target_role, skill_names, request.timeline_months)
        return LearningPathResponse(**result)
    except Exception as e:
        logger.error(f"Error generating learning path: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate learning path")

@router.post("/career-recommendation", response_model=CareerRecommendationResponse)
async def career_recommendation(
    request: CareerRecommendationRequest,
    current_student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    try:
        logger.info(f"Recommending careers for student: {current_student.id}")
        skills = db.query(Skill).filter(Skill.student_id == current_student.id).all()
        projects = db.query(Project).filter(Project.student_id == current_student.id).all()
        
        result = MLService.recommend_careers(current_student, skills, projects)
        return CareerRecommendationResponse(**result)
    except Exception as e:
        logger.error(f"Error recommending careers: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to recommend careers")
