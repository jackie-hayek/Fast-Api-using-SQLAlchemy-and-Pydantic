from dependency_injector import containers, providers

from BLL.abstract_student_service import AbstractStudentService
from BLL.student_service import StudentService
from DAL.abstract_student_repository import AbstractStudentRepository
from DAL.student_repository import StudentRepository


class Container(containers.DeclarativeContainer):
    student_repository = providers.Factory(AbstractStudentRepository.register(StudentRepository))
    student_service = providers.Factory(
        AbstractStudentService.register(StudentService), student_repository=student_repository)
