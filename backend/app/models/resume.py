from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from backend.app.database.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    target_role = Column(String, nullable=False)
    raw_text = Column(Text)
    score = Column(Float)
    ats_score = Column(Float)
    extracted_skills = Column(Text)
    missing_skills = Column(Text)
    suggestions = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)