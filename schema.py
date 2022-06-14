from datetime import datetime
from typing import List
from pydantic import BaseModel


class student(BaseModel):
    first_name: str
    last_name: str
    enrollment_year: int
    major: str
    email: str

    class Config:
        orm_mode = True


class course(BaseModel):
    instructor: str
    course_nb: str
    instruction_days: List[str]
    # start_time: datetime
    # end_time:
    capacity: int
    nb_enrolled: int

    class Config:
        orm_mode = True


class enrollment(BaseModel):
    course_id: int
    student_id: int

    class Config:
        orm_mode = True
