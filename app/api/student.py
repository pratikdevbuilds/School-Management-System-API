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

#  get by id 
@router.get("/{student_id}", response_model=StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
     return student_co.get_student(student_id,db)


# add students
@router.post("/", response_model=StudentOut)
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
     return student_co.create_student(data,db) 


# update and create student 
@router.put("/{student_id}", response_model=StudentOut)
def update_student(student_id: int, data: StudentCreate, db: Session = Depends(get_db)):
     return student_co.update_student(student_id,data,db)

# delete the data
@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
   return student_co.delete_student(student_id,db)