from sqlalchemy import Column, Float, String, Integer, ForeignKey
from .base_model import Base, BaseModel


class Trainer(Base, BaseModel):
    """
        Class model for a trainer
    """
    __tablename__ = 'trainers'

    user_id = Column(String, ForeignKey('users.id'), unique=True)
    specialization = Column(String, nullable=False)
    years_of_experience = Column(Integer, nullable=False)
    hourly_rate = Column(Float, nullable=False)
    verification_status = Column(String, default='Pending')
