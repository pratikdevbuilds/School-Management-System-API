from fastapi import APIRouter,  HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.models import Student
from app.schema.schemas import StudentCreate, StudentOut
from app.models.models import User
 
 
# check all student 
def get_students(db: Session,current_user:User):
    return db.query(Student).all()

#  get by id 
def get_student(student_id: int, db: Session,current_user:User):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student



# add student 
def create_student(data: StudentCreate, db: Session ,current_user:User):
    student = Student(**data.model_dump())
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


# update and changes 
def update_student(student_id: int, data: StudentCreate, db: Session,current_user:User):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in data.model_dump().items():
        setattr(student, key, value)
    db.commit()
    db.refresh(student)
    return student

# delete Student
def delete_student(student_id: int, db: Session,current_user:User):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted"}