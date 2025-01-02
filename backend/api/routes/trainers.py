from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.trainers import Trainer
from db.models.users import User
from schemas.trainers import (
    TrainerCreate,
    TrainerResponse,
    TrainerUpdate,
    TrainerFullResponse
    )
from typing import List
from utils.auth import get_current_user, oauth2_scheme
from utils.logging_helper import logger
from crud.db_hepers import(
    delete_object_by_user_id,
    get_object_by_user_id,
    create_object, update_object_by_user_id, get_all_objects
    )
from crud.trainers import get_full_trainer_profiles
from typing import List



router = APIRouter(prefix='/api/trainers', redirect_slashes=False)

@router.post('/', response_model=TrainerResponse, status_code=201)
async def create_trainer(
    trainer: TrainerCreate,
    db: Session = Depends(get_db)
    ):
    """Creates a new trainer"""
    create_data = trainer.model_dump()
    trainer = create_object(Trainer, create_data, db)
    logger.info(f"New trainer profile created for User: {trainer.user_id}")
    return TrainerResponse.model_validate(trainer)



@router.get('/', response_model=List[TrainerFullResponse])
async def get_trainers(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    """Retrieves all trainers"""
    trainers = get_full_trainer_profiles(db)
    return [
        TrainerFullResponse(
            user_id=trainer.user_id,
            full_name=trainer.full_name,
            bio=trainer.bio,
            profile_picture=trainer.profile_picture,
            hourly_rate=trainer.hourly_rate
        )
        for trainer in trainers
    ]

@router.get('/{user_id}', response_model=TrainerResponse)
async def get_trainer(
    user_id: str, db: Session = Depends(get_db)
    ):
    """Retrieves a trainer"""
    trainer = get_object_by_user_id(Trainer, user_id, db)
    return TrainerResponse.model_validate(trainer)


@router.patch('/{user_id}', response_model=TrainerResponse)
async def update_trainer_route(
    user_id: str, data: TrainerUpdate, db: Session = Depends(get_db)
    ):
    """Updates a trainer profile"""
    update_data = data.model_dump(exclude_unset=True)
    updated_trainer = update_object_by_user_id(
        Trainer, user_id, update_data, db
    )
    return TrainerResponse.model_validate(updated_trainer)


@router.delete('/{user_id}')
async def delete_trainer(
    user_id: str, db: Session = Depends(get_db)):
    """Deletes a trainer"""
    if delete_object_by_user_id(Trainer, user_id, db):
        logger.info(f"Trainer with id: {user_id} deleted successfully")
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "Successfully deleted trainer"
            }
            )
