from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from fastapi.responses import JSONResponse
from db.models.profile import Profile
from db.session import get_db
from schemas.profiles import ProfileCreate, ProfileResponse, ProfileUpdate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .upload_router import generate_upload_url
from utils.auth import get_current_user
from crud.db_hepers import (
    create_object,
    get_object_by_id,
    get_object_by_user_id,
    update_object_by_user_id,
    delete_object_by_id)
from utils.logging_helper import logger
import requests


router = APIRouter(prefix='/api/profiles')


@router.post('/', response_model=ProfileResponse, status_code=201)
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


@router.get('/{user_id}', response_model=ProfileResponse)
async def retrieve_profile(user_id: str, db: Session = Depends(get_db)):
    """retrieves a single profile"""
    if not user_id:
        raise ValueError("Profile id is required")
    db_profile = get_object_by_user_id(Profile, user_id, db)
    return ProfileResponse.model_validate(db_profile)


@router.patch('/{id}', response_model=ProfileResponse)
async def update_user_profile(
    id: str, profile: ProfileUpdate, db: Session = Depends(get_db)
    ):
    """Updates a user profile"""
    profile_data = profile.model_dump(exclude_unset=True)
    updated_profile = update_object_by_user_id(Profile, id, profile_data, db)

    return ProfileResponse.model_validate(updated_profile)


@router.delete('/{id}')
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


@router.patch('/update-profile-picture/{user_id}')
async def update_profile_picture(
    user_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
    ):
    """updates user profile picture"""
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400, detail="Only images are allowed"
        )
    upload_url_response = await generate_upload_url(
        file_name=file.filename, file_type=file.content_type,
        user_id=user_id, document_type="profile_pic"
    )
    upload_url = upload_url_response.get("upload_url")
    file_path = upload_url_response.get('file_path')
    try:
        file_content = await file.read()
        headers = {"Content-Type": file.content_type}
        upload_response = requests.put(
            upload_url, data=file_content, headers=headers
            )
        if upload_response.status_code != 200:
            raise HTTPException(
                status_code=upload_response.status_code,
                detail="Failed to upload to s3"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error uploading file: {str(e)}"
        )
    
    profile = get_object_by_user_id(Profile, user_id, db)
    profile.profile_picture = file_path
    db.commit()

    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "message": "Profile picture uploaded successfully"
        }
    )
