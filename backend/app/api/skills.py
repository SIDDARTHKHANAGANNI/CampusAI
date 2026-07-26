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
from backend.app.core.logger import logger

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
    logger.info(
        f"Skills viewed. Student ID: {student.id}"
    )

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
    logger.info(
        f"Skill creation attempt. Student ID: {student.id}"
    )

    new_skill = Skill(
        student_id=student.id,
        **skill.model_dump()
    )

    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)

    logger.info(
        f"Skill created successfully. Skill ID: {new_skill.id}, Student ID: {student.id}"
    )

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
    logger.info(
        f"Public skills requested. Student ID: {student_id}"
    )

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        logger.warning(
            f"Public skills request failed. Student ID: {student_id} not found"
        )

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
    logger.info(
        f"Skill update attempt. Skill ID: {skill_id}, Student ID: {student.id}"
    )

    skill = db.query(Skill).filter(
        Skill.id == skill_id,
        Skill.student_id == student.id
    ).first()

    if not skill:
        logger.warning(
            f"Skill update failed. Skill ID: {skill_id} not found for Student ID: {student.id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    for key, value in skill_data.model_dump(exclude_unset=True).items():
        setattr(skill, key, value)

    db.commit()
    db.refresh(skill)

    logger.info(
        f"Skill updated successfully. Skill ID: {skill.id}, Student ID: {student.id}"
    )

    return skill