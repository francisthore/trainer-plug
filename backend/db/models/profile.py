from sqlalchemy import Column, String, ForeignKey, Text
from .base_model import Base, BaseModel
from .users import User


class Profile(Base, BaseModel):
    """
       Class model for a user profile
    """
    __tablename__ = 'profiles'

    user_id = Column(String, ForeignKey('users.id'), index=True)
    profile_picture = Column(String)
    bio = Column(Text)
