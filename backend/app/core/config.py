from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str = (
        "postgresql://postgres:postgres@localhost:5432/aetheros"
    )

    OPENAI_API_KEY: str = ""

    REDIS_HOST: str = "localhost"

    REDIS_PORT: int = 6379

    REDIS_URL: str = (
        "redis://localhost:6379/0"
    )

    class Config:
        env_file = ".env"


settings = Settings()

print(settings.DATABASE_URL)