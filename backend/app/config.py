from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    openai_api_key: str = Field(default="")
    openai_model: str = Field(default="gpt-5-mini")

    cors_origin_list: list[str] = [
        "http://localhost:4200",
        "http://localhost:5400"
    ]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


@lru_cache
def get_settings():
    return Settings()