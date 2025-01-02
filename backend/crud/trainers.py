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
        Trainer.hourly_rate
    ).join(Profile, Trainer.user_id == Profile.user_id).filter(Trainer.verification_status == "Verified").all()

    return query
