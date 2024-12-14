from pydantic import BaseModel, field_validator, Field, EmailStr
from typing import Optional
from datetime import datetime
import re



class UserBase(BaseModel):
    """User base schema"""
    nickname: str
    full_name: Optional[str]
    email: EmailStr
    phone_number: Optional[str]
    role: str
    is_verified: bool


class UserCreate(UserBase):
    """Handles user creation"""
    password: str

    @field_validator
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character")
        return value
    

class UserUpdate(BaseModel):
    """Handles user update"""
    nickname: Optional[str]
    full_name: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[str]
    password: Optional[str]
    role: Optional[str]


class UserResponse(UserBase):
    """Handles data shown on response"""
    id: str

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    """Handles user login schema"""
    email: EmailStr
    password: str
