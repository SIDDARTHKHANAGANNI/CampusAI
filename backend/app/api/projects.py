from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.student import Student
from backend.app.models.project import Project

from backend.app.core.dependencies import get_current_student
from backend.app.core.logger import logger

from backend.app.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse
)

router = APIRouter(
    prefix="/students",
    tags=["Projects"]
)


@router.get(
    "/me/projects",
    response_model=list[ProjectResponse]
)
def get_my_projects(
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    logger.info(
        f"Projects viewed. Student ID: {student.id}"
    )

    return db.query(Project).filter(
        Project.student_id == student.id
    ).all()


@router.post(
    "/me/projects",
    response_model=ProjectResponse,
    status_code=201
)
def add_my_project(
    project: ProjectCreate,
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    logger.info(
        f"Project creation attempt. Student ID: {student.id}"
    )

    new_project = Project(
        student_id=student.id,
        **project.model_dump()
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    logger.info(
        f"Project created successfully. Project ID: {new_project.id}, Student ID: {student.id}"
    )

    return new_project


@router.delete("/me/projects/{project_id}")
def delete_my_project(
    project_id: int,
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    logger.info(
        f"Project deletion attempt. Project ID: {project_id}, Student ID: {student.id}"
    )

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.student_id == student.id
    ).first()

    if not project:
        logger.warning(
            f"Project deletion failed. Project ID: {project_id} not found for Student ID: {student.id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    db.delete(project)
    db.commit()

    logger.info(
        f"Project deleted successfully. Project ID: {project_id}, Student ID: {student.id}"
    )

    return {
        "message": "Project deleted successfully"
    }


# GET ALL PROJECTS OF A STUDENT
@router.get(
    "/{student_id}/projects",
    response_model=list[ProjectResponse]
)
def get_projects(
    student_id: int,
    db: Session = Depends(get_db)
):
    logger.info(
        f"Public projects requested. Student ID: {student_id}"
    )

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        logger.warning(
            f"Public projects request failed. Student ID: {student_id} not found"
        )

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    projects = db.query(Project).filter(
        Project.student_id == student_id
    ).all()

    return projects


@router.put(
    "/me/projects/{project_id}",
    response_model=ProjectResponse
)
def update_my_project(
    project_id: int,
    project_data: ProjectUpdate,
    student: Student = Depends(get_current_student),
    db: Session = Depends(get_db)
):
    logger.info(
        f"Project update attempt. Project ID: {project_id}, Student ID: {student.id}"
    )

    project = db.query(Project).filter(
        Project.id == project_id,
        Project.student_id == student.id
    ).first()

    if not project:
        logger.warning(
            f"Project update failed. Project ID: {project_id} not found for Student ID: {student.id}"
        )

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    for key, value in project_data.model_dump(exclude_unset=True).items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)

    logger.info(
        f"Project updated successfully. Project ID: {project.id}, Student ID: {student.id}"
    )

    return project