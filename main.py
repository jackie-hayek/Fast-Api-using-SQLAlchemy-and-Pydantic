import uvicorn
from fastapi import Depends, FastAPI, status, HTTPException

from abstract_student_service import AbstractStudentService
from student_services import StudentService
from config import SessionLocal
from schema import student as SchemaStudent

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/student()', response_model=SchemaStudent, status_code=status.HTTP_201_CREATED)
async def add_new_student(studentx: SchemaStudent, db: SessionLocal = Depends(get_db)):
    db_students = AbstractStudentService.register(StudentService)()
    result = db_students.add_new_student(db=db, studentx=studentx)
    # if db_student:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return result


@app.get('/student()', response_model=list[SchemaStudent], status_code=200)
async def get_students(db: SessionLocal = Depends(get_db)):
    db_students = AbstractStudentService.register(StudentService)()
    result = db_students.get_students(db)
    return result


@app.get('/student/{major}', response_model=list[SchemaStudent], status_code=status.HTTP_200_OK)
async def get_student_by_major(major: str, db: SessionLocal = Depends(get_db)):
    db_student = AbstractStudentService.register(StudentService)()
    result = db_student.get_student_by_major(db, major=major)
    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return result


@app.delete('/student/{email}')
async def delete_student_by_email(email: str, db: SessionLocal = Depends(get_db)):
    student_to_delete = AbstractStudentService.register(StudentService)()
    result = student_to_delete.delete_student_by_email(db=db, email=email)
    return result


@app.put('/student/{email}', response_model=SchemaStudent, status_code=status.HTTP_200_OK)
async def update_student_by_email(studentx: SchemaStudent, email: str, db: SessionLocal = Depends(get_db)):
    student_to_update = AbstractStudentService.register(StudentService)()
    result = student_to_update.update_student_by_email(studentx=studentx, db=db, email=email)
    return result


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
