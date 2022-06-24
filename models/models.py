import uuid
from http.client import HTTPException
from typing import Optional
from pydantic import BaseModel, validator, EmailStr
import re
from datetime import date


class Student(BaseModel):
    _id_: uuid.uuid4()
    first_name: str
    last_name: str
    enrollment_year: int
    major: str
    email: EmailStr

    @validator('email')
    def check_email_format(cls, v):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, v):
            return v
        else:
            raise HTTPException(status_code=422, detail="Invalid Email")

    @validator('enrollment_year')
    def check_enrollment_year(cls, v):
        today_date = date.today()
        current_year = int(today_date.strftime("%Y"))
        if v < current_year:
            raise HTTPException(status_code=400, detail="Invalid Enrollment Year")
        else:
            return v

    class Config:
        orm_mode = True


class UpdateStudentModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    enrollment_year: Optional[int]
    major: Optional[str]
    email: Optional[EmailStr]

    class Collection:
        name = "student"

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Abdulazeez",
                "last_name": "Abdulazeez",
                "enrollment_year": 2022,
                "major": "Water resources and environmental engineering",
                "email": "abdul@school.com"
            }
        }
