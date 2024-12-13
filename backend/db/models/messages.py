from sqlalchemy import Column, Text, String, ForeignKey, DateTime
from .base_model import Base, BaseModel
from datetime import datetime


class Message(Base, BaseModel):
    """Class model for the messages"""
    __tablename__ = 'messages'

    sender_id = Column(String, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(String, ForeignKey('users.id'), nullable=False)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.now())
