from pydantic import BaseSettings


class Settings(BaseSettings):
    # DB_HOST: str = "localhost"
    # DB_PORT: int = 3306
    # DB_USER: str = "api"
    # DB_PASSWORD: str = "api"
    # DB: str = "api"

    class Config:
        env_file = ".env"


settings = Settings()
