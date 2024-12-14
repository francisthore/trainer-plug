from pydantic import BaseModel, field_validator, Field, EmailStr
from typing import Optional, Dict
from datetime import datetime
import re



class UserBase(BaseModel):
    """User base schema"""
    username: str
    email: EmailStr
    role: str
    is_verified: bool = Field(default=False)


class UserCreate(UserBase):
    """Handles user creation"""
    password: str

    @field_validator('password')
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
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    role: Optional[str]


class UserResponse(BaseModel):
    id: str
    role: str
    is_verified: bool

    model_config = {
        "from_attributes": True
    }



class UserLogin(BaseModel):
    """Handles user login schema"""
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: Dict[str, str]
