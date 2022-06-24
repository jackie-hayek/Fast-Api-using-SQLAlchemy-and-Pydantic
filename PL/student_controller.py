from fastapi import APIRouter, status
from models import Student as StudentsModel
from models import *
import logging

from BLL.student_service import StudentService

router = APIRouter()

logging.basicConfig(level=logging.DEBUG)


@router.post("/student()", response_model=StudentsModel, status_code=status.HTTP_201_CREATED)
async def add_student(student: StudentsModel):
    return StudentService().add_student(student)


@router.get("/student()", response_model=list[StudentsModel], status_code=200)
async def get_students():
    return StudentService().get_students()


@router.get("/student/{id}", response_model=list[StudentsModel], status_code=status.HTTP_200_OK)
async def get_student_by_id(id: str):
    return StudentService().get_student_by_id(id)


@router.delete("/student/{id}", status_code=status.HTTP_200_OK)
async def delete_student_by_id(id: str):
    return StudentService().delete_student_by_id(id)


@router.put("/student/{id}", response_model=UpdateStudentModel, status_code=status.HTTP_200_OK)
async def update_student(id: str, studentx: UpdateStudentModel):
    return StudentService().update_student(id, studentx )
