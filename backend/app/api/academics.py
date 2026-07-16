from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.student import Student
from backend.app.models.academic import AcademicRecord
from backend.app.schemas.academic import AcademicCreate, AcademicResponse


router = APIRouter(
    prefix="/students",
    tags=["Academics"]
)


@router.post(
    "/{student_id}/academics",
    response_model=AcademicResponse,
    status_code=201
)
def add_academic_record(
    student_id: int,
    academic: AcademicCreate,
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

    record = AcademicRecord(
        student_id=student_id,
        **academic.model_dump()
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record