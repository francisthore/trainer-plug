from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..db.models.users import User
from ..schemas.users import UserCreate
from ..utils.password import hash_password, verify_password

def create_user(db: Session, user: UserCreate):
    """Creates a new user"""
    try:
        hashed_password = hash_password(user.password)
        db_user = User(
        nickname=user.nickname,
        password_has=hashed_password,
        full_name=user.full_name,
        email=user.email,
        phone_number=user.phone_number,
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


def authenticate_user(db: Session, email: str, password: str):
    """Authenticates a user"""
    user = db.query(User).filter(User.email).first()
    if user and verify_password(password, user.password_hash):
        return user
    return None
