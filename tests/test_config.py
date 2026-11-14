"""Unit tests for application configuration."""

from src.config import Settings


def test_settings_initialization():
    settings = Settings(
        ENVIRONMENT="test",
        DEFAULT_LLM_PROVIDER="gemini",
        CHUNK_DURATION_SEC=90,
    )
    assert settings.ENVIRONMENT == "test"
    assert settings.DEFAULT_LLM_PROVIDER == "gemini"
    assert settings.CHUNK_DURATION_SEC == 90
    assert settings.VECTOR_STORE_PATH.exists()
    assert settings.CACHE_DB_PATH.parent.exists()

