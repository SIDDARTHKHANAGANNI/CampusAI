from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from backend.app.database.database import get_db
from backend.app.models.user import User
from backend.app.models.student import Student

from backend.app.core.security import decode_access_token
from backend.app.core.logger import logger

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    payload = decode_access_token(token)

    if payload is None:
        logger.warning("Authentication failed. Invalid or expired JWT token.")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    user_id = payload.get("sub")

    if user_id is None:
        logger.warning("Authentication failed. JWT token missing 'sub' claim.")

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

    try:
        user_id = int(user_id)
    except ValueError:
        logger.warning(
            f"Authentication failed. Invalid user ID in token: {user_id}"
        )

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        logger.warning(
            f"Authentication failed. User ID {user_id} not found."
        )

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    if not user.is_active:
        logger.warning(
            f"Authentication failed. Inactive user ID: {user.id}"
        )

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )

    logger.info(
        f"Authenticated user successfully. User ID: {user.id}"
    )

    return user


def get_current_student(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    student = (
        db.query(Student)
        .filter(Student.user_id == current_user.id)
        .first()
    )

    if not student:
        logger.warning(
            f"Student profile not found for User ID: {current_user.id}"
        )

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student profile not found"
        )

    logger.info(
        f"Student authenticated successfully. Student ID: {student.id}"
    )

    return student