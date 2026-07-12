from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.models import user
from app.schema.schemas import UserCreate, UserResponse
from app.controller import user_co
router = APIRouter()

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    data: UserCreate,
    db: Session = Depends(get_db)
):
    return user_co.register_user(data, db)