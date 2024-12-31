from sqlalchemy import Column, Text, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from .base_model import Base, BaseModel
from datetime import datetime


class Message(Base, BaseModel):
    """Class model for the messages"""
    __tablename__ = 'messages'

    sender_id = Column(String, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(String, ForeignKey('users.id'), nullable=False)
    content = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)


    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])
