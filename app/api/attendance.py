from fastapi import APIRouter, Depends, Query,status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from app.db.database import get_db
from app.models.models import Attendance,User
from app.schema.schemas import AttendanceCreate, AttendanceOut
from app.controller import attendance_co
from app.core.security import require_admin,require_student,require_teacher_or_admin,get_current_user

router = APIRouter()

# get attendances
@router.get("/", response_model=List[AttendanceOut],status_code=status.HTTP_200_OK)
def get_attendance(
    date_filter: Optional[date] = Query(None, alias="date"),
    class_id: Optional[int] = None,
    student_id: Optional[int] = None,
    db: Session = Depends(get_db),current_user: User = Depends(get_current_user)): 
    return attendance_co.get_attendance(date_filter,class_id,student_id,db)


#  add aatendance 
@router.post("/", response_model=AttendanceOut)
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db),current_user: User = Depends(require_teacher_or_admin)):
         return  attendance_co.mark_attendance(data,db,current_user)


# update attendance 
@router.put("/{attendance_id}", response_model=AttendanceOut)
def update_attendance(attendance_id: int, data: AttendanceCreate, db: Session = Depends(get_db),current_user: User = Depends(require_teacher_or_admin)):
    return attendance_co.update_attendance(attendance_id,data,db,current_user)