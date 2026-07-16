from fastapi import APIRouter
from backend.app.schemas.student import StudentCreate

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post("/")
def create_student(student: StudentCreate):
    return {
        "message": "Student profile created successfully",
        "student": student
    }