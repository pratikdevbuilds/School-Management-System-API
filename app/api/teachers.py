from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import Teacher,User
from app.schema.schemas import TeacherCreate, TeacherOut
from app.controller import teachers_co
from app.core.security import require_teacher_or_admin,require_admin


router = APIRouter()
# show all teacher 
@router.get("/", response_model=List[TeacherOut])
def get_teachers(db: Session = Depends(get_db),current_user: User = Depends(require_teacher_or_admin)):
    return  teachers_co.get_teachers(db,current_user)

# get teacher by id 
@router.get("/{teacher_id}", response_model=TeacherOut)
def get_teacher(teacher_id: int, db: Session = Depends(get_db),current_user: User = Depends(require_admin)):
    return teachers_co.get_teacher(teacher_id,db,current_user)  


# add teacher 
@router.post("/", response_model=TeacherOut)
def create_teacher(data: TeacherCreate, db: Session = Depends(get_db),current_user: User = Depends(require_admin)):
     return teachers_co.create_teacher(data,db,current_user)


#  update teacher info or detail
@router.put("/{teacher_id}", response_model=TeacherOut)
def update_teacher(teacher_id: int, data: TeacherCreate, db: Session = Depends(get_db),current_user: User = Depends(require_teacher_or_admin)):
 return teachers_co.update_teacher(teacher_id,data,db,current_user)


# delete teacher 
@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db),current_user: User = Depends(require_admin)):
  return delete_teacher(teacher_id,db,current_user)