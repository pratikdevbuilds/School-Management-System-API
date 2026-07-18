from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import SchoolClass
from app.schema.schemas import ClassCreate, ClassOut
from app.models.models import User
from app.core.security import require_admin,require_teacher_or_admin,require_student

from app.controller import SchoolClass_co

router = APIRouter()

# get all calsses
@router.get("/", response_model=List[ClassOut],)
def get_classes(db: Session = Depends(get_db),current_user: User = Depends(require_teacher_or_admin)):
    return SchoolClass_co.get_classes(db,current_user)


#  get class by id
@router.get("/{class_id}", response_model=ClassOut)
def get_class(class_id: int, db: Session = Depends(get_db),current_user: User = Depends(require_teacher_or_admin)):
    return SchoolClass_co.get_class(class_id,db,current_user)
   


# add class and details 
@router.post("/", response_model=ClassOut)
def create_class(data: ClassCreate, db: Session = Depends(get_db),current_user: User = Depends(require_admin)):
    return SchoolClass_co.create_class(data,db,current_user)

# update and edit data
@router.put("/{class_id}", response_model=ClassOut)
def update_class(class_id: int, data: ClassCreate, db: Session = Depends(get_db),current_user: User = Depends(require_admin)):
 return SchoolClass_co.update_class(class_id,data,db,current_user)


# delete data 
@router.delete("/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db),current_user: User = Depends(require_admin)):
 return delete_class(class_id,db,current_user)