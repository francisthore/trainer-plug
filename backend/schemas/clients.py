from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from schemas.trainers import TrainerResponse


# class ClientCreate(BaseModel):
#     """Creates a new client record"""
#     user_id: str


class ClientUpdate(BaseModel):
    """Updates a client record"""
    linked_trainer_id: str


class ClientResponse(BaseModel):
    """Response schema for a client"""
    user_id: str
    linked_trainer_id: Optional[str] = Field(default=None)

    model_config = {
        "from_attributes": True
    }


class ClientWithTrainerResponse(BaseModel):
    user_id: str
    trainer: Dict[str, Any]
