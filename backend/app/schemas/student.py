from typing import Optional

from pydantic import BaseModel, ConfigDict


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

    model_config = ConfigDict(from_attributes=True)