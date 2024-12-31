from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from typing import Dict, Any
from db.models.users import User


def get_object_by_id(cls, id: str, db: Session = Depends(get_db)) -> Dict:
    """retrieves an object from db"""
    obj = db.query(cls).filter(
        cls.id == id
    ).first()
    if not obj:
        raise HTTPException(status_code=404, detail=f"Resource doesn't exist")
    return obj

def get_object_by_user_id(cls, user_id: str, db: Session = Depends(get_db)) -> Dict:
    """retrieves an object from db"""
    obj = db.query(cls).filter(
        cls.user_id == user_id
    ).first()
    if not obj:
        raise HTTPException(status_code=404, detail=f"Resource doesn't exist")
    return obj


def delete_object_by_id(cls, id: str, db: Session = Depends(get_db)) -> bool:
    """deletes an object from db"""
    obj = db.query(cls).filter(
        cls.id == id
    ).first()
    if not obj:
        raise HTTPException(status_code=404, detail=f"Resource doesn't exist")
    db.delete(obj)
    db.commit()
    return True

def delete_object_by_user_id(cls, user_id: str, db: Session = Depends(get_db)) -> bool:
    """deletes an object from db"""
    obj = db.query(cls).filter(
        cls.user_id == user_id
    ).first()
    if not obj:
        raise HTTPException(status_code=404, detail=f"Resource doesn't exist")
    db.delete(obj)
    db.commit()
    return True


def update_object_by_id(
        cls,
        id: str,
        update_data: Dict[str, Any],
        db: Session = Depends(get_db)
        ) -> Dict:
    """Updates an object in the database by its ID"""
    obj = db.query(cls).filter(cls.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail=f"Resource doesn't exist")

    for key, value in update_data.items():
        if hasattr(obj, key):
            setattr(obj, key, value)

    db.commit()
    db.refresh(obj)
    return obj

def update_object_by_user_id(
        cls,
        user_id: str,
        update_data: Dict[str, Any],
        db: Session = Depends(get_db)
        ) -> Dict:
    """Updates an object in the database by its ID"""
    obj = db.query(cls).filter(cls.user_id == user_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail=f"Resource doesn't exist")

    for key, value in update_data.items():
        if hasattr(obj, key):
            setattr(obj, key, value)

    db.commit()
    db.refresh(obj)
    return obj



def create_object(
        cls,
        obj_data: Dict[str, Any],
        db: Session = Depends(get_db)
        ) -> Dict:
    """Creates a new object in the database"""
    obj = cls(**obj_data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_all_objects(
    cls,
    db: Session = Depends(get_db)
    ):
    """Retrieves all objects in a class db model"""
    objects = db.query(cls).all()
    if not objects:
        raise HTTPException(
            status_code=404,
            detail="There are no objects found"
        )
    return objects


def get_user_email(user_id: str, db: Session = Depends(get_db)) -> str:
    """Retrieves user email"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    user_email = user.to_dict().get('email')
    if not user_email:
        raise HTTPException(
            status_code=404,
            detail="No email found"
        )
    return user_email
