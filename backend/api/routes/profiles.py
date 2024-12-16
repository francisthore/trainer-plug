from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from db.models.profile import Profile
from db.session import get_db
from schemas.profiles import ProfileCreate, ProfileResponse, ProfileUpdate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from utils.auth import get_current_user
from crud.db_hepers import (
    create_object,
    get_object_by_id,
    update_object_by_id,
    delete_object_by_id)
from utils.logging_helper import logger


router = APIRouter(prefix='/api')


@router.post('/profiles', response_model=ProfileResponse, status_code=201)
async def create_new_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db)
    ):
    """Creates a new profile"""
    try:
        from db.models.users import User        
        profile_data = profile.model_dump()
        if get_object_by_id(User, profile_data.get("user_id"), db):
            new_profile = create_object(Profile, profile_data, db)
            return ProfileResponse.model_validate(new_profile)
    except IntegrityError as e:
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": "Profile already exists for user"
            }
        )
    except Exception as e:
        raise HTTPException(status_code=404, detail="not found")


@router.get('/profiles/{id}', response_model=ProfileResponse)
async def retrieve_profile(id: str, db: Session = Depends(get_db)):
    """retrieves a single profile"""
    if not id:
        raise ValueError("Profile id is required")
    db_profile = get_object_by_id(Profile, id, db)
    return ProfileResponse.model_validate(db_profile)


@router.patch('/profiles/{id}', response_model=ProfileResponse)
async def update_user_profile(
    id: str, profile: ProfileUpdate, db: Session = Depends(get_db)
    ):
    """Updates a user profile"""
    profile_data = profile.model_dump(exclude_unset=True)
    updated_profile = update_object_by_id(Profile, id, profile_data, db)

    return ProfileResponse.model_validate(updated_profile)


@router.delete('/profiles/{id}')
async def delete_profile(id: str, db: Session = Depends(get_db)):
    """Deletes a profile"""
    if delete_object_by_id(Profile, id, db):
        logger.info(f"Profle with id: {id} deleted successfully")
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "Successfully deleted profile"
            }
            )
