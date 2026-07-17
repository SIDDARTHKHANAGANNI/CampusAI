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


# CREATE CAREER GOAL
@router.post(
    "/{student_id}/career-goals",
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


# GET ALL CAREER GOALS OF A STUDENT
@router.get(
    "/{student_id}/career-goals",
    response_model=list[CareerGoalResponse]
)
def get_career_goals(
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

    career_goals = db.query(CareerGoal).filter(
        CareerGoal.student_id == student_id
    ).all()

    return career_goals


# UPDATE CAREER GOAL
@router.put(
    "/career-goals/{goal_id}",
    response_model=CareerGoalResponse
)
def update_career_goal(
    goal_id: int,
    goal_data: CareerGoalCreate,
    db: Session = Depends(get_db)
):
    career_goal = db.query(CareerGoal).filter(
        CareerGoal.id == goal_id
    ).first()

    if not career_goal:
        raise HTTPException(
            status_code=404,
            detail="Career goal not found"
        )

    for key, value in goal_data.model_dump().items():
        setattr(career_goal, key, value)

    db.commit()
    db.refresh(career_goal)

    return career_goal


# DELETE CAREER GOAL
@router.delete("/career-goals/{goal_id}")
def delete_career_goal(
    goal_id: int,
    db: Session = Depends(get_db)
):
    career_goal = db.query(CareerGoal).filter(
        CareerGoal.id == goal_id
    ).first()

    if not career_goal:
        raise HTTPException(
            status_code=404,
            detail="Career goal not found"
        )

    db.delete(career_goal)
    db.commit()

    return {
        "message": "Career goal deleted successfully"
    }