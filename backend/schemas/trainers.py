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


class TrainerDelete(BaseModel):
    """delete trainer"""
    id: str
