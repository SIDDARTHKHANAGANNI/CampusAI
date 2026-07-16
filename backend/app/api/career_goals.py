from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.student import Student
from backend.app.models.career_goal import CareerGoal
from backend.app.schemas.career_goal import (
    CareerGoalCreate,
    CareerGoalResponse
)


router = APIRouter(
    prefix="/students",
    tags=["Career Goals"]
)


@router.post(
    "/{student_id}/career-goal",
    response_model=CareerGoalResponse,
    status_code=201
)
def add_career_goal(
    student_id: int,
    goal: CareerGoalCreate,
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

    career_goal = CareerGoal(
        student_id=student_id,
        **goal.model_dump()
    )

    db.add(career_goal)
    db.commit()
    db.refresh(career_goal)

    return career_goal