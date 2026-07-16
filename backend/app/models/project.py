from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from backend.app.database.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False
    )

    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    technologies = Column(Text, nullable=True)
    github_url = Column(String, nullable=True)

    student = relationship(
        "Student",
        back_populates="projects"
    )