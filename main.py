import uvicorn
from fastapi import FastAPI
from PL.student_controller import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Students"], prefix="/student")

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)

