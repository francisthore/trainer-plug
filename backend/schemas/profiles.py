from pydantic import BaseModel, Field, field_serializer
from typing import Optional, Text
from core.config import settings
from datetime import date


class ProfileCreate(BaseModel):
    """Profile creation schema"""
    user_id: str
    full_name: Optional[str] = None
    phone_number: Optional[str] = None 
    dob: Optional[date] = None
    profile_picture: Optional[str] = settings.BASE_PROFILE_PIC
    bio: Text = Field(min_length=2)


class ProfileUpdate(BaseModel):
    """Profile creation schema"""
    full_name: Optional[str] = None
    phone_number: Optional[str] = None 
    dob: Optional[date] = None
    profile_picture: Optional[str] = None
    bio: Optional[Text] = None


class ProfileResponse(BaseModel):
    """Profile response schema"""
    id: str
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    dob: Optional[date] = None
    profile_picture: str
    bio: Text

    model_config = {
        "from_attributes": True
    }
