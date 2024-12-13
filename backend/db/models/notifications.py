from sqlalchemy import Boolean, Column, ForeignKey, Text, String
from .base_model import Base, BaseModel


class Notification(Base, BaseModel):
    """Class model for notifications"""
    __tablename__ = 'notifications'

    user_id = Column(String, ForeignKey('users.id'))
    message = Column(Text, nullable=True)
    is_read = Column(Boolean, default=False)
