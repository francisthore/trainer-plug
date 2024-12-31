from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MessageCreate(BaseModel):
    """Message creation schema"""
    sender_id: str
    receiver_id: str
    content: str


class MessageResponse(BaseModel):
    """Message response schema"""
    id: str
    sender_id: str
    receiver_id: str
    content: str
    created_at: datetime
    is_read: bool

    model_config = {
        "from_attributes": True
    }
