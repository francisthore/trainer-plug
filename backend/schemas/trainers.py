from pydantic import BaseModel, Field
from typing import Optional


class TrainerBase(BaseModel):
    """Base model schema for the trainer"""
    user_id: str
    specialization: str
    years_of_experience: int
    hourly_rate: float


class TrainerCreate(TrainerBase):
    """Trainer creation schema"""
    pass


class TrainerResponse(BaseModel):
    """Response schema for a trainer"""
    user_id: str
    specialization: str
    years_of_experience: int
    hourly_rate: float
    verification_status: str

    model_config = {
        "from_attributes": True
    }


class TrainerUpdate(BaseModel):
    """Updating the trainer"""
    specialization: Optional[str] = None
    years_of_experience: Optional[int] = None
    hourly_rate: Optional[float] = None
    verification_status: Optional[str] = None



class TrainerFullResponse(BaseModel):
    """Trainer full profile response"""
    user_id: str
    full_name: str
    bio: str
    profile_picture: str
    hourly_rate: float
    specialization: str
    years_of_experience: int

    model_config = {
        "from_attributes": True
    }
