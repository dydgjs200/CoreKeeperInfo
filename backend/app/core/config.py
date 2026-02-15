from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Core Keeper Info API"
    DEBUG: bool = True
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/corekeeper"
    API_V1_PREFIX: str = "/api/v1"
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]

    model_config = {"env_file": ".env"}


settings = Settings()
