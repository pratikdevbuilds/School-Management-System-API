from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.models import User
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from jose import JWTError, jwt
from jose import jwt


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
    minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
)
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(
    to_encode,
    settings.SECRET_KEY,
    algorithm=settings.ALGORITHM
)
    return encoded_jwt
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/user/login"
)
    
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        raise credentials_exception

    return user

# require_admin()

def require_admin(
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "Admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Admin can perform this action"
        )

    return current_user

# require_teacher_or_admin()
def require_teacher_or_admin(
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in ["Admin", "Teacher"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied"
        )

    return current_user

# require_student()     
def require_student(
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "Student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Student can access this resource"
        )

    return current_user
def require_teacher_or_admin(
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in ["Admin", "Teacher"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied"
        )

    return current_user