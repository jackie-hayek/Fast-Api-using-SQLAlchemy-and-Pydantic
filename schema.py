import uuid
from models.models import Student


def studentEntity(Student) -> dict:
    return {
        "student_id": str(uuid.uuid4()),
        "first_name": Student["first_name"],
        "last_name": Student["last_name"],
        "enrollment_year": Student["enrollment_year"],
        "major": Student["major"]
    }


def studentsEntity(entity) -> list:
    return [studentEntity(Student) for Student in entity]
