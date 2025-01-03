from sqlalchemy.orm import Session
from db.models.trainers import Trainer
from db.models.profile import Profile


def get_full_trainer_profiles(db: Session):
    """Fetch trainers with full profiles"""
    query = db.query(
        Trainer.user_id,
        Profile.full_name,
        Profile.bio,
        Profile.profile_picture,
        Trainer.hourly_rate,
        Trainer.specialization,
        Trainer.years_of_experience
    ).join(Profile, Trainer.user_id == Profile.user_id).filter(Trainer.verification_status == "Verified").all()

    return query


def get_full_trainer_profile(db: Session, user_id: str):
    """Fetch trainers with full profiles"""
    query = db.query(
        Trainer.user_id,
        Profile.full_name,
        Profile.bio,
        Profile.profile_picture,
        Trainer.hourly_rate,
        Trainer.specialization,
        Trainer.years_of_experience
    ).join(Profile, Trainer.user_id == Profile.user_id).filter(Trainer.verification_status == "Verified" and Trainer.user_id == user_id).first()

    return query
