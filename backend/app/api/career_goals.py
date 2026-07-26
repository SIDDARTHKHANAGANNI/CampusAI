from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.student import Student
from backend.app.models.career_goal import CareerGoal

from backend.app.core.dependencies import get_current_student
from backend.app.core.logger import logger

from backend.app.schemas.career_goal import (
    CareerGoalCreate,
    CareerGoalUpdate,
    CareerGoalResponse
)

router = APIRouter(
    prefix="/students",
    tags=["Career Goals"]
)


@router.get(
    "/me/career-goals",
    response_model=list[CareerGoalResponse]
)
def get_my_career_goals(
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    logger.info(
        f"Career goals viewed. Student ID: {student.id}"
    )

    return db.query(CareerGoal).filter(
        CareerGoal.student_id == student.id
    ).all()


@router.post(
    "/me/career-goals",
    response_model=CareerGoalResponse,
    status_code=201
)
def add_my_career_goal(
    career_goal: CareerGoalCreate,
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    logger.info(
        f"Career goal creation attempt. Student ID: {student.id}"
    )

    new_career_goal = CareerGoal(
        student_id=student.id,
        **career_goal.model_dump()
    )

    db.add(new_career_goal)
    db.commit()
    db.refresh(new_career_goal)

    logger.info(
        f"Career goal created successfully. Career Goal ID: {new_career_goal.id}, Student ID: {student.id}"
    )

    return new_career_goal


@router.delete("/me/career-goals/{career_goal_id}")
def delete_my_career_goal(
    career_goal_id: int,
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    logger.info(
        f"Career goal deletion attempt. Career Goal ID: {career_goal_id}, Student ID: {student.id}"
    )

    career_goal = db.query(CareerGoal).filter(
        CareerGoal.id == career_goal_id,
        CareerGoal.student_id == student.id
    ).first()

    if not career_goal:
        logger.warning(
            f"Career goal deletion failed. Career Goal ID: {career_goal_id} not found for Student ID: {student.id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Career goal not found"
        )

    db.delete(career_goal)
    db.commit()

    logger.info(
        f"Career goal deleted successfully. Career Goal ID: {career_goal_id}, Student ID: {student.id}"
    )

    return {
        "message": "Career goal deleted successfully"
    }


# GET ALL CAREER GOALS OF A STUDENT
@router.get(
    "/{student_id}/career-goals",
    response_model=list[CareerGoalResponse]
)
def get_career_goals(
    student_id: int,
    db: Session = Depends(get_db)
):
    logger.info(
        f"Public career goals requested. Student ID: {student_id}"
    )

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        logger.warning(
            f"Public career goals request failed. Student ID: {student_id} not found"
        )

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    career_goals = db.query(CareerGoal).filter(
        CareerGoal.student_id == student_id
    ).all()

    return career_goals


@router.put(
    "/me/career-goals/{career_goal_id}",
    response_model=CareerGoalResponse
)
def update_my_career_goal(
    career_goal_id: int,
    career_goal_data: CareerGoalUpdate,
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    logger.info(
        f"Career goal update attempt. Career Goal ID: {career_goal_id}, Student ID: {student.id}"
    )

    career_goal = db.query(CareerGoal).filter(
        CareerGoal.id == career_goal_id,
        CareerGoal.student_id == student.id
    ).first()

    if not career_goal:
        logger.warning(
            f"Career goal update failed. Career Goal ID: {career_goal_id} not found for Student ID: {student.id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Career goal not found"
        )

    for key, value in career_goal_data.model_dump(exclude_unset=True).items():
        setattr(career_goal, key, value)

    db.commit()
    db.refresh(career_goal)

    logger.info(
        f"Career goal updated successfully. Career Goal ID: {career_goal.id}, Student ID: {student.id}"
    )

    return career_goal