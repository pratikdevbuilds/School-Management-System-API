from fastapi import APIRouter, Depends, Query,status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from app.db.database import get_db
from app.models.models import Attendance
from app.schema.schemas import AttendanceCreate, AttendanceOut
from app.controller import attendance_co

router = APIRouter()

# get attendances
@router.get("/", response_model=List[AttendanceOut],status_code=status.HTTP_200_OK)
def get_attendance(
    date_filter: Optional[date] = Query(None, alias="date"),
    class_id: Optional[int] = None,
    student_id: Optional[int] = None,
    db: Session = Depends(get_db)): 
    return attendance_co.get_attendance(date_filter,class_id,student_id,db)


#  add aatendance 
@router.post("/", response_model=AttendanceOut)
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):
         return  attendance_co.mark_attendance(data,db)


# update attendance 
@router.put("/{attendance_id}", response_model=AttendanceOut)
def update_attendance(attendance_id: int, data: AttendanceCreate, db: Session = Depends(get_db)):
    return attendance_co.update_attendance(attendance_id,data,db)