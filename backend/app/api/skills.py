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


# CREATE SKILL
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


# GET ALL SKILLS OF A STUDENT
@router.get(
    "/{student_id}/skills",
    response_model=list[SkillResponse]
)
def get_skills(
    student_id: int,
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

    skills = db.query(Skill).filter(
        Skill.student_id == student_id
    ).all()

    return skills


# UPDATE SKILL
@router.put(
    "/skills/{skill_id}",
    response_model=SkillResponse
)
def update_skill(
    skill_id: int,
    skill_data: SkillCreate,
    db: Session = Depends(get_db)
):
    skill = db.query(Skill).filter(
        Skill.id == skill_id
    ).first()

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    for key, value in skill_data.model_dump().items():
        setattr(skill, key, value)

    db.commit()
    db.refresh(skill)

    return skill


# DELETE SKILL
@router.delete("/skills/{skill_id}")
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db)
):
    skill = db.query(Skill).filter(
        Skill.id == skill_id
    ).first()

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    db.delete(skill)
    db.commit()

    return {
        "message": "Skill deleted successfully"
    }