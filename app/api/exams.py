from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import Exam, ExamResult,User
from app.schema.schemas import ExamCreate, ExamOut
from app.controller import exams_co
from app.core.security import require_admin,require_student,require_teacher_or_admin

router = APIRouter()
# get  exams details 
@router.get("/", response_model=List[ExamOut])
def get_exams(db: Session = Depends(get_db),current_user: User = Depends(require_student)):
    return exams_co.get_exams(db,current_user)

# add exam  
@router.post("/", response_model=ExamOut)
def create_exam(data: ExamCreate, db: Session = Depends(get_db),current_user: User = Depends(require_teacher_or_admin)):
    return exams_co.create_exam(data,db,current_user)

# update exams 
@router.put("/{exam_id}", response_model=ExamOut)
def update_exam(exam_id: int, data: ExamCreate, db: Session = Depends(get_db),current_user: User = Depends(require_teacher_or_admin)):
    return exams_co. update_exam(exam_id,data,db,current_user)


# delete data
@router.delete("/{exam_id}")
def delete_exam(exam_id: int, db: Session = Depends(get_db),current_user: User = Depends(require_admin)):
   return exams_co.delete_exam(exam_id,db,current_user)