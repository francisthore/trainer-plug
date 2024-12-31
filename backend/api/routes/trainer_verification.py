from fastapi import APIRouter, HTTPException, Depends, UploadFile, Query, File
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.models.trainer_verification import TrainerVerification
from db.models.trainers import Trainer
from db.session import get_db
from schemas.trainer_verification import (
    TrainerVerificationCreate,
    TrainerVerificationUpdate,
    TrainerVerificationResponse
    )
from crud.db_hepers import (
    get_object_by_id,
    get_object_by_user_id
    )
import requests
from api.routes.upload_router import (
    FILE_TYPE_TO_EXTENSION,
    validate_file_extension,
    generate_upload_url
    )
from datetime import datetime

router = APIRouter(prefix='/api/verification')


@router.post('/trainer-verifications', response_model=TrainerVerificationResponse, status_code=201)
async def create_trainer_verification(
    data: TrainerVerificationCreate, db: Session = Depends(get_db)
    ):
    """Creates a verification record for a trainer"""
    data = data.model_dump()
    existing_record = db.query(TrainerVerification).filter(TrainerVerification.user_id == data.get('user_id')).first()
    if existing_record:
        raise HTTPException(
            status_code=400,
            detail='Verification record already exists.'
        )
    verification = TrainerVerification(**data)
    db.add(verification)
    db.commit()
    db.refresh(verification)
    return TrainerVerificationResponse.model_validate(verification)


@router.patch('/trainer-verifications/{user_id}', response_model=TrainerVerificationResponse)
async def update_trainer_verification(
    user_id: str, data: TrainerVerificationUpdate,
    db: Session = Depends(get_db)
    ):
    """Updates a trainer verification"""
    verification = get_object_by_user_id(
        TrainerVerification,
        user_id,
        db)
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(verification, key, value)
    
    db.commit()
    db.refresh(verification)

    return TrainerVerificationResponse.model_validate(verification)


@router.get('/trainer-verifications/{user_id}', response_model=TrainerVerificationResponse)
async def get_trainer_verification(
    user_id: str, db: Session = Depends(get_db)
    ):
    """Retrieves a trainer verification record"""
    verification = get_object_by_user_id(
        TrainerVerification,
        user_id,
        db)
    return TrainerVerificationResponse.model_validate(verification)


@router.patch('/trainer-veficications/verify/{user_id}')
async def verify_trainer(user_id: str, db: Session = Depends(get_db)):
    """Verifies a trainer record"""
    verification = get_object_by_user_id(
        TrainerVerification, user_id, db
    )
    verification.verified_at = datetime.now()
    trainer = get_object_by_user_id(
        Trainer, user_id, db
    )
    trainer.verification_status = 'Verified'
    db.commit()

    return JSONResponse(
        status_code=200,
        content={
            'success': True,
            'message': 'Trainer successfully verified'
        }
    )


@router.patch("/upload-verification-document/{user_id}")
async def upload_verification_document(
    user_id: str,
    document_type: str = Query(..., regex="^(government_id|certifications|selfie|proof_of_res)$"),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """
    Uploads a verification document to S3
    and updates the trainer's verification record.
    """
    if file.content_type not in FILE_TYPE_TO_EXTENSION:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    
    validate_file_extension(file.filename, file.content_type)

    upload_url_response = await generate_upload_url(
        file_name=file.filename, file_type=file.content_type, user_id=user_id, document_type=document_type
    )
    upload_url = upload_url_response.get("upload_url")
    file_path = upload_url_response.get("file_path")

    try:
        file_content = await file.read()
        headers = {"Content-Type": file.content_type}
        upload_response = requests.put(upload_url, data=file_content, headers=headers)
        if upload_response.status_code != 200:
            raise HTTPException(
                status_code=upload_response.status_code,
                detail="Failed to upload to S3"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error uploading file: {str(e)}"
        )
    
    verification = db.query(TrainerVerification).filter(
        TrainerVerification.user_id == user_id
    ).first()

    if not verification:
        raise HTTPException(status_code=404, detail="Trainer verification record not found")

    if document_type == "government_id":
        verification.government_id_url = file_path
    elif document_type == "certifications":
        verification.certifications_url = file_path
    elif document_type == "selfie":
        verification.selfie_url = file_path
    elif document_type == "proof_of_res":
        verification.proof_of_res_url = file_path

    db.commit()
    db.refresh(verification)

    return {
        "success": True,
        "message": f"{document_type.replace('_', ' ').capitalize()} uploaded successfully.",
        "file_path": file_path,
    }

