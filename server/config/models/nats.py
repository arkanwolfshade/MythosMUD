"""
NATS messaging configuration model.
"""

from typing import Any

from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from ...structured_logging.enhanced_logging_config import get_logger
from ._helpers import _validate_tls_files_and_maybe_update_url

logger = get_logger(__name__)


class NATSConfig(BaseSettings):
    """NATS messaging configuration."""

    enabled: bool = Field(default=True, description="Enable NATS messaging")
    url: str = Field(default="nats://localhost:4222", description="NATS server URL")
    max_payload: int = Field(default=1048576, description="Maximum message payload size (1MB)")
    reconnect_time_wait: int = Field(default=1, description="Reconnect wait time in seconds")
    max_reconnect_attempts: int = Field(default=5, description="Maximum reconnection attempts")
    connect_timeout: int = Field(default=5, description="Connection timeout in seconds")
    ping_interval: int = Field(default=30, description="Ping interval in seconds")
    max_outstanding_pings: int = Field(default=5, description="Maximum outstanding pings")

    # Connection health monitoring
    health_check_interval: int = Field(default=30, description="Health check interval in seconds")

    # Connection pooling configuration
    connection_pool_size: int = Field(default=5, description="Number of connections in pool")
    pool_wait_timeout: float = Field(
        default=10.0,
        description="Seconds to wait for an available pool connection when exhausted before raising",
    )
    enable_connection_pooling: bool = Field(default=True, description="Enable connection pooling")

    # Message batching configuration
    batch_size: int = Field(default=100, description="Maximum messages per batch")
    batch_timeout: float = Field(default=0.1, description="Batch timeout in seconds")
    enable_message_batching: bool = Field(default=True, description="Enable message batching")
    max_batch_retries: int = Field(default=3, description="Maximum retry attempts for failed batch groups")

    # Subject validation configuration
    enable_subject_validation: bool = Field(default=True, description="Enable NATS subject validation")
    strict_subject_validation: bool = Field(
        default=False, description="Enable strict subject validation (reject invalid subjects)"
    )

    # Message acknowledgment configuration
    manual_ack: bool = Field(default=False, description="Enable manual message acknowledgment (ack/nak)")

    # Optional NATS server authentication (NATS_USER, NATS_PASSWORD, or NATS_TOKEN)
    user: str | None = Field(default=None, description="NATS auth username (optional)")
    password: str | None = Field(default=None, description="NATS auth password (optional)")
    token: str | None = Field(default=None, description="NATS auth token (optional; alternative to user/password)")

    # TLS/SSL configuration
    tls_enabled: bool = Field(default=False, description="Enable TLS/SSL encryption for NATS connections")
    tls_cert_file: str | None = Field(default=None, description="Path to TLS certificate file (.crt)")
    tls_key_file: str | None = Field(default=None, description="Path to TLS private key file (.key)")
    tls_ca_file: str | None = Field(default=None, description="Path to TLS CA certificate file for verification")
    tls_verify: bool = Field(default=True, description="Verify TLS certificates (set False for self-signed certs)")

    @field_validator("tls_cert_file", "tls_key_file", "tls_ca_file")
    @classmethod
    def validate_tls_files(cls, v: str | None, info: Any) -> str | None:
        """Validate TLS file paths exist when TLS is enabled."""
        if v is not None:
            from pathlib import Path

            file_path = Path(v)
            if not file_path.exists():
                logger.warning("TLS file path does not exist", file_path=str(file_path), field=info.field_name)
        return v

    @model_validator(mode="after")
    def validate_tls_config(self) -> "NATSConfig":
        """Validate TLS configuration is complete when enabled."""
        if self.tls_enabled:
            _validate_tls_files_and_maybe_update_url(self)
        return self

    @field_validator("max_payload")
    @classmethod
    def validate_max_payload(cls, v: int) -> int:
        """Validate max payload is reasonable."""
        if v < 1024 or v > 10485760:  # 1KB to 10MB
            raise ValueError("Max payload must be between 1KB and 10MB")
        return v

    @field_validator("connect_timeout", "ping_interval")
    @classmethod
    def validate_positive(cls, v: int) -> int:
        """Validate value is positive."""
        if v <= 0:
            raise ValueError("Value must be positive")
        return v

    model_config = SettingsConfigDict(env_prefix="NATS_", case_sensitive=False, extra="ignore")
