from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi.responses import JSONResponse
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


@router.post('/login')
async def login_user(
    user: UserLogin,
    response: Response,
    db: Session = Depends(get_db)
    ):
    """Logs a user in"""
    auth_user = authenticate_user(db, user.username, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token({"sub": auth_user.id, "role": auth_user.role})
    refresh_token = create_refresh_token({"sub": auth_user.username})
    
    response.set_cookie(
        key="access_token", value=access_token,
        httponly=True, samesite="strict"
    )

    response.set_cookie(
        key="refresh_token", value=refresh_token,
        httponly=True, samesite="strict"
    )


    logger.info(f"User {auth_user.username} authenticated successfully.")

    return {
            "success": True,
            "id": auth_user.id,
            "role": auth_user.role
        }


@router.post('/logout')
async def logout_user(response: Response):
    """Logs a user out"""
    response.delete_cookie(
        key="access_token", httponly=True, samesite="strict"
    )
    response.delete_cookie(
        key="refresh_token", httponly=True, samesite="strict"
    )

    return {
        "status_code": 2000,
        "success": True,
        "message": "Logged out successfully"
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


@router.get("/me")
async def get_authenticated_user(current_user: dict = Depends(get_current_user)):
    return {"user": current_user}
