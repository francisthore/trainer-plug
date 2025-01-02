from pydantic_settings import BaseSettings


class Setings(BaseSettings):
    """
        Settings class that helps me with env imports
    """

    DATABASE_URL: str
    FRONTEND_URL: str
    FRONTEND_URL2: str
    SECRET_KEY: str
    REFRESH_SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int
    TIMEOUT: int
    MAIL_API_KEY: str
    FROM_MAIL: str
    FROM_NAME: str
    BASE_PROFILE_PIC: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    S3_BUCKET_NAME: str

    class Config:
        env_file = '.env'


settings = Setings()
