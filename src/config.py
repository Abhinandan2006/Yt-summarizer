"""Configuration management using Pydantic Settings."""

from pathlib import Path
from typing import List, Literal
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application runtime settings loaded from environment or .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Environment
    ENVIRONMENT: Literal["development", "production", "test"] = "development"
    LOG_LEVEL: str = "INFO"

    # API Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    # LLM Settings
    DEFAULT_LLM_PROVIDER: Literal["gemini", "openai"] = "gemini"
    GEMINI_API_KEY: str = Field(default="")
    GEMINI_MODEL: str = "gemini-2.0-flash"

    OPENAI_API_KEY: str = Field(default="")
    OPENAI_MODEL: str = "gpt-4o-mini"

    # Embeddings
    EMBEDDING_PROVIDER: Literal["local", "openai", "gemini"] = "local"
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"

    # Storage Paths
    VECTOR_STORE_PATH: Path = Path("./data/vector_store")
    CACHE_DB_PATH: Path = Path("./data/cache/yt_rag.db")
    TEMP_AUDIO_PATH: Path = Path("./data/temp_audio")

    # Ingestion & Chunking
    CHUNK_DURATION_SEC: int = 75
    CHUNK_OVERLAP_SEC: int = 15
    MIN_CHUNK_CHARACTERS: int = 80

    # Whisper Fallback
    WHISPER_MODEL_SIZE: str = "base"
    WHISPER_DEVICE: str = "cpu"
    WHISPER_COMPUTE_TYPE: str = "int8"

    def ensure_directories(self) -> None:
        """Ensures that configured persistent directories exist on disk."""
        self.VECTOR_STORE_PATH.mkdir(parents=True, exist_ok=True)
        self.CACHE_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        self.TEMP_AUDIO_PATH.mkdir(parents=True, exist_ok=True)


# Singleton configuration instance
settings = Settings()
settings.ensure_directories()

