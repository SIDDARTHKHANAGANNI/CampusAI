import json
from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.core.dependencies import get_current_user
from backend.app.models.user import User
from backend.app.models.resume import Resume
from backend.app.schemas.resume import ResumeAnalysisResponse
from backend.app.services.resume_service import analyze_resume
from backend.app.core.logger import logger

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post("/analyze", response_model=ResumeAnalysisResponse)
async def analyze(
    file: UploadFile = File(...),
    target_role: str = Form(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    logger.info(f"Resume analysis requested. User ID: {current_user.id}, Role: {target_role}")

    file_bytes = await file.read()
    result = analyze_resume(file_bytes, file.filename, target_role)

    resume = Resume(
        user_id=current_user.id,
        target_role=target_role,
        raw_text=result["raw_text"],
        score=result["score"],
        ats_score=result["ats_score"],
        extracted_skills=json.dumps(result["extracted_skills"]),
        missing_skills=json.dumps(result["missing_skills"]),
        suggestions=json.dumps(result["suggestions"]),
    )
    db.add(resume)
    db.commit()

    logger.info(f"Resume analysis complete. User ID: {current_user.id}, Score: {result['score']}")

    return result