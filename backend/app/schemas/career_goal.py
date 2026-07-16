from pydantic import BaseModel, ConfigDict
from typing import Optional


class CareerGoalCreate(BaseModel):
    target_role: str
    target_company_type: Optional[str] = None
    target_timeline: Optional[str] = None


class CareerGoalResponse(CareerGoalCreate):
    id: int
    student_id: int

    model_config = ConfigDict(from_attributes=True)