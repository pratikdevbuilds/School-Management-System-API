from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import Student
from app.schema.schemas import StudentCreate, StudentOut


# check all student 
def get_students(db: Session):
    return db.query(Student).all()

# add student 
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    student = Student(**data.model_dump())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student