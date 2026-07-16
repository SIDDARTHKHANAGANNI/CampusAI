from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.database.database import Base


class CareerGoal(Base):
    __tablename__ = "career_goals"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False
    )

    target_role = Column(String, nullable=False)
    target_company_type = Column(String, nullable=True)
    target_timeline = Column(String, nullable=True)

    student = relationship(
    "Student",
    back_populates="career_goals"
)