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


# CREATE PROJECT
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


# GET ALL PROJECTS OF A STUDENT
@router.get(
    "/{student_id}/projects",
    response_model=list[ProjectResponse]
)
def get_projects(
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

    projects = db.query(Project).filter(
        Project.student_id == student_id
    ).all()

    return projects


# UPDATE PROJECT
@router.put(
    "/projects/{project_id}",
    response_model=ProjectResponse
)
def update_project(
    project_id: int,
    project_data: ProjectCreate,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    for key, value in project_data.model_dump().items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)

    return project


# DELETE PROJECT
@router.delete("/projects/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(
        Project.id == project_id
    ).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully"
    }