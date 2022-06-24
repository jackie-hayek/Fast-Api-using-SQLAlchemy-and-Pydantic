from abc import ABC, abstractmethod, ABCMeta
from models import Student as StudentsModel


class AbstractStudentRepository(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_students(self):
        raise NotImplementedError

    @abstractmethod
    def get_student_by_id(self, id: str):
        raise NotImplementedError

    @abstractmethod
    async def add_new_student(self, studentx: StudentsModel):
        raise NotImplementedError

    @abstractmethod
    def delete_student_by_id(self, id: str):
        raise NotImplementedError

    @abstractmethod
    def update_student_data(self, id: str, studentx: StudentsModel):
        raise NotImplementedError
