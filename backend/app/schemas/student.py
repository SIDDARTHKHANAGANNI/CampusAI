from pydantic import BaseModel
from typing import Optional


class StudentCreate(BaseModel):
    name: str
    email: str
    college: str
    degree: str
    branch: str
    current_year: int
    graduation_year: int
    cgpa: float
    attendance: Optional[float] = None
    backlogs: int = 0
    target_role: str


class StudentResponse(StudentCreate):
    id: int