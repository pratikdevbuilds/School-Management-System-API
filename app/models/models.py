from sqlalchemy import Enum ,Column,Integer,String,Float,Date,Boolean,ForeignKey,Text
from sqlalchemy .orm import relationship  
from app.db.database import Base
import enum

class GenderEnum(str,enum.Enum):
   male = "Male"
   female = "Female"
   other = "Other"

class StatusEnum(str,enum.Enum):
    active = "Active"
    inactive = "Inactive"  

# Student
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True,index=True)
    admission_number = Column(String,unique=True,index=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False) 
    date_of_birth = Column(Date)
    gender = Column(String)
    blood_group = Column(String)
    class_id = Column(Integer,ForeignKey("classes.id"))
    section = Column(String)
    roll_number = Column(String)
    admission_date = Column(Date)
    status = Column(String ,default="Active")
    parent_name = Column(String)
    parent_phone = Column(String)
    parent_email = Column(String)
    address = Column(Text)

    school_class = relationship("SchoolClass" ,back_populates="students")
    attendances = relationship("Attendance", back_populates="student")
    fee_payments = relationship("FeePayment", back_populates="student")

# Teacher 

class Teacher(Base):
     __tablename__ = "teachers"
     id = Column(Integer,primary_key=True,index=True)
     employee_id =  Column(String,unique=True,index=True)
     first_name = Column(String,nullable=False)
     last_name = Column(String,nullable=False) 
     email = Column(String)
     phone  = Column(String)
     gender = Column(String)
     qualification = Column(String)
     specialization = Column(String)
     joining_date = Column(Date)
     status = Column(String,default="Active")
     salary = Column(Float)
     address  = Column(Text)
     
     
     subjects = relationship("Subject", back_populates="teacher")


# SchoolClass 
class SchoolClass(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    section = Column(String)
    room_number = Column(String)
    capacity = Column(Integer)
    academic_year = Column(String)
    class_teacher_id = Column(Integer, ForeignKey("teachers.id"))

    subjects = relationship("Subject", back_populates="school_class")
    students = relationship("Student", back_populates="school_class")

# Subject
class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, unique=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    type = Column(String, default="Core")
    description = Column(Text)

    school_class = relationship("SchoolClass", back_populates="subjects")
    teacher = relationship("Teacher", back_populates="subjects")

# Attendance
class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))
    section = Column(String)
    status = Column(String, default="Present")
    remarks = Column(String)

    student = relationship("Student", back_populates="attendances")

# Exams
class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    date = Column(Date)
    total_marks = Column(Float)
    passing_marks = Column(Float)
    academic_year = Column(String)
    term = Column(String)
    status = Column(String, default="Scheduled")

    results = relationship("ExamResult", back_populates="exam")


# result
class ExamResult(Base):
    __tablename__ = "exam_results"

    id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey("exams.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    marks_obtained = Column(Float)
    grade = Column(String)
    remarks = Column(String)
# yha check kar 
    exam = relationship("Exam", back_populates="results")

    
# Fee- structure
class FeeStructure(Base):
    __tablename__ = "fee_structures"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"))
    amount = Column(Float, nullable=False)
    frequency = Column(String, default="Monthly")
    academic_year = Column(String)
    due_day = Column(Integer)
    description = Column(Text)


# FeePayment
class FeePayment(Base):
    __tablename__ = "fee_payments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    fee_structure_id = Column(Integer, ForeignKey("fee_structures.id"))
    amount = Column(Float, nullable=False)
    payment_date = Column(Date)
    payment_method = Column(String, default="Cash")
    receipt_number = Column(String)
    status = Column(String, default="Paid")
    month = Column(String)
    remarks = Column(String)

    student = relationship("Student", back_populates="fee_payments")


# Announcement
class Announcement(Base):
    __tablename__ = "announcements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    target_audience = Column(String, default="All")
    priority = Column(String, default="Normal")
    publish_date = Column(Date)
    expiry_date = Column(Date)
    author_name = Column(String)
    status = Column(String, default="Published")
    






    
    




   