from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import Exam, ExamResult
from app.schema.schemas import ExamCreate, ExamOut
from app.controller import exams_co

router = APIRouter()
# get  exams details 
@router.get("/", response_model=List[ExamOut])
def get_exams(db: Session = Depends(get_db)):
    return exams_co.get_exams(db)

# add exam  
@router.post("/", response_model=ExamOut)
def create_exam(data: ExamCreate, db: Session = Depends(get_db)):
    return exams_co.create_exam(data,db)

# update exams 
@router.put("/{exam_id}", response_model=ExamOut)
def update_exam(exam_id: int, data: ExamCreate, db: Session = Depends(get_db)):
    return exams_co. update_exam(exam_id,data,db)


# delete data
@router.delete("/{exam_id}")
def delete_exam(exam_id: int, db: Session = Depends(get_db)):
   return exams_co.delete_exam(exam_id,db)