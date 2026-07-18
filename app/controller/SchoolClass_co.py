from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import SchoolClass, User

from app.schema.schemas import ClassCreate, ClassOut

# get all classes 
def get_classes(db: Session,current_user:User):
    return db.query(SchoolClass).all()

#  get class by id
def get_class(class_id: int, db: Session,current_user:User):
    sc = db.query(SchoolClass).filter(SchoolClass.id == class_id).first()
    if not sc:
        raise HTTPException(status_code=404, detail="Class not found")
    return sc


# add classes and details 
def create_class(data: ClassCreate, db: Session ,current_user:User):
    sc = SchoolClass(**data.model_dump())
    db.add(sc)
    db.commit()
    db.refresh(sc)
    return sc


# update and edit the info
def update_class(class_id: int, data: ClassCreate, db: Session ,current_user:User):
    sc = db.query(SchoolClass).filter(SchoolClass.id == class_id).first()
    if not sc:
        raise HTTPException(status_code=404, detail="Class not found")
    for key, value in data.model_dump().items():
        setattr(sc, key, value)
    db.commit()
    db.refresh(sc)
    return sc 

# reset and delet the classes data
def delete_class(class_id: int, db: Session ,current_user:User):
    sc = db.query(SchoolClass).filter(SchoolClass.id == class_id).first()
    if not sc:
        raise HTTPException(status_code=404, detail="Class not found")
    db.delete(sc)
    db.commit()
    return {"message": "Class deleted"}