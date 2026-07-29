from typing import List, Optional
from backend.app.schemas.academic import AcademicResponse
from backend.app.schemas.skill import SkillResponse
from backend.app.schemas.project import ProjectResponse
from backend.app.schemas.career_goal import CareerGoalResponse
from pydantic import BaseModel, ConfigDict, EmailStr, Field





class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)

    email: EmailStr

    college: str = Field(min_length=2, max_length=200)
    degree: str = Field(min_length=2, max_length=100)
    branch: str = Field(min_length=2, max_length=100)

    current_year: int = Field(ge=1, le=6)

    graduation_year: int = Field(
        ge=2020,
        le=2040
    )

    cgpa: float = Field(
        ge=0,
        le=10
    )

    attendance: Optional[float] = Field(
        default=None,
        ge=0,
        le=100
    )

    backlogs: int = Field(
        default=0,
        ge=0
    )

    target_role: str = Field(
        min_length=2,
        max_length=100
    )

class StudentUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

    college: str | None = None
    degree: str | None = None
    branch: str | None = None

    current_year: int | None = Field(
        default=None,
        ge=1,
        le=6
    )

    graduation_year: int | None = Field(
        default=None,
        ge=2020,
        le=2040
    )

    cgpa: float | None = Field(
        default=None,
        ge=0,
        le=10
    )

    attendance: float | None = Field(
        default=None,
        ge=0,
        le=100
    )

    backlogs: int | None = Field(
        default=None,
        ge=0
    )

    target_role: str | None = None
       
class StudentResponse(StudentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class StudentProfileResponse(StudentResponse):
    academic_records: List[AcademicResponse] = []
    skills: List[SkillResponse] = []
    projects: List[ProjectResponse] = []
    career_goals: List[CareerGoalResponse] = []