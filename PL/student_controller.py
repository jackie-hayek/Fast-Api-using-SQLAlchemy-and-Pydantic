from fastapi import APIRouter, status

from BLL.abstract_student_service import AbstractStudentService
from models.student_model import Student as StudentsModel, UpdateStudentModel
import logging

from BLL.student_service import StudentService

router = APIRouter()

logging.basicConfig(level=logging.DEBUG)

student_service = AbstractStudentService.register(StudentService)()


@router.post("/student()", response_model=StudentsModel, status_code=status.HTTP_201_CREATED)
async def add_student(student: StudentsModel):
    return await student_service.add_student(student)


@router.get("/student()", response_model=list[StudentsModel], status_code=200)
async def get_students():
    return await student_service.get_students()


@router.get("/student/{student_id}", status_code=status.HTTP_200_OK)
async def get_student_by_id(student_id: str):
    return await student_service.get_student_by_id(student_id)


@router.delete("/student/{student_id}", status_code=status.HTTP_200_OK)
async def delete_student_by_id(student_id: str):
    return await student_service.delete_student_by_id(student_id)


@router.put("/student/{student_id}", response_model=UpdateStudentModel, status_code=status.HTTP_200_OK)
async def update_student(student_id: str, studentx: UpdateStudentModel):
    return await student_service.update_student(student_id, studentx.dict())
