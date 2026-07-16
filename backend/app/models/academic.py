from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.database.database import Base


class AcademicRecord(Base):
    __tablename__ = "academic_records"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False
    )

    semester = Column(Integer, nullable=False)
    semester_gpa = Column(Float, nullable=False)
    attendance = Column(Float, nullable=True)
    backlogs = Column(Integer, default=0)

    student = relationship(
        "Student",
        back_populates="academic_records"
    )