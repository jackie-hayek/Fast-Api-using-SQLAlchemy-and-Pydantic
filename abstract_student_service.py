from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from schema import student as SchemaStudent


class AbstractStudentService(ABC):
    @abstractmethod
    def get_students(self, db: Session):
        raise NotImplementedError

    @abstractmethod
    def get_student_by_major(self, db: Session, major: str):
        raise NotImplementedError

    @abstractmethod
    def add_new_student(self, db: Session, studentx: SchemaStudent) -> object:
        raise NotImplementedError

    @abstractmethod
    def delete_student_by_email(self, db: Session, email: str):
        raise NotImplementedError

    @abstractmethod
    def update_student_by_email(self, db: Session, email: str, studentx: SchemaStudent):
        raise NotImplementedError
