from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schema.schemas import UserCreate, UserResponse
from app.controller import user_co
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import get_current_user
from app.models.models import User
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

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return user_co.login_user(form_data, db)

@router.get("/profile")
def profile(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role
    }