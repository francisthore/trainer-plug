from sqlalchemy import Column, DateTime, String, ForeignKey
from .base_model import Base, BaseModel
from datetime import datetime


class TrainerVerification(Base, BaseModel):
    """
        Class model for trainer verification
    """
    __tablename__ = 'trainer_verifications'

    user_id = Column(String, ForeignKey('users.id'), unique=True)
    government_id_url = Column(String, default=None)
    certifications_url = Column(String, default=None)
    selfie_url = Column(String, default=None)
    proof_of_res_url = Column(String, default=None)
    submitted_at = Column(DateTime, default=datetime.now())
    verified_at = Column(DateTime, nullable=True)
