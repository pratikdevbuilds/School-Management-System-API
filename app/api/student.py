from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import Student
from app.schema.schemas import StudentCreate, StudentOut
from app.controller import student_co
router = APIRouter()


# get all students
@router.get("/", response_model=List[StudentOut])
def get_students(db: Session = Depends(get_db)):
    return student_co.get_students(db)


@router.post("/", response_model=StudentOut)
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
     return student_co.create_student(data,db) 