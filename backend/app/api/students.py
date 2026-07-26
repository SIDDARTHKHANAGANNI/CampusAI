from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.models.user import User
from backend.app.database.database import get_db
from backend.app.models.student import Student

from backend.app.core.dependencies import (
    get_current_user,
    get_current_student
)

from backend.app.core.logger import logger

from backend.app.schemas.student import (
    StudentCreate,
    StudentUpdate,
    StudentResponse,
    StudentProfileResponse
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get(
    "/me/profile",
    response_model=StudentProfileResponse
)
def get_my_profile(
    student: Student = Depends(get_current_student)
):
    logger.info(
        f"Student profile viewed. Student ID: {student.id}"
    )

    return student


@router.post(
    "/me/profile",
    response_model=StudentResponse,
    status_code=201
)
def create_my_profile(
    student_data: StudentUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    logger.info(
        f"Profile creation attempt. User ID: {current_user.id}"
    )

    existing_profile = db.query(Student).filter(
        Student.user_id == current_user.id
    ).first()

    if existing_profile:
        logger.warning(
            f"Profile creation failed. Profile already exists for User ID: {current_user.id}"
        )

        raise HTTPException(
            status_code=400,
            detail="Student profile already exists"
        )

    new_student = Student(
        user_id=current_user.id,
        **student_data.model_dump()
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    logger.info(
        f"Student profile created successfully. Student ID: {new_student.id}"
    )

    return new_student


@router.put(
    "/me/profile",
    response_model=StudentResponse
)
def update_my_profile(
    student_data: StudentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    logger.info(
        f"Profile update attempt. User ID: {current_user.id}"
    )

    student = db.query(Student).filter(
        Student.user_id == current_user.id
    ).first()

    if not student:
        logger.warning(
            f"Profile update failed. Student profile not found for User ID: {current_user.id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Student profile not found"
        )

    for key, value in student_data.model_dump(exclude_unset=True).items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    logger.info(
        f"Student profile updated successfully. Student ID: {student.id}"
    )

    return student


@router.get(
    "/{student_id}/profile",
    response_model=StudentProfileResponse
)
def get_student_profile(
    student_id: int,
    db: Session = Depends(get_db)
):
    logger.info(
        f"Public profile requested. Student ID: {student_id}"
    )

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:
        logger.warning(
            f"Public profile not found. Student ID: {student_id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student