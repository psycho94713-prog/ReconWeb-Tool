from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Advanced Website OSINT Framework"
    VERSION: str = "1.0.0"
    DEBUG: bool = True

    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()