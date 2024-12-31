import boto3
from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException, Query, Path
from core.config import settings
from utils.logging_helper import logger
from typing import Optional


router = APIRouter(prefix='/api')

FILE_TYPE_TO_EXTENSION = {
    "image/jpeg": [".jpg", ".jpeg"],
    "image/png": [".png"],
    "image/webp": [".webp"],
    "application/pdf": [".pdf"]
}

def validate_file_extension(file_name: str, file_type: str):
    """
    Validates that the file_name extension matches the provided file_type.
    """
    valid_extensions = FILE_TYPE_TO_EXTENSION.get(file_type)
    if not valid_extensions:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    
    if not any(file_name.lower().endswith(ext) for ext in valid_extensions):
        raise HTTPException(
            status_code=400,
            detail=f"File extension does not match file type '{file_type}'. Expected extensions: {valid_extensions}"
        )


s3_client = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION
)


@router.get("/generate-upload-url/{user_id}")
async def generate_upload_url(
    file_name: str = Query(..., min_length=1, max_length=255, regex=r"^[a-zA-Z0-9._-]+$"),
    file_type: str = Query(..., regex=r"^(image/(jpeg|png|webp)|application/pdf)$"),
    user_id: str = Path(..., min_length=1, max_length=255, regex=r"^[a-zA-Z0-9_-]+$"),
    document_type: Optional[str] = Query(None, regex="^(profile_pic|government_id|certifications|selfie|proof_of_res)$")
    ):
    """Generates a signed url for uploading to S3"""
    validate_file_extension(file_name, file_type)

    bucket_name = settings.S3_BUCKET_NAME
    if document_type == 'profile_pic' or file_type.startswith("image/"):
        folder = "profile-pictures/"
    elif document_type in [
        'government_id', 'certifications', 'selfie', 'proof_of_res'
    ] or file_type == "application/pdf":
        folder = "verification-docs/"
    else:
        raise HTTPException(status_code=400, detail="Unsupported document or file type")

    if document_type:
        sanitized_file_name = f"{user_id}-{document_type}.{file_name.split('.')[-1]}"
    else:
        sanitized_file_name = f"{user_id}-{file_name}"
    s3_key = f"{folder}{sanitized_file_name}"
    try:
        signed_url = s3_client.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": bucket_name,
                "Key": s3_key,
                "ContentType": file_type
            },
            ExpiresIn=3600
        )
        logger.info(f"Generated signed URL for profile_id={user_id}, key={s3_key}")
        return {
            "upload_url": signed_url,
            "file_path": s3_key
            }
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))
    



