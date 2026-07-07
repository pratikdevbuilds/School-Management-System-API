from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from typing import List 
from app.db.database import get_db
from app.models.models import Announcement
from app.schema.schemas import AnnouncementCreate,AnnouncementOut
from app.controller import announcements_co

router = APIRouter()
# for get all announcements 
@router.get("/", response_model=List[AnnouncementOut],status_code=status.HTTP_200_OK)
def get_announcements(db: Session = Depends(get_db)):
    return announcements_co.get_announcements(db)

# for add announcement
@router.post("/", response_model=AnnouncementOut,status_code=status.HTTP_201_CREATED)
def create_announcement(data: AnnouncementCreate, db: Session=Depends(get_db)):
    return announcements_co.create_announcement(data,db)

# for update announcement
@router.put("/{ann_id}", response_model=AnnouncementOut,status_code=status.HTTP_201_CREATED)
def update_announcement(ann_id: int, data: AnnouncementCreate, db: Session = Depends(get_db)):
    return announcements_co. update_announcement(ann_id,data,db)

# for delete announcement
@router.delete("/{ann_id}",status_code=status.HTTP_200_OK)
def delete_announcement(ann_id: int, db: Session = Depends(get_db)):
    return announcements_co.delete_announcement(ann_id,db) 