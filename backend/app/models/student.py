from sqlalchemy import Column, Float, Integer, String

from backend.app.database.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    college = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    branch = Column(String, nullable=False)

    current_year = Column(Integer, nullable=False)
    graduation_year = Column(Integer, nullable=False)

    cgpa = Column(Float, nullable=False)
    attendance = Column(Float, nullable=True)
    backlogs = Column(Integer, default=0)

    target_role = Column(String, nullable=False)