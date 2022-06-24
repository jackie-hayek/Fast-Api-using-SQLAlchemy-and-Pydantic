from abc import ABC
from fastapi import HTTPException, status
from DAL.abstract_student_repos import AbstractStudentRepository
from models.models import Student as StudentsModel
from config import student_collection
from typing import List, Union
from schema import studentEntity, studentsEntity


class StudentRepository(AbstractStudentRepository, ABC):
    def get_students(self) -> List[StudentsModel]:
        response = student_collection.all()
        if response is not None:
            result = []
            for entry in response:
                result_object = StudentsModel.from_orm(entry)
        result.append(result_object)
        return result

    def get_student_by_id(self, id: str):
        response = student_collection.find({"id": id})
        # if response:
        #     result = []
        #     for entry in response:
        #         result_object = StudentsModel.from_orm(entry)
        #     result.append(result_object)
        #
        # else:
        #     result = None

        return studentEntity(response)

    def add_new_student(self, studentx: StudentsModel):
        new_student = student_collection.insert_one(dict(studentx))
        return dict(new_student)

    def delete_student_by_id(self, id: str) -> bool:
        student_to_delete = student_collection.find(id)

        if student_to_delete is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")
        else:
            student_to_delete.delete()
            return True

    def update_student_data(self, id: str, studentx: StudentsModel) -> Union[bool, StudentsModel]:
        des_body = {k: v for k, v in studentx.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        student_to_update = student_collection.get(id)
        if student_to_update:
            student_to_update.update(update_query)
            return student_to_update
        return False
