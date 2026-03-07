"""
Security and logging configuration models.
"""

from typing import Any

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from ...structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class SecurityConfig(BaseSettings):
    """Security-sensitive configuration."""

    admin_password: str = Field(..., description="Admin password (required)")
    invite_codes_file: str = Field(default="invites.json", description="Invite codes file path")

    @field_validator("admin_password")
    @classmethod
    def validate_admin_password(cls, v: str) -> str:
        """Validate admin password strength (production only)."""
        logger.debug("Validating admin password strength", password_length=len(v))
        if len(v) < 8:
            logger.error("Admin password validation failed - too short", password_length=len(v), minimum_length=8)
            raise ValueError("Admin password must be at least 8 characters")
        logger.debug("Admin password validation successful", password_length=len(v))
        return v

    model_config = SettingsConfigDict(env_prefix="MYTHOSMUD_", case_sensitive=False, extra="ignore")


class LoggingConfig(BaseSettings):
    """Logging configuration."""

    environment: str = Field(..., description="Logging environment (required)")
    level: str = Field(default="INFO", description="Log level")
    format: str = Field(default="colored", description="Log format")
    log_base: str = Field(default="logs", description="Base log directory")
    rotation_max_size: str = Field(default="100MB", description="Log rotation max size")
    rotation_backup_count: int = Field(default=5, description="Number of backup log files")
    compression: bool = Field(default=True, description="Enable log compression")
    disable_logging: bool = Field(default=False, description="Disable all logging")

    @field_validator("environment")
    @classmethod
    def validate_environment(cls, v: str) -> str:
        """Validate logging environment."""
        logger.debug("Validating logging environment", environment=v)
        valid_environments = ["local", "unit_test", "e2e_test", "production"]
        if v not in valid_environments:
            logger.error("Invalid logging environment", environment=v, valid_environments=valid_environments)
            raise ValueError(f"Environment must be one of {valid_environments}, got '{v}'")
        logger.debug("Logging environment validation successful", environment=v)
        return v

    @field_validator("level")
    @classmethod
    def validate_level(cls, v: str) -> str:
        """Validate log level."""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        v_upper = v.upper()
        if v_upper not in valid_levels:
            raise ValueError(f"Log level must be one of {valid_levels}, got '{v}'")
        return v_upper

    @field_validator("format")
    @classmethod
    def validate_format(cls, v: str) -> str:
        """Validate log format."""
        valid_formats = ["json", "human", "colored"]
        if v not in valid_formats:
            raise ValueError(f"Log format must be one of {valid_formats}, got '{v}'")
        return v

    model_config = SettingsConfigDict(env_prefix="LOGGING_", case_sensitive=False, extra="ignore")

    def to_legacy_dict(self) -> dict[str, Any]:
        """
        Convert to legacy logging config dict format for backward compatibility.

        Returns a dict with the structure expected by logging_config.py
        """
        return {
            "environment": self.environment,
            "level": self.level,
            "format": self.format,
            "log_base": self.log_base,
            "rotation": {
                "max_size": self.rotation_max_size,
                "backup_count": self.rotation_backup_count,
            },
            "compression": self.compression,
            "disable_logging": self.disable_logging,
        }
