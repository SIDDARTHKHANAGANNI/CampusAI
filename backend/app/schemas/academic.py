from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AcademicCreate(BaseModel):
    semester: int = Field(ge=1, le=12)

    semester_gpa: float = Field(
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

class AcademicUpdate(BaseModel):
    semester: int | None = Field(
        default=None,
        ge=1,
        le=12
    )

    semester_gpa: float | None = Field(
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
class AcademicResponse(AcademicCreate):
    id: int
    student_id: int

    model_config = ConfigDict(from_attributes=True)