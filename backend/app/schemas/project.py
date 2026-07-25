from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProjectCreate(BaseModel):
    title: str
    description: Optional[str] = None
    technologies: Optional[str] = None
    github_url: Optional[str] = None


class ProjectUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    technologies: str | None = None
    github_url: str | None = None


class ProjectResponse(ProjectCreate):
    id: int
    student_id: int

    model_config = ConfigDict(from_attributes=True)