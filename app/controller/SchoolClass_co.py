from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import SchoolClass
from app.schema.schemas import ClassCreate, ClassOut


# get all classes 
def get_classes(db: Session):
    return db.query(SchoolClass).all()

# add classes and details 
def create_class(data: ClassCreate, db: Session ):
    sc = SchoolClass(**data.model_dump())
    db.add(sc)
    db.commit()
    db.refresh(sc)
    return sc
