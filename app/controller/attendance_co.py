from fastapi import APIRouter, Depends, Query,status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from app.db.database import get_db
from app.models.models import Attendance
from app.schema.schemas import AttendanceCreate, AttendanceOut

# get attendances
def get_attendance(
    date_filter ,
    class_id ,
    student_id,
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


#  add aatendence 
def mark_attendance(data: AttendanceCreate, db: Session):
    attendance = Attendance(**data.model_dump())
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance

# update attendance 
def update_attendance(attendance_id: int, data: AttendanceCreate, db: Session = Depends(get_db)):
    record = db.query(Attendance).filter(Attendance.id == attendance_id).first()
    for key, value in data.model_dump().items():
        setattr(record, key, value)
    db.commit()
    db.refresh(record)
    return record