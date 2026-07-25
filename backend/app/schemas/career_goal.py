from typing import Optional

from pydantic import BaseModel, ConfigDict


class CareerGoalCreate(BaseModel):
    target_role: str
    target_company_type: Optional[str] = None
    target_timeline: Optional[str] = None


class CareerGoalUpdate(BaseModel):
    target_role: str | None = None
    target_company_type: str | None = None
    target_timeline: str | None = None


class CareerGoalResponse(CareerGoalCreate):
    id: int
    student_id: int

    model_config = ConfigDict(from_attributes=True)