# student chal rha tha app api and controller me  (controller/classes_co.py) and (api/classes.py) check kar lena create and update dono kar lena them subjects pr shift hona after that other 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import engine, Base
from app.api import  announcements
from app.api import student
from app.api import SchoolClass
from app.api import teachers
from app.api import subjects
from app.api import attendance





# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="School Management API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(student.router, prefix="/api/students", tags=["Students"])
app.include_router(teachers.router, prefix="/api/teachers", tags=["Teachers"])
app.include_router(SchoolClass.router, prefix="/api/classes", tags=["Classes"])
app.include_router(subjects.router, prefix="/api/subjects", tags=["Subjects"])
app.include_router(attendance.router, prefix="/api/attendance", tags=["Attendance"])
# app.include_router(exams.router, prefix="/api/exams", tags=["Exams"])
# app.include_router(fees.router, prefix="/api/fees", tags=["Fees"])
app.include_router(announcements.router, prefix="/api/announcements", tags=["Announcements"])

@app.get("/")
def root():
    return {"message": "School Management API is running"}   