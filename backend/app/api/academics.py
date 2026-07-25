from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.student import Student
from backend.app.models.academic import AcademicRecord
from backend.app.core.dependencies import (
    get_current_user,
    get_current_student
)

from backend.app.schemas.academic import (
    AcademicCreate,
    AcademicUpdate,
    AcademicResponse
)

router = APIRouter(
    prefix="/students",
    tags=["Academics"]
)


@router.get(
    "/me/academics",
    response_model=list[AcademicResponse]
)
def get_my_academics(
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    return db.query(AcademicRecord).filter(
        AcademicRecord.student_id == student.id
    ).all()


@router.post(
    "/me/academics",
    response_model=AcademicResponse,
    status_code=201
)
def add_my_academic(
    academic: AcademicCreate,
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    new_academic = AcademicRecord(
        student_id=student.id,
        **academic.model_dump()
    )

    db.add(new_academic)
    db.commit()
    db.refresh(new_academic)

    return new_academic


@router.delete("/me/academics/{academic_id}")
def delete_my_academic(
    academic_id: int,
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    academic = db.query(AcademicRecord).filter(
        AcademicRecord.id == academic_id,
        AcademicRecord.student_id == student.id
    ).first()

    if not academic:
        raise HTTPException(
            status_code=404,
            detail="Academic record not found"
        )

    db.delete(academic)
    db.commit()

    return {
        "message": "Academic record deleted successfully"
    }


@router.get(
    "/{student_id}/academics",
    response_model=list[AcademicResponse]
)
def get_academic_records(
    student_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(AcademicRecord)
        .filter(AcademicRecord.student_id == student_id)
        .all()
    )


@router.put(
    "/me/academics/{academic_id}",
    response_model=AcademicResponse
)
def update_my_academic(
    academic_id: int,
    academic_data: AcademicUpdate,
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    record = db.query(AcademicRecord).filter(
        AcademicRecord.id == academic_id,
        AcademicRecord.student_id == student.id
    ).first()

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Academic record not found"
        )

    for key, value in academic_data.model_dump(exclude_unset=True).items():
        setattr(record, key, value)

    db.commit()
    db.refresh(record)

    return record