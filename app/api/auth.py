from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserRegister, UserLogin
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/register")
async def register(user: UserRegister):
    db: Session = SessionLocal()

    try:
        existing = db.query(User).filter(
            User.username == user.username
        ).first()

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

        new_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password)
        )

        db.add(new_user)
        db.commit()

        return {
            "status": "success",
            "message": "User registered successfully"
        }

    finally:
        db.close()


@router.post("/login")
async def login(user: UserLogin):
    db: Session = SessionLocal()

    try:
        existing = db.query(User).filter(
            User.username == user.username
        ).first()

        if existing is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid username or password"
            )

        if not verify_password(user.password, existing.password):
            raise HTTPException(
                status_code=401,
                detail="Invalid username or password"
            )

        token = create_access_token(
            {"sub": existing.username}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    finally:
        db.close()