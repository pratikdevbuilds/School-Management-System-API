from fastapi import  Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import Exam, ExamResult
from app.schema.schemas import ExamCreate, ExamOut
 
# get exams 
def get_exams(db: Session ):
    return db.query(Exam).all()

#  add exams 
def create_exam(data: ExamCreate, db: Session ):
    exam = Exam(**data.model_dump())
    db.add(exam)
    db.commit()
    db.refresh(exam)
    return exam

#  update exams 
def update_exam(exam_id: int, data: ExamCreate, db: Session ):
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    for key, value in data.model_dump().items():
        setattr(exam, key, value)
    db.commit()
    db.refresh(exam)
    return exam

# delete exam
def delete_exam(exam_id: int, db: Session ):
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")
    db.delete(exam)
    db.commit()
    return {"message": "Exam deleted"}