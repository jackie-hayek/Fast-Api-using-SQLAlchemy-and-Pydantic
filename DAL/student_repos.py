from abc import ABC
from fastapi import HTTPException, status
from abstract_student_repos import AbstractStudentRepository
from models import Student as StudentsModel
from config import student_collection
from typing import List, Union

student_collection = StudentsModel


class StudentRepository(AbstractStudentRepository, ABC):
    async def get_students(self) -> List[StudentsModel]:
        response = await student_collection.all().to_list()
        if response is not None:
            result = []
            for entry in response:
                result_object = StudentsModel.from_orm(entry)
        result.append(result_object)
        return result

    async def get_student_by_id(self, id: str):
        response = await student_collection.get(id)
        if response:
            result = []
            for entry in response:
                result_object = StudentsModel.from_orm(entry)
            result.append(result_object)

        else:
            result = None

        return result

    async def add_new_student(self, studentx: StudentsModel):
        new_student = await studentx.create()
        return new_student

    async def delete_student_by_id(self, id: str) -> bool:
        student_to_delete = await student_collection.get(id)

        if student_to_delete is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")
        else:
            student_to_delete.delete()
            return True

    async def update_student_data(self, id: str, studentx: StudentsModel) -> Union[bool, StudentsModel]:
        des_body = {k: v for k, v in studentx.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        student_to_update = await student_collection.get(id)
        if student_to_update:
            await student_to_update.update(update_query)
            return student_to_update
        return False

