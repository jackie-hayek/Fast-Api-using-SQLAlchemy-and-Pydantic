from datetime import datetime
from http.client import HTTPException
from typing import List
from pydantic import BaseModel, validator
import re


class student(BaseModel):
    first_name: str
    last_name: str
    enrollment_year: int
    major: str
    email: str

    @validator('email')
    def check_email_format(cls, v):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, v):
            return v
        else:
            raise HTTPException(status_code=422, detail="Email Validation Error")

    @validator('enrollment_year')
    def check_enrollment_year(cls, v):
        if v < 2022:
            raise HTTPException(status_code=400, detail="Invalid Enrollment Year")
        else:
            return v

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
