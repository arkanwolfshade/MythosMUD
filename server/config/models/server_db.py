"""
Server and database configuration models.
"""

from typing import Any

from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from ...structured_logging.enhanced_logging_config import get_logger
from ._helpers import _apply_url_fallback

logger = get_logger(__name__)


class ServerConfig(BaseSettings):
    """Server network configuration."""

    host: str = Field(default="127.0.0.1", description="Server bind address")
    port: int = Field(..., description="Server port (required)")

    @field_validator("port")
    @classmethod
    def validate_port(cls, v: int) -> int:
        """Validate port is in valid range."""
        logger.debug("Validating server port", port=v)
        if not 1024 <= v <= 65535:
            logger.error("Invalid server port", port=v, valid_range="1024-65535")
            raise ValueError("Port must be between 1024 and 65535")
        logger.debug("Server port validation successful", port=v)
        return v

    model_config = SettingsConfigDict(env_prefix="SERVER_", case_sensitive=False, extra="ignore")


class DatabaseConfig(BaseSettings):
    """Database configuration."""

    url: str = Field(..., description="Primary database URL (required)")
    npc_url: str = Field(..., description="NPC database URL (required)")

    # Connection pool configuration (SQLAlchemy)
    pool_size: int = Field(default=5, description="Number of connections to maintain in pool")
    max_overflow: int = Field(default=10, description="Additional connections that can be created beyond pool_size")
    pool_timeout: int = Field(default=30, description="Seconds to wait for connection from pool")

    # AsyncPG connection pool configuration
    asyncpg_pool_min_size: int = Field(default=1, description="Minimum connections in asyncpg pool")
    asyncpg_pool_max_size: int = Field(default=10, description="Maximum connections in asyncpg pool")
    asyncpg_command_timeout: int = Field(default=60, description="Command timeout for asyncpg operations (seconds)")

    @field_validator("url", "npc_url")
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        """Validate database URL format - PostgreSQL only."""
        logger.debug("Validating database URL", url_length=len(v) if v else 0)
        if not v:
            logger.error("Database URL validation failed - empty URL")
            raise ValueError("Database URL cannot be empty")
        # PostgreSQL only - SQLite is no longer supported
        if not v.startswith("postgresql"):
            logger.error(
                "Database URL validation failed - invalid protocol",
                url_preview=v[:50] if len(v) > 50 else v,
                expected_protocol="postgresql",
            )
            raise ValueError("Database URL must start with 'postgresql'. SQLite is no longer supported.")
        logger.debug("Database URL validation successful", url_preview=v[:50] if len(v) > 50 else v)
        return v

    @field_validator(
        "pool_size",
        "max_overflow",
        "pool_timeout",
        "asyncpg_pool_min_size",
        "asyncpg_pool_max_size",
        "asyncpg_command_timeout",
    )
    @classmethod
    def validate_pool_config(cls, v: int) -> int:
        """Validate pool configuration values are positive."""
        if v < 1:
            raise ValueError("Pool configuration values must be at least 1")
        return v

    @model_validator(mode="before")
    @classmethod
    def ensure_url_set(cls, data: Any) -> Any:
        """
        Ensure url is set - use npc_url as fallback if url is missing.

        This handles cases where DatabaseConfig is instantiated with only npc_url
        (e.g., from environment variables where DATABASE_URL might not be set but
        DATABASE_NPC_URL is). In such cases, we use npc_url as the url value.
        """
        if isinstance(data, dict):
            _apply_url_fallback(data)
        return data

    model_config = SettingsConfigDict(env_prefix="DATABASE_", case_sensitive=False, extra="ignore")
