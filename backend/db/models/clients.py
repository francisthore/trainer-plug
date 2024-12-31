from sqlalchemy import Column, ForeignKey, String
from .base_model import Base, BaseModel


class Client(Base, BaseModel):
    """
        Class model of the client
    """
    __tablename__ = 'clients'

    user_id = Column(String, ForeignKey('users.id'), unique=True)
    linked_trainer_id = Column(String, ForeignKey('trainers.user_id'), nullable=True)
