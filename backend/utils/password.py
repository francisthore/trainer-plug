from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def hash_password(raw_password):
    """Hashes a password from plain text"""
    hashed = pwd_context.hash(raw_password)
    return hashed

def verify_password(raw, hashed):
    """Verifys the given password"""
    return pwd_context(raw, hashed)
