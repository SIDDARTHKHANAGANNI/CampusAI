from pydantic import BaseModel, ConfigDict
from typing import Optional


class SkillCreate(BaseModel):
    name: str
    category: Optional[str] = None
    proficiency: str


class SkillResponse(SkillCreate):
    id: int
    student_id: int

    model_config = ConfigDict(from_attributes=True)