from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.student import Student
from backend.app.models.career_goal import CareerGoal
from backend.app.models.user import User
from backend.app.core.dependencies import get_current_user
from backend.app.schemas.career_goal import CareerGoalCreate, CareerGoalResponse


router = APIRouter(
    prefix="/students",
    tags=["Career Goals"]
)

@router.get(
    "/me/career-goals",
    response_model=list[CareerGoalResponse]
)
def get_my_career_goals(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.user_id == current_user.id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
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
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.user_id == current_user.id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    new_career_goal = CareerGoal(
        student_id=student.id,
        **career_goal.model_dump()
    )

    db.add(new_career_goal)
    db.commit()
    db.refresh(new_career_goal)

    return new_career_goal

@router.delete("/me/career-goals/{career_goal_id}")
def delete_my_career_goal(
    career_goal_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.user_id == current_user.id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    career_goal = db.query(CareerGoal).filter(
        CareerGoal.id == career_goal_id,
        CareerGoal.student_id == student.id
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
    
@router.put(
    "/me/career-goals/{career_goal_id}",
    response_model=CareerGoalResponse
)
def update_my_career_goal(
    career_goal_id: int,
    career_goal_data: CareerGoalCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.user_id == current_user.id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    career_goal = db.query(CareerGoal).filter(
        CareerGoal.id == career_goal_id,
        CareerGoal.student_id == student.id
    ).first()

    if not career_goal:
        raise HTTPException(
            status_code=404,
            detail="Career goal not found"
        )

    for key, value in career_goal_data.model_dump().items():
        setattr(career_goal, key, value)

    db.commit()
    db.refresh(career_goal)

    return career_goal