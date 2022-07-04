from abc import ABC, abstractmethod, ABCMeta

from models.student_model import Student as StudentsModel


class AbstractStudentService(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_student(self, student: StudentsModel):
        raise NotImplementedError

    @abstractmethod
    def get_students(self):
        raise NotImplementedError

    @abstractmethod
    def get_student_by_id(self, student_id: str):
        raise NotImplementedError

    @abstractmethod
    def delete_student_by_id(self, student_id: str):
        raise NotImplementedError

    @abstractmethod
    def update_student(self, student_id: str, student: StudentsModel):
        raise NotImplementedError

