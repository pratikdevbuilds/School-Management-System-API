from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import Teacher
from app.schema.schemas import TeacherCreate, TeacherOut


# get all teachers 
def get_teachers(db: Session = Depends(get_db)):
    return db.query(Teacher).all()

# add teachers and details 
def create_teacher(data: TeacherCreate, db: Session):
    teacher = Teacher(**data.model_dump())
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher  