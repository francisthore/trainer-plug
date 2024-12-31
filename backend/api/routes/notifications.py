from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from db.session import get_db
from db.models.notifications import Notification
from crud.db_hepers import(
    create_object,
    get_object_by_id
)
from schemas.notifications import NotificationCreate, NotificationResponse
from typing import List

router = APIRouter(prefix='/api/notifications')


@router.post('/', response_model=NotificationResponse, status_code=201)
async def send_notification(
    data: NotificationCreate,
    db: Session = Depends(get_db)
    ):
    """Creates a new notification"""
    notification_data = data.model_dump()
    new_notification = create_object(
        Notification, notification_data, db
    )
    return NotificationResponse.model_validate(new_notification)


@router.get('/{user_id}',
            response_model=List[NotificationResponse])
async def get_user_notifications(
    user_id: str, db: Session = Depends(get_db)
    ):
    """Retrieves notifications for a user"""
    notifications = db.query(Notification).filter(
        Notification.user_id == user_id).all()
    if not notifications:
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": "no notifications found"
            }
        )
    return [NotificationResponse.model_validate(notification)
            for notification in notifications]


@router.patch('/{notification_id}/read', response_model=NotificationResponse)
async def mark_notification_as_read(
    notification_id: str, db: Session = Depends(get_db)
    ):
    """Marks notification as read"""
    notification = get_object_by_id(
        Notification,
        notification_id,
        db
    )
    notification.is_read = True
    db.commit()
    db.refresh(notification)

    return NotificationResponse.model_validate(notification)

