import yaml
from pydantic_settings import BaseSettings
from pydantic import HttpUrl
import os

class Settings(BaseSettings):
    SENTRY_DSN: HttpUrl | None = None
    ENV: str | None = None
    LOGGER_CONFIG_PATH: str = f"{os.getcwd()}/src/common/logger/logging_config.yaml"

    class Config:
        case_sensitive = True

def read_yaml(file_path: str) -> Settings:
    with open(file_path) as stream:
        config = yaml.safe_load(stream)

    return Settings(**config)