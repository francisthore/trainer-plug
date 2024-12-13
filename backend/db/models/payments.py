from sqlalchemy import Column, String, Float, ForeignKey, DateTime
from .base_model import Base, BaseModel
from datetime import datetime


class Payment(Base, BaseModel):
    """Class model for the payment"""
    __tablename__ = 'payments'

    trainer_id = Column(String, ForeignKey('trainers.id'), nullable=False)
    client_id = Column(String, ForeignKey('clients.id'), nullable=False)
    amount = Column(Float, default=0.00)
    payment_date = Column(DateTime, default=datetime.now())
    payment_status = Column(String, default='Pending')
