from sqlalchemy import Column, String, Boolean
from .base_model import Base, BaseModel


class User(Base, BaseModel):
    """
        DB model for User
    """
    __tablename__ = 'users'

    username = Column(String(100), nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String(250), nullable=False, unique=True)
    role = Column(String(10), default='client')
    is_verified = Column(Boolean, default=False)
