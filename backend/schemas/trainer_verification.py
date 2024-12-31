from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime


class TrainerVerificationCreate(BaseModel):
    """Trainer verification create schema"""
    user_id: str
    government_id_url: Optional[str] = None
    certifications_url: Optional[str] = None
    selfie_url: Optional[str] = None
    proof_of_res_url: Optional[str] = None


class TrainerVerificationUpdate(BaseModel):
    """Trainer verification update schema"""
    government_id_url: Optional[str] = None
    certifications_url: Optional[str] = None
    selfie_url: Optional[str] = None
    proof_of_res_url: Optional[str] = None


class TrainerVerificationResponse(BaseModel):
    """Trainer verification response schema"""
    user_id: str
    government_id_url: Optional[str]
    certifications_url: Optional[str]
    selfie_url: Optional[str]
    proof_of_res_url: Optional[str]
    submitted_at: datetime
    verified_at: Optional[datetime]

    model_config = {
        "from_attributes": True
    }

