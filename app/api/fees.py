from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.models.models import FeePayment, FeeStructure
from app.schema.schemas import FeePaymentCreate, FeePaymentOut
from app.controller import fees_co

router = APIRouter()
# check by id student pyment 
@router.get("/payments", response_model=List[FeePaymentOut])
def get_payments(student_id: Optional[int] = None, db: Session = Depends(get_db)):
   return fees_co.get_payments(student_id,db)


# fee pyment create
@router.post("/payments", response_model=FeePaymentOut)
def create_payment(data: FeePaymentCreate, db: Session = Depends(get_db)):
   return fees_co.create_payment(data,db)


# delete fee data
@router.delete("/payments/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return fees_co.delete_payment(payment_id,db)