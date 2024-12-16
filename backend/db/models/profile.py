from sqlalchemy import Column, String, ForeignKey, Text, Date
from .base_model import Base, BaseModel
from core.config import settings

class Profile(Base, BaseModel):
    """
       Class model for a user profile
    """
    __tablename__ = 'profiles'

    user_id = Column(String, ForeignKey('users.id'),unique=True, index=True)
    full_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    dob = Column(Date, nullable=True)
    profile_picture = Column(String, default=settings.BASE_PROFILE_PIC)
    bio = Column(Text, nullable=False)
