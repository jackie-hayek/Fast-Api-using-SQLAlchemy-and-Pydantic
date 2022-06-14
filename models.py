# SQLAlchemy models
from sqlalchemy import Column, String, Integer, Date, ARRAY, ForeignKey

import config as db


class course(db.base):
    __tablename__ = "course"
    courses_id = Column(Integer, primary_key=True, index=True)
    instructor = Column(String)
    course_nb = Column(String, unique=True)
    instruction_days = Column(ARRAY(String))
    start_time = Column(Date)
    end_time = Column(Date)
    capacity = Column(Integer)
    nb_enrolled = Column(Integer)


class student(db.base):
    __tablename__ = "student"
    student_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    enrollment_year = Column(Integer)
    major = Column(String)
    email = Column(String, unique=True)


class enrollment(db.base):
    __tablename__ = "enrollment"
    student_id = Column(Integer, ForeignKey("students.student_id"))
    courses_id = Column(Integer, ForeignKey("courses.courses_id"))
    id = Column(Integer, primary_key=True, index=True)
