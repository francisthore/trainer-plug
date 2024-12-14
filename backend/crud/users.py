from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.models.users import User
from schemas.users import UserCreate, UserResponse, UserLogin, UserUpdate
from utils.auth import hash_password, verify_password

def create_user(db: Session, user: UserCreate):
    """Creates a new user"""
    try:
        hashed_password = hash_password(user.password)
        db_user = User(
        username=user.username,
        password_hash=hashed_password,
        email=user.email,
        role=user.role
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        db.rollback()
        raise ValueError('User wth this email already exists')
    except Exception as e:
        raise RuntimeError('An error occured while creating user')


def get_user(db: Session, username: str):
    """Retrieves a user from the db"""
    try:
        return db.query(User).filter(User.username == username).first()
    except Exception as e:
        raise HTTPException(status_code=404, detail='User not found, consider registering')

def authenticate_user(db: Session, username: str, password: str):
    """Authenticates a user"""
    user = get_user(db, username)
    if user and verify_password(password, user.password_hash):
        return user
    return None
