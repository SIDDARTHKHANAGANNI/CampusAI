from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.student import Student
from backend.app.models.skill import Skill

from backend.app.schemas.skill import (
    SkillCreate,
    SkillUpdate,
    SkillResponse
)

from backend.app.core.dependencies import get_current_student

router = APIRouter(
    prefix="/students",
    tags=["Skills"]
)


@router.get(
    "/me/skills",
    response_model=list[SkillResponse]
)
def get_my_skills(
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    return db.query(Skill).filter(
        Skill.student_id == student.id
    ).all()


@router.post(
    "/me/skills",
    response_model=SkillResponse,
    status_code=201
)
def add_my_skill(
    skill: SkillCreate,
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    new_skill = Skill(
        student_id=student.id,
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


@router.put(
    "/me/skills/{skill_id}",
    response_model=SkillResponse
)
def update_my_skill(
    skill_id: int,
    skill_data: SkillUpdate,
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    skill = db.query(Skill).filter(
        Skill.id == skill_id,
        Skill.student_id == student.id
    ).first()

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    for key, value in skill_data.model_dump(exclude_unset=True).items():
        setattr(skill, key, value)

    db.commit()
    db.refresh(skill)

    return skill