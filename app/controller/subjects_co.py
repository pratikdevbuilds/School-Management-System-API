
from fastapi import HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.models.models import Subject,User
from app.schema.schemas import SubjectCreate, SubjectOut
 
# view all subject 
def get_subjects(db: Session,current_user:User):
    return db.query(Subject).all()

#  add subject 
def  create_subject(data:SubjectCreate,db:Session,current_user:User):
    subject = Subject(**data.model_dump())
    db.add(subject)
    db.commit()
    db.refresh(subject)
    return subject
    
# update data 
def update_subject(subject_id:int,data:SubjectCreate,db:Session,current_user:User):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    for key,value in data.model_dump().items():
        setattr(subject, key, value)
    db.commit()
    db.refresh(subject)
    return subject
    
# deleting data
def  delete_subject(subject_id,db: Session,current_user:User):
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not subject:
            raise HTTPException(status_code=404, detail="Subject not found")
    db.delete(subject)
    db.commit()
    return {"message": "Subject deleted"}
    
