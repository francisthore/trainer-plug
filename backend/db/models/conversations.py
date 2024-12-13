from sqlalchemy import Column, String, ForeignKey
from .base_model import Base, BaseModel


class Conversation(Base, BaseModel):
    """Class model for conversations"""
    __tablename__ = 'conversations'

    client_id = Column(String, ForeignKey('client.id'))
    trainer_id = Column(String, ForeignKey('trainer.id'))
