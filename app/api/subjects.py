from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import Subject
from app.schema.schemas import SubjectCreate, SubjectOut
from app.controller import subjects_co

router = APIRouter()
# get all subjects
@router.get("/", response_model=List[SubjectOut])
def get_subjects(db: Session = Depends(get_db)):
    return subjects_co.get_subjects(db)

# for add students
@router.post("/",response_model=List[SubjectOut])
def create_subject(data:SubjectCreate,db: Session = Depends(get_db)):
    return subjects_co. create_subject(data,db)

# updates student details or info 
@router.put("/{subject_id}", response_model=SubjectOut)
def update_subject(subject_id:int,data:SubjectCreate,db: Session = Depends(get_db)):
    return subjects_co .update_subject
   
#  for deleting sudent 

@router.delete("/{subject_id}")
def delete_subject(subject_id: int, db: Session = Depends(get_db)):
  return subjects_co.delete_subject(subject_id,db)

