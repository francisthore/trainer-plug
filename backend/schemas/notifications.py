from pydantic import BaseModel
from datetime import datetime


class NotificationCreate(BaseModel):
    """Notification create schema"""
    user_id: str
    message: str


class NotificationResponse(BaseModel):
    """Notification response schema"""
    id: str
    user_id: str
    message: str
    created_at: datetime
    is_read: bool

    model_config = {
        "from_attributes": True
    }
