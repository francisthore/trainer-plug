from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from utils.auth import create_access_token, create_refresh_token, verify_access_token
from schemas.users import UserCreate, UserLogin, UserResponse, TokenResponse
from db.models.users import User
from db.session import get_db
from crud.users import create_user, authenticate_user, get_user
from core.send_email_util import send_email_message
from core.message_templates import email_verification_msg
from utils.logging_helper import logger
from utils.auth import generate_verification_link, get_current_user


router = APIRouter(prefix='/api/auth')

@router.post('/register', response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """Registers anew user"""
    new_user = create_user(db, user)
    verification_link = generate_verification_link(new_user.username)
    message = email_verification_msg(verification_link)
    send_email_message(
            new_user.email,
            subject="Verify your email",
            message=message
            )
    logger.info("Verification email sent to %s", new_user.email)
    return UserResponse.model_validate(new_user)


@router.post('/login', response_model=TokenResponse)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    """Logs a user in"""
    auth_user = authenticate_user(db, user.username, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token({"sub": auth_user.username, "role": auth_user.role})
    refresh_token = create_refresh_token({"sub": auth_user.username})
    logger.info(f"User {auth_user.username} authenticated successfully.")

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": {"username": auth_user.username, "role": auth_user.role}
    }


@router.get('/verify-email')
async def verify_email(token: str, db: Session = Depends(get_db)):
    """Verifies email of a user"""
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=400, detail='Invalid or expired token')

    username = payload.get('sub')
    if not username:
        raise HTTPException(status_code=400, detail='Invalid token payload')

    user = get_user(db, username)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    if user.is_verified:
        raise HTTPException(status_code=400, detail='User is already verified')

    user.is_verified = True
    db.commit()
    logger.info(f"User {username} verified their email.")

    return {'msg': 'Email verified successfully.'}


@router.post('/resend-verification')
async def resend_verification(
    username: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
    ):
    """Regenerates and resends verification email."""
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.is_verified:
        raise HTTPException(status_code=400, detail="User is already verified")

    verification_link = generate_verification_link(user.username)
    message = email_verification_msg(verification_link)
    send_email_message(
            user.email,
            subject="Verify your email",
            message=message
            )
    logger.info(f"Verification email resent to {user.email}")
    return {"msg": "Verification email resent successfully."}
