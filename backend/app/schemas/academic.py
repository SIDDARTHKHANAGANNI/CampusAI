from pydantic import BaseModel, ConfigDict
from typing import Optional


class AcademicCreate(BaseModel):
    semester: int
    semester_gpa: float
    attendance: Optional[float] = None
    backlogs: int = 0


class AcademicResponse(AcademicCreate):
    id: int
    student_id: int

    model_config = ConfigDict(from_attributes=True)