from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.database.database import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False
    )

    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    proficiency = Column(String, nullable=False)

    student = relationship(
        "Student",
        back_populates="skills"
    )