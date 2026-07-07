from fastapi import  Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.models.models import FeePayment, FeeStructure
from app.schema.schemas import FeePaymentCreate, FeePaymentOut

 
# get pyment 
def get_payments(student_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(FeePayment)
    if student_id:
        query = query.filter(FeePayment.student_id == student_id)
    return query.all()


# create pyment for fee 
def create_payment(data: FeePaymentCreate, db: Session ):
    payment = FeePayment(**data.model_dump())
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment

# delete pyment 
def delete_payment(payment_id: int, db: Session ):
    payment = db.query(FeePayment).filter(FeePayment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    db.delete(payment)
    db.commit()
    return {"message": "Payment deleted"}