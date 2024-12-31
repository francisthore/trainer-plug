from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from core.config import settings


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def hash_password(raw_password):
    """Hashes a password from plain text"""
    hashed = pwd_context.hash(raw_password)
    return hashed


def verify_password(raw: str, hashed: str) -> bool:
    """Verifies the given password"""
    return pwd_context.verify(raw, hashed)


def create_access_token(data: dict) -> str:
    """Generates an access tokem"""
    to_encode = data.copy()
    expire = datetime.now() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )
    return encoded_jwt


def create_refresh_token(data: dict) -> str:
    """Generates a refresh token"""
    to_encode = data.copy()
    expire = datetime.now() + timedelta(
        seconds=settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.REFRESH_SECRET_KEY, algorithm=settings.ALGORITHM
        )
    return encoded_jwt


def decode_token(token: str, secret_key:  str) -> dict:
    """Decodes a JWT token"""
    try:
        payload = jwt.decode(
            token, secret_key, algorithms=[settings.ALGORITHM]
            )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def verify_access_token(token: str):
    """Verifys an access token and returns its payload"""
    return decode_token(token, settings.SECRET_KEY)


def verify_refresh_token(token: str):
    """Verifys refresh token"""
    return decode_token(token, settings.REFRESH_SECRET_KEY)


def get_current_user(request: Request):
    """Dependency to get the current user from the token"""
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload


def generate_verification_link(username: str) -> str:
    """
    Generates a user email verification link

    Args:
        username (str): user

    Returns:
        str: verification link
    """
    token = create_access_token({'sub': username, 'exp': 3600})
    return f"{settings.FRONTEND_URL}/api/auth/verify-email?token={token}"
