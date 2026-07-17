from typing import Optional

from pydantic import BaseModel, ConfigDict
from typing import List

from backend.app.schemas.academic import AcademicResponse
from backend.app.schemas.skill import SkillResponse
from backend.app.schemas.project import ProjectResponse
from backend.app.schemas.career_goal import CareerGoalResponse


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
    
class StudentProfileResponse(StudentResponse):
    academic_records: List[AcademicResponse] = []
    skills: List[SkillResponse] = []
    projects: List[ProjectResponse] = []
    career_goals: List[CareerGoalResponse] = []