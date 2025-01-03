from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.users import User
from schemas.users import UserResponse
from typing import List
from utils.auth import get_current_user


router = APIRouter(prefix='/api')


@router.get('/users', response_model=List[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    """Gets all users in db"""
    users = db.query(User).all()
    return [UserResponse.model_validate(user) for user in users]
