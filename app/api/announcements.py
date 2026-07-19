from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from typing import List 
from app.db.database import get_db
from app.models.models import Announcement,User
from app.schema.schemas import AnnouncementCreate,AnnouncementOut
from app.controller import announcements_co
from app.core.security import require_admin,require_student,require_teacher_or_admin ,get_current_user
router = APIRouter()
# for get all announcements 
@router.get("/", response_model=List[AnnouncementOut],status_code=status.HTTP_200_OK)
def get_announcements(db: Session = Depends(get_db) ,current_user:User =Depends(get_current_user)):
    return announcements_co.get_announcements(db,current_user)

# for add announcement
@router.post("/", response_model=AnnouncementOut,status_code=status.HTTP_201_CREATED)
def create_announcement(data: AnnouncementCreate, db: Session=Depends(get_db),current_user:User =Depends(require_teacher_or_admin)):
    return announcements_co.create_announcement(data,db,current_user)

# for update announcement
@router.put("/{ann_id}", response_model=AnnouncementOut,status_code=status.HTTP_201_CREATED)
def update_announcement(ann_id: int, data: AnnouncementCreate, db: Session = Depends(get_db) ,current_user:User =Depends(require_teacher_or_admin)):
    return announcements_co. update_announcement(ann_id,data,db,current_user)

# for delete announcement
@router.delete("/{ann_id}",status_code=status.HTTP_200_OK)
def delete_announcement(ann_id: int, db: Session = Depends(get_db),current_user:User =Depends(require_admin)):
    return announcements_co.delete_announcement(ann_id,db,current_user) 