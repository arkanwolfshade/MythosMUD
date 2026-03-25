"""
Chat and time configuration models.
"""

from datetime import UTC, datetime

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class ChatConfig(BaseSettings):
    """Chat system configuration."""

    # Rate limiting per channel (messages per minute)
    rate_limit_global: int = Field(default=10, description="Global channel rate limit")
    rate_limit_local: int = Field(default=20, description="Local channel rate limit")
    rate_limit_say: int = Field(default=15, description="Say channel rate limit")
    rate_limit_party: int = Field(default=30, description="Party channel rate limit")
    rate_limit_whisper: int = Field(default=5, description="Whisper channel rate limit")

    # Content filtering
    content_filtering_enabled: bool = Field(default=True, description="Enable content filtering")
    profanity_filter: bool = Field(default=True, description="Enable profanity filter")
    keyword_detection: bool = Field(default=True, description="Enable keyword detection")

    # Message history
    message_history_enabled: bool = Field(default=True, description="Enable message history")
    message_retention_days: int = Field(default=30, description="Message retention in days")
    max_messages_per_channel: int = Field(default=1000, description="Max messages per channel")

    @field_validator(
        "rate_limit_global",
        "rate_limit_local",
        "rate_limit_say",
        "rate_limit_party",
        "rate_limit_whisper",
    )
    @classmethod
    def validate_rate_limits(cls, v: int) -> int:
        """Validate rate limits are reasonable."""
        if v < 1 or v > 1000:
            raise ValueError("Rate limit must be between 1 and 1000 messages per minute")
        return v

    model_config = SettingsConfigDict(env_prefix="CHAT_", case_sensitive=False, extra="ignore")


class TimeConfig(BaseSettings):
    """Temporal compression configuration for the MythosChronicle."""

    compression_ratio: float = Field(default=4.0, description="Mythos hours per real hour")
    real_epoch_utc: datetime = Field(
        default_factory=lambda: datetime(2025, 1, 1, tzinfo=UTC),
        description="Reference UTC timestamp anchoring real time calculations",
    )
    mythos_epoch: datetime = Field(
        default_factory=lambda: datetime(1920, 1, 1, tzinfo=UTC),
        description="Reference Mythos timestamp paired with the real epoch (uses real-world Gregorian calendar)",
    )
    state_file: str = Field(
        default="data/system/time_state.json",
        description="Filesystem path used to persist the chronicle state between restarts",
    )

    @field_validator("compression_ratio")
    @classmethod
    def validate_compression_ratio(cls, value: float) -> float:
        """Ensure we never divide by zero or run the chronicle backward."""
        if value <= 0:
            raise ValueError("compression_ratio must be greater than zero")
        return value

    model_config = SettingsConfigDict(env_prefix="TIME_", case_sensitive=False, extra="ignore")
