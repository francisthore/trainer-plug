from sqlalchemy import Column, String, Boolean
from .base_model import Base, BaseModel


class User(Base, BaseModel):
    """
        DB model for User
    """
    __tablename__ = 'users'

    nickname = Column(String(50), nullable=False)
    full_name = Column(String(250))
    email = Column(String(), unique=True)
    password_hash = Column(String(250))
    phone_number = Column(String, nullable=True)
    role = Column(String(6), default='client')
    is_verified = Column(Boolean(), default=False)
