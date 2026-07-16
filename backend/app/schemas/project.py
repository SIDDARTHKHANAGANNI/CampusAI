from pydantic import BaseModel, ConfigDict
from typing import Optional


class ProjectCreate(BaseModel):
    title: str
    description: Optional[str] = None
    technologies: Optional[str] = None
    github_url: Optional[str] = None


class ProjectResponse(ProjectCreate):
    id: int
    student_id: int

    model_config = ConfigDict(from_attributes=True)