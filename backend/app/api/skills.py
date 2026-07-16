from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.student import Student
from backend.app.models.skill import Skill
from backend.app.schemas.skill import SkillCreate, SkillResponse


router = APIRouter(
    prefix="/students",
    tags=["Skills"]
)


@router.post(
    "/{student_id}/skills",
    response_model=SkillResponse,
    status_code=201
)
def add_skill(
    student_id: int,
    skill: SkillCreate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    new_skill = Skill(
        student_id=student_id,
        **skill.model_dump()
    )

    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)

    return new_skill