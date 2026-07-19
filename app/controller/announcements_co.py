from fastapi import Depends ,HTTPException
from sqlalchemy.orm import Session
from typing import List 
# from app.db.database import get_db
from app.models.models import Announcement ,User
from app.schema.schemas import AnnouncementCreate,AnnouncementOut

# get all announcement 
def get_announcements(db: Session,current_user:User):
    return db.query(Announcement).all()

# create announcement
def create_announcement(data: AnnouncementCreate, db: Session,current_user:User):
    ann = Announcement(**data.model_dump())
    db.add(ann)
    db.commit()
    db.refresh(ann)
    return ann

# UPDATE DATA
def update_announcement(ann_id: int, data: AnnouncementCreate, db: Session ,current_user:User):
    ann = db.query(Announcement).filter(Announcement.id == ann_id).first()
    if not ann:
        raise HTTPException(status_code=404, detail="Not found")
    for key, value in data.model_dump().items():
        setattr(ann, key, value)
    db.commit()
    db.refresh(ann)
    return ann
# delete announcement
def delete_announcement(ann_id: int, db: Session,current_user:User):
    ann = db.query(Announcement).filter(Announcement.id == ann_id).first()
    if not ann:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(ann)
    db.commit()
    return {"message": "Deleted"}