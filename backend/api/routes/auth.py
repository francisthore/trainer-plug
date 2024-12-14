from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from utils.auth import create_access_token, create_refresh_token, verify_access_token
from schemas.users import UserCreate, UserLogin, UserResponse, TokenResponse
from db.models.users import User
from db.session import get_db
from crud.users import create_user, authenticate_user, get_user


router = APIRouter(prefix='/api/auth')

@router.post('/register', response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """Registers anew user"""
    try:
        new_user = create_user(db, user)
        token = create_access_token({'sub': new_user.username, 'exp': 3600})
        verification_link = f'http://localhost:8000/api/auth/verify-email?token={token}'
        print(verification_link)
        return UserResponse.model_validate(new_user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail='Email already registered')
    except ValueError as e:
        raise HTTPException(status_code=400, detail=(e))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail='An uncex error occured')


@router.post('/login', response_model=TokenResponse)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    """Logs a user in"""
    try:
        auth_user = authenticate_user(db, user.username, user.password)
        if not auth_user:
            raise HTTPException(status_code=401, detail="Invalid username or password")

        access_token = create_access_token({"sub": auth_user.username, "role": auth_user.role})
        refresh_token = create_refresh_token({"sub": auth_user.username})

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": {"username": auth_user.username, "role": auth_user.role}
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


@router.get('/verify-email')
async def verify_email(token: str, db: Session = Depends(get_db)):
    """Verifys email of a user"""
    payload =  verify_access_token(token)
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
    return {'msg': 'Email verified successfully.'}


@router.post('/resend-verification')
async def resend_verification(
    username: str,
    db: Session = Depends(get_db),
    ):
    """Regenerates and resends verification email."""
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.is_verified:
        raise HTTPException(status_code=400, detail="User is already verified")

    token = create_access_token({'sub': user.username, 'exp': 3600})
    verification_link = f'http://localhost:8000/api/auth/verify-email?token={token}'
    print(verification_link)
    return {"msg": "Verification email resent successfully."}
