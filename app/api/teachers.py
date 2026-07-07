from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import Teacher
from app.schema.schemas import TeacherCreate, TeacherOut
from app.controller import teachers_co


router = APIRouter()
# show all teacher 
@router.get("/", response_model=List[TeacherOut])
def get_teachers(db: Session = Depends(get_db)):
    return  teachers_co.get_teachers(db)

# get teacher by id 
@router.get("/{teacher_id}", response_model=TeacherOut)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return teachers_co.get_teacher(teacher_id,db)  


# add teacher 
@router.post("/", response_model=TeacherOut)
def create_teacher(data: TeacherCreate, db: Session = Depends(get_db)):
     return teachers_co.create_teacher(data,db)


#  update teacher info or detail
@router.put("/{teacher_id}", response_model=TeacherOut)
def update_teacher(teacher_id: int, data: TeacherCreate, db: Session = Depends(get_db)):
 return teachers_co.update_teacher(teacher_id,data,db)


# delete teacher 
@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
  return delete_teacher(teacher_id,db)