from abc import ABC, abstractmethod, ABCMeta

from models.models import Student as StudentsModel, UpdateStudentModel


class AbstractStudentService(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_student(self, student: StudentsModel):
        raise NotImplementedError

    @abstractmethod
    def get_students(self):
        raise NotImplementedError

    @abstractmethod
    def get_student_by_id(self, id: str):
        raise NotImplementedError

    @abstractmethod
    def delete_student_by_id(self, id: str):
        raise NotImplementedError

    @abstractmethod
    def update_student(self, id: str, student: UpdateStudentModel):
        raise NotImplementedError

