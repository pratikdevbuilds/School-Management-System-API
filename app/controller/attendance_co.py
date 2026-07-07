from fastapi import APIRouter, Depends, Query,status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from app.db.database import get_db
from app.models.models import Attendance
from app.schema.schemas import AttendanceCreate, AttendanceOut

# get attendances
def get_attendance(
    date_filter: Optional[date] = Query(None, alias="date"),
    class_id: Optional[int] = None,
    student_id: Optional[int] = None,
    db: Session = Depends(get_db)
): 
    query = db.query(Attendance)
    if date_filter:
        query = query.filter(Attendance.date == date_filter)
    if class_id:
        query = query.filter(Attendance.class_id == class_id)
    if student_id:
        query = query.filter(Attendance.student_id == student_id)
    return query.all()