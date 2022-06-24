from fastapi import HTTPException

from DAL.abstract_student_repos import AbstractStudentRepository
import logging

from BLL.abstract_student_service import AbstractStudentService
from models.models import Student as StudentsModel, UpdateStudentModel
from DAL.student_repos import StudentRepository


class StudentService(AbstractStudentService):

    def __init__(self):
        self.student_repository = AbstractStudentRepository.register(StudentRepository)()

    def add_student(self, student: StudentsModel):
        new_student = self.student_repository.add_new_student(student)
        logging.info('Student added to the list')
        return new_student

    def get_students(self):
        students = self.student_repository.get_students()
        logging.info('Students list returned')
        return students

    def get_student_by_id(self, id: str):
        student = self.student_repository.get_student_by_id(id)
        if not student:
            logging.error('Student with the specified id is not found')
            raise HTTPException(status_code=404, detail="Student not found")
        logging.info('Student with the specified major is returned')
        return student

    def delete_student_by_id(self, id: str):
        deleted_student = self.student_repository.delete_student_by_id(id)
        if not deleted_student:
            logging.error('Student not found')
            raise HTTPException(status_code=404, detail="Student not found")
        logging.info('Student deleted')
        return deleted_student

    def update_student(self, id: str, student: UpdateStudentModel):
        updated_student = self.student_repository.update_student_data(id, student)
        if not updated_student:
            logging.error('Student not found')
            raise HTTPException(status_code=404, detail="Student not found")
        logging.info('Student data updated')
        return updated_student
