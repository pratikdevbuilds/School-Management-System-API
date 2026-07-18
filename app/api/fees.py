from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.models.models import FeePayment, FeeStructure,User
from app.schema.schemas import FeePaymentCreate, FeePaymentOut
from app.controller import fees_co
from app.core.security import require_teacher_or_admin,require_admin
router = APIRouter()

# check by id student pyment 
@router.get("/payments", response_model=List[FeePaymentOut])
def get_payments(student_id: Optional[int] = None, db: Session = Depends(get_db),current_user: User = Depends(require_teacher_or_admin)):
   return fees_co.get_payments(student_id,db,current_user)


# fee pyment create
@router.post("/payments", response_model=FeePaymentOut)
def create_payment(data: FeePaymentCreate, db: Session = Depends(get_db),current_user: User = Depends(require_admin)):
   return fees_co.create_payment(data,db,current_user)


# delete fee data
@router.delete("/payments/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db),current_user: User = Depends(require_admin)):
    return fees_co.delete_payment(payment_id,db,current_user)