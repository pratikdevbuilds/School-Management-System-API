from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from app.models.models import User
from app.schema.schemas import UserCreate
from app.core.security import hash_password


def register_user(data: UserCreate, db: Session):
  existing_user = db.query(User).filter(
    User.email == data.email
).first()
  if existing_user:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail="Email already exists"
  )
  existing_username = db.query(User).filter(
    User.username == data.username
).first()

  if existing_username:
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Username already exists"
    )