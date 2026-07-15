from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from app.models.models import User
from app.schema.schemas import UserCreate
from app.core.security import hash_password,verify_password,create_access_token
from fastapi.security import OAuth2PasswordRequestForm

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
  # Hash password
  hashed_password = hash_password(data.password)

  # Create User object
  new_user = User(
        username=data.username,
        email=data.email,
        hashed_password=hashed_password,
        role=data.role
    )

  # Save to database
  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return new_user



def login_user(form_data: OAuth2PasswordRequestForm, db: Session):
   
   existing_user = db.query(User).filter(User.email== form_data.username).first()

   if not  existing_user:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid email or password"
    ) 
    # verify password 
   if not verify_password(
    form_data.password,
    existing_user.hashed_password
    ):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid email or password"
    )
    # token banao 
   access_token = create_access_token(
     data={"sub": existing_user.email}
)   
   return {
    "access_token": access_token,
    "token_type": "bearer"
}
    