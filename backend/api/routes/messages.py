from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from db.models.messages import Message
from db.models.notifications import Notification
from db.session import get_db
from schemas.messages import MessageCreate, MessageResponse
from crud.db_hepers import(
    create_object,
    get_object_by_id,
    get_user_email
)
from typing import List
from core.send_email_util import send_email_message


router = APIRouter(prefix='/api/messages')


@router.post('/', response_model=MessageResponse, status_code=201)
async def send_message(
    data: MessageCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
    ):
    """Sends a message from one user to the other"""
    message_data = data.model_dump()
    new_message = create_object(
        Message, message_data, db
    )
    notification_data = {
        "user_id": new_message.receiver_id,
        "message": "You have a new message, login to see the message"
    }
    
    notification = create_object(
        Notification, notification_data, db
    )

    background_tasks.add_task(
        send_email_message,
        get_user_email(user_id=notification_data.get('user_id'), db=db),
        "New Notification",
        notification.message
    )

    return MessageResponse.model_validate(new_message)


@router.get('/{user_id}', response_model=List[MessageResponse])
async def get_messages(user_id: str, db: Session = Depends(get_db)):
    """Gets messages sent by user"""
    messages = db.query(Message).filter(
        (Message.sender_id == user_id) | (Message.receiver_id == user_id)
    ).order_by(Message.created_at.desc()).all()
    if not messages:
        raise HTTPException(
            status_code=404,
            detail="No messages found"
        )

    return [MessageResponse.model_validate(message) for message in messages]


@router.patch('/{message_id}/read', response_model=MessageResponse)
async def mark_message_as_read(
    message_id: str, db: Session = Depends(get_db)
    ):
    """Marks a message as read"""
    message = get_object_by_id(
        Message, message_id, db
    )
    message.is_read = True
    db.commit()
    db.refresh(message)
    
    return MessageResponse.model_validate(message)
