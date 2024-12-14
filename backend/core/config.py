from pydantic_settings import BaseSettings


class Setings(BaseSettings):
    """
        Settings class that helps me with env imports
    """

    DATABASE_URL: str
    FRONTEND_URL: str
    SECRET_KEY: str
    REFRESH_SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int
    TIMEOUT: int
    MAIL_API_KEY: str


    class Config:
        env_file = '.env'


settings = Setings()
