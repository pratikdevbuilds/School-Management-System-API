from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import Teacher
from app.schema.schemas import TeacherCreate, TeacherOut
from app.controller import teachers_co


router = APIRouter()

@router.get("/", response_model=List[TeacherOut])
def get_teachers(db: Session = Depends(get_db)):
    return  teachers_co.get_teachers(db)


@router.post("/", response_model=TeacherOut)
def create_teacher(data: TeacherCreate, db: Session = Depends(get_db)):
     return teachers_co.create_teacher(data,db)