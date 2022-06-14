import uvicorn
from fastapi import Depends, FastAPI, status, HTTPException

import services
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
    db_student = services.add_new_student(db, studentx)
    # if db_student:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return db_student


@app.get('/student()', response_model=list[SchemaStudent], status_code=200)
async def get_students(db: SessionLocal = Depends(get_db)):
    db_students = services.get_students(db)
    return db_students


@app.get('/student/{major}', response_model=list[SchemaStudent], status_code=status.HTTP_200_OK)
async def get_student_by_major(major: str, db: SessionLocal = Depends(get_db)):
    db_student = services.get_student_by_major(db, major=major)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.delete('/student/{email}')
async def delete_student_by_email(email: str, db: SessionLocal = Depends(get_db)):
    student_to_delete = services.delete_student_by_email(db, email=email)
    return student_to_delete


@app.put('/student/{email}', response_model=SchemaStudent, status_code=status.HTTP_200_OK)
async def update_student_by_email(studentx: SchemaStudent, email: str, db: SessionLocal = Depends(get_db)):
    student_to_update = services.update_student_by_email(studentx=studentx, db=db, email=email)
    return student_to_update


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
