from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.trainers import Trainer
from schemas.trainers import TrainerCreate, TrainerResponse, TrainerUpdate, TrainerDelete
from typing import List
from utils.auth import get_current_user
from utils.logging_helper import logger
from crud.trainers import create_new_trainer, update_trainer
from crud.db_hepers import get_object_by_id, delete_object_by_id



router = APIRouter(prefix='/api')

@router.post('/trainers', response_model=TrainerResponse, status_code=201)
async def create_trainer(
    trainer: TrainerCreate,
    db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)
    ):
    """Creates a new trainer"""
    trainer = create_new_trainer(db, trainer)
    logger.info(f"New trainer profile created for User: {trainer.user_id}")
    return TrainerResponse.model_validate(trainer)


@router.get('/trainers', response_model=TrainerResponse)
async def get_trainer(
    trainer_id: str, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
    ):
    """Retrieves a trainer"""
    trainer = get_object_by_id(Trainer, trainer_id, db)
    return TrainerResponse.model_validate(trainer)


@router.patch('/trainers', response_model=TrainerResponse)
async def update_trainer_route(
    trainer_id: str, trainer: TrainerUpdate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
    ):
    """Updates a trainer profile"""
    updated_trainer = update_trainer(trainer_id, trainer, db)
    return TrainerResponse.model_validate(updated_trainer)


@router.delete('/trainers')
async def delete_trainer(
    trainer: TrainerDelete, db: Session = Depends(get_db)):
    """Deletes a trainer"""
    if delete_object_by_id(Trainer, trainer.id, db):
        logger.info(f"Trainer with id: {trainer.id} deleted successfully")
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "Successfully deleted trainer"
            }
            )
