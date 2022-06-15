from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from abstract_student_service import AbstractStudentService
from schema import student as SchemaStudent
from models import student as ModelStudent


class StudentService(AbstractStudentService):
    def get_students(self, db: Session, **kwargs):
        response = db.query(ModelStudent).all()
        if response is not None:
            result = []
            for entry in response:
                result_object = SchemaStudent.from_orm(entry)
        result.append(result_object)
        return result

    def get_student_by_major(self, db: Session, major: str):
        response = db.query(ModelStudent).filter(ModelStudent.major == major).all()
        if response is not None:
            result = []
            for entry in response:
                result_object = SchemaStudent.from_orm(entry)
        result.append(result_object)
        return result

    def add_new_student(self, db: Session, studentx: SchemaStudent) -> object:
        db_student = db.query(ModelStudent).filter(ModelStudent.email == studentx.email).first()

        if db_student is not None:
            raise HTTPException(status_code=400, detail="Student already exists")

        new_student = ModelStudent(
            first_name=studentx.first_name,
            last_name=studentx.last_name,
            enrollment_year=studentx.enrollment_year,
            email=studentx.email,
            major=studentx.major
        )

        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student

    def delete_student_by_email(self, db: Session, email: str):
        student_to_delete = db.query(ModelStudent).filter(ModelStudent.email == email).first()

        if student_to_delete is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

        db.delete(student_to_delete)
        db.commit()
        db.refresh(student_to_delete)
        return student_to_delete

    def update_student_by_email(self, db: Session, email: str, studentx: SchemaStudent):
        student_to_update = db.query(ModelStudent).filter(ModelStudent.email == email).first()
        student_to_update.first_name = studentx.first_name
        student_to_update.last_name = studentx.last_name
        student_to_update.enrollment_year = studentx.enrollment_year
        student_to_update.major = studentx.major

        db.commit()
        db.refresh(student_to_update)
        return student_to_update
