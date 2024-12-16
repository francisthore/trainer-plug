from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.models.trainers import Trainer
from schemas.trainers import TrainerCreate, TrainerUpdate, TrainerDelete
from utils.logging_helper import logger
from .db_hepers import get_object_by_id


def create_new_trainer(db: Session, trainer: TrainerCreate):
    """Creates a new trainer and store in the db"""
    try:
        new_trainer = Trainer(
        user_id=trainer.user_id,
        specialization=trainer.specialization,
        years_of_experience=trainer.years_of_experience,
        hourly_rate=trainer.hourly_rate,
        verification_status=trainer.verification_status
        )
        db.add(new_trainer)
        db.commit()
        db.refresh(new_trainer)
        return new_trainer
    except IntegrityError as e:
        raise ValueError("Personal Trainer already exists")
    

def update_trainer(trainer_id: str, trainer: TrainerUpdate, db: Session):
    """Updates a trainer"""
    if not trainer_id:
        raise ValueError("Trainer user_id is required")
    db_trainer = get_object_by_id(Trainer, trainer_id, db)
    if trainer.specialization is not None:
        db_trainer.specialization = trainer.specialization
    if trainer.years_of_experience is not None:
        db_trainer.years_of_experience = trainer.years_of_experience
    if trainer.hourly_rate is not None:
        db_trainer.hourly_rate = trainer.hourly_rate
    if trainer.verification_status is not None:
        db_trainer.verification_status = trainer.verification_status
    db.commit()
    db.refresh(db_trainer)
    logger.info(
        f"Trainer updated: id={db_trainer.id}, updated_fields={trainer.model_dump(exclude_unset=True)}"
    )
    return db_trainer
