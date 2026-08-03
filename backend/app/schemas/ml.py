from pydantic import BaseModel
from typing import List, Optional, Dict

class ResumeAnalysisRequest(BaseModel):
    resume_text: str
    target_role: Optional[str] = None

class ResumeAnalysisResponse(BaseModel):
    overall_score: float
    section_scores: Dict[str, float]
    suggestions: List[str]
    keywords_found: List[str]
    keywords_missing: List[str]

class ResumeMatchRequest(BaseModel):
    resume_text: str
    job_description: str

class ResumeMatchResponse(BaseModel):
    match_score: float
    matching_skills: List[str]
    missing_skills: List[str]
    suggestions: List[str]

class PlacementReadinessRequest(BaseModel):
    target_role: Optional[str] = None

class PlacementReadinessResponse(BaseModel):
    readiness_score: float
    confidence: str
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]

class AcademicRiskResponse(BaseModel):
    risk_score: float
    risk_level: str
    trend: str
    risk_factors: List[str]
    suggestions: List[str]

class LearningPathRequest(BaseModel):
    target_role: str
    timeline_months: Optional[int] = 6

class LearningPathStep(BaseModel):
    step: int
    topic: str
    description: str
    duration_weeks: int
    resources: List[str]

class LearningPathResponse(BaseModel):
    steps: List[LearningPathStep]

class CareerRecommendationRequest(BaseModel):
    interests: Optional[str] = None
    preferred_company_type: Optional[str] = None

class CareerRecommendationItem(BaseModel):
    role: str
    match_percentage: float
    description: str
    required_skills: List[str]
    skill_gaps: List[str]

class CareerRecommendationResponse(BaseModel):
    recommendations: List[CareerRecommendationItem]
