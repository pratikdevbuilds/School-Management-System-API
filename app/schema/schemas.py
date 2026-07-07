from pydantic import BaseModel
from typing import Optional
from datetime import date

#Student 
class StudentBase(BaseModel):   
    admission_number: str
    first_name: str
    last_name: str
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    blood_group: Optional[str] = None
    class_id: Optional[int] = None
    section: Optional[str] = None
    roll_number: Optional[str] = None
    admission_date: Optional[date] = None
    status: Optional[str] = "Active"
    parent_name: Optional[str] = None
    parent_phone: Optional[str] = None
    parent_email: Optional[str] = None
    address: Optional[str] = None

class StudentCreate(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int
    class Config:
        from_attributes = True

# Teacher 
class TeacherBase(BaseModel):
    employee_id: str
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    gender: Optional[str] = None
    qualification: Optional[str] = None
    specialization: Optional[str] = None
    joining_date: Optional[date] = None
    status: Optional[str] = "Active"
    salary: Optional[float] = None
    address: Optional[str] = None

class TeacherCreate(TeacherBase):
    pass

class TeacherOut(TeacherBase):
    id: int
    class Config:
        from_attributes = True

# SchoolClass 
class ClassBase(BaseModel):
    name: str
    section: Optional[str] = None
    room_number: Optional[str] = None
    capacity: Optional[int] = None
    academic_year: Optional[str] = None
    class_teacher_id: Optional[int] = None

class ClassCreate(ClassBase):
    pass

class ClassOut(ClassBase):
    id: int
    class Config:
        from_attributes = True

# Subject
class SubjectBase(BaseModel):
    name: str
    code: str
    class_id: Optional[int] = None
    teacher_id: Optional[int] = None
    type: Optional[str] = "Core"
    description: Optional[str] = None

class SubjectCreate(SubjectBase):
    pass

class SubjectOut(SubjectBase):
    id: int
    class Config:
        from_attributes = True

# Attendance
class AttendanceBase(BaseModel):
    date: date
    student_id: int
    class_id: Optional[int] = None
    section: Optional[str] = None
    status: Optional[str] = "Present"
    remarks: Optional[str] = None

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceOut(AttendanceBase):
    id: int
    class Config:
        from_attributes = True

# Exam 
class ExamBase(BaseModel):
    name: str
    class_id: Optional[int] = None
    subject_id: Optional[int] = None
    date: Optional[date] = None
    total_marks: Optional[float] = None
    passing_marks: Optional[float] = None
    academic_year: Optional[str] = None
    term: Optional[str] = None
    status: Optional[str] = "Scheduled"

class ExamCreate(ExamBase):
    pass

class ExamOut(ExamBase):
    id: int
    class Config:
        from_attributes = True

# FeePayment 
class FeePaymentBase(BaseModel):
    student_id: int
    fee_structure_id: Optional[int] = None
    amount: float
    payment_date: Optional[date] = None
    payment_method: Optional[str] = "Cash"
    receipt_number: Optional[str] = None
    status: Optional[str] = "Paid"
    month: Optional[str] = None
    remarks: Optional[str] = None

class FeePaymentCreate(FeePaymentBase):
    pass

class FeePaymentOut(FeePaymentBase):
    id: int
    class Config:
        from_attributes = True

# Announcement
class AnnouncementBase(BaseModel):
    title: str
    content: str
    target_audience: Optional[str] = "All"
    priority: Optional[str] = "Normal"
    publish_date: Optional[date] = None
    expiry_date: Optional[date] = None
    author_name: Optional[str] = None
    status: Optional[str] = "Published"

class AnnouncementCreate(AnnouncementBase):
    pass

class AnnouncementOut(AnnouncementBase):
    id: int
    class Config:
        from_attributes = True