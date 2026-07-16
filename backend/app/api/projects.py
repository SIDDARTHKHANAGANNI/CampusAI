from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.student import Student
from backend.app.models.project import Project
from backend.app.schemas.project import ProjectCreate, ProjectResponse


router = APIRouter(
    prefix="/students",
    tags=["Projects"]
)


@router.post(
    "/{student_id}/projects",
    response_model=ProjectResponse,
    status_code=201
)
def add_project(
    student_id: int,
    project: ProjectCreate,
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

    new_project = Project(
        student_id=student_id,
        **project.model_dump()
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project