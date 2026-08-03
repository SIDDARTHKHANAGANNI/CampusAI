from pydantic import BaseModel
from typing import List, Dict


class ResumeAnalysisResponse(BaseModel):
    score: float
    ats_score: float
    extracted_skills: List[str]
    missing_skills: List[str]
    sections_detected: Dict[str, bool]
    suggestions: List[str]