from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_current_user
from backend.app.database.database import get_db
from backend.app.models.user import User

from backend.app.schemas.auth import (
    UserRegister,
    UserLogin,
    UserResponse,
    TokenResponse
)

from backend.app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from backend.app.core.logger import logger


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/health")
def auth_health():
    logger.info("Authentication health endpoint accessed")

    return {
        "status": "ok",
        "service": "CampusAI Authentication"
    }


# REGISTER
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    logger.info(f"Registration attempt for email: {user_data.email}")

    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        logger.warning(
            f"Registration failed. Email already exists: {user_data.email}"
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    new_user = User(
        email=user_data.email,
        hashed_password=hash_password(
            user_data.password
        )
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    logger.info(
        f"New user registered successfully. User ID: {new_user.id}, Email: {new_user.email}"
    )

    return new_user


# LOGIN
@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):
    logger.info(f"Login attempt for email: {user_data.email}")

    user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if not user:
        logger.warning(
            f"Login failed. User not found: {user_data.email}"
        )

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(
        user_data.password,
        user.hashed_password
    ):
        logger.warning(
            f"Login failed. Incorrect password for: {user.email}"
        )

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not user.is_active:
        logger.warning(
            f"Inactive user attempted login. User ID: {user.id}"
        )

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )

    access_token = create_access_token(
        data={
            "sub": str(user.id)
        }
    )

    logger.info(
        f"User logged in successfully. User ID: {user.id}"
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(get_current_user)
):
    logger.info(
        f"Profile accessed. User ID: {current_user.id}"
    )

    return current_user