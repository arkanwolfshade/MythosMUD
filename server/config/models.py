"""
Pydantic-based configuration models for MythosMUD server.

This module replaces the legacy config_loader.py with type-safe,
validated configuration using Pydantic BaseSettings.

As noted in the restricted archives: "Explicit configuration prevents
the seepage of secrets into unintended dimensions."
"""

# pylint: disable=too-many-lines  # Reason: Configuration models require extensive Pydantic model definitions for all server configuration options

import json
import os
from datetime import UTC, datetime
from typing import Any

from pydantic import AliasChoices, Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsError

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _parse_env_list(candidate: Any) -> list[str]:
    """Parse a string from the environment as JSON list or CSV."""
    if candidate is None:
        return []
    s = str(candidate).strip()
    if not s:
        return []
    try:
        loaded = json.loads(s)
        if isinstance(loaded, list):
            return [str(item).strip() for item in loaded if str(item).strip()]
    except json.JSONDecodeError:
        pass
    return [item.strip() for item in s.split(",") if item.strip()]


def _default_cors_origins() -> list[str]:
    """Derive default CORS origins with environment taking precedence."""
    raw = (
        os.getenv("CORS_ALLOW_ORIGINS")
        or os.getenv("CORS_ORIGINS")
        or os.getenv("CORS_ALLOWED_ORIGINS")
        or os.getenv("ALLOWED_ORIGINS")
    )
    parsed = _parse_env_list(raw) if raw is not None else []
    if parsed:
        return parsed
    return ["http://localhost:5173", "http://127.0.0.1:5173"]


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

    model_config = {"env_prefix": "SERVER_", "case_sensitive": False, "extra": "ignore"}


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
        # Human reader: If url is missing but npc_url is set, use npc_url as url
        # AI reader: Fallback logic for missing url field when npc_url is available
        if isinstance(data, dict):
            # If url is missing but npc_url is present, use npc_url as url
            if "url" not in data and "npc_url" in data and data["npc_url"]:
                logger.debug("url missing but npc_url available, using npc_url as url fallback")
                data["url"] = data["npc_url"]
            # Also check environment variables if data is empty or url is missing
            elif "url" not in data or not data.get("url"):
                # Check if DATABASE_URL is in environment but not in data
                db_url = os.getenv("DATABASE_URL")
                npc_url = os.getenv("DATABASE_NPC_URL")
                if not db_url and npc_url:
                    logger.debug("DATABASE_URL missing but DATABASE_NPC_URL available, using as fallback")
                    data["url"] = npc_url
        return data

    model_config = {"env_prefix": "DATABASE_", "case_sensitive": False, "extra": "ignore"}


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
    enable_connection_pooling: bool = Field(default=True, description="Enable connection pooling")

    # Message batching configuration
    batch_size: int = Field(default=100, description="Maximum messages per batch")
    batch_timeout: float = Field(default=0.1, description="Batch timeout in seconds")
    enable_message_batching: bool = Field(default=True, description="Enable message batching")

    # Subject validation configuration
    enable_subject_validation: bool = Field(default=True, description="Enable NATS subject validation")
    strict_subject_validation: bool = Field(
        default=False, description="Enable strict subject validation (reject invalid subjects)"
    )

    # Message acknowledgment configuration
    manual_ack: bool = Field(default=False, description="Enable manual message acknowledgment (ack/nak)")

    # TLS/SSL configuration
    tls_enabled: bool = Field(default=False, description="Enable TLS/SSL encryption for NATS connections")
    tls_cert_file: str | None = Field(default=None, description="Path to TLS certificate file (.crt)")
    tls_key_file: str | None = Field(default=None, description="Path to TLS private key file (.key)")
    tls_ca_file: str | None = Field(default=None, description="Path to TLS CA certificate file for verification")
    tls_verify: bool = Field(default=True, description="Verify TLS certificates (set False for self-signed certs)")

    @field_validator("tls_cert_file", "tls_key_file", "tls_ca_file")
    @classmethod
    def validate_tls_files(cls, v: str | None, info) -> str | None:
        """Validate TLS file paths exist when TLS is enabled."""
        # Only validate if TLS is enabled and file is provided
        # We can't access other fields in field_validator, so we'll do full validation in model_validator
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
            if not self.tls_cert_file or not self.tls_key_file:
                logger.error(
                    "TLS enabled but certificate or key file not provided",
                    cert_file=self.tls_cert_file,
                    key_file=self.tls_key_file,
                )
                raise ValueError("TLS certificate and key files are required when TLS is enabled")
            # Verify files exist
            from pathlib import Path

            cert_path = Path(self.tls_cert_file)
            key_path = Path(self.tls_key_file)
            if not cert_path.exists():
                raise ValueError(f"TLS certificate file not found: {self.tls_cert_file}")
            if not key_path.exists():
                raise ValueError(f"TLS key file not found: {self.tls_key_file}")
            if self.tls_ca_file:
                ca_path = Path(self.tls_ca_file)
                if not ca_path.exists():
                    raise ValueError(f"TLS CA file not found: {self.tls_ca_file}")
            # Update URL to use tls:// if still using nats://
            if self.url.startswith("nats://"):
                logger.info("TLS enabled, updating URL scheme to tls://", old_url=self.url)
                self.url = self.url.replace("nats://", "tls://", 1)
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

    model_config = {"env_prefix": "NATS_", "case_sensitive": False, "extra": "ignore"}


class SecurityConfig(BaseSettings):
    """Security-sensitive configuration."""

    admin_password: str = Field(..., description="Admin password (required)")
    invite_codes_file: str = Field(default="invites.json", description="Invite codes file path")

    @field_validator("admin_password")
    @classmethod
    def validate_admin_password(cls, v: str) -> str:
        """Validate admin password strength (production only)."""
        logger.debug("Validating admin password strength", password_length=len(v))
        # Only enforce strict validation in production
        # This is determined by LoggingConfig.environment but we can't access it here
        # So we check if it looks like a real password vs test password
        if len(v) < 8:
            logger.error("Admin password validation failed - too short", password_length=len(v), minimum_length=8)
            raise ValueError("Admin password must be at least 8 characters")
        logger.debug("Admin password validation successful", password_length=len(v))
        return v

    model_config = {"env_prefix": "MYTHOSMUD_", "case_sensitive": False, "extra": "ignore"}


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

    model_config = {"env_prefix": "LOGGING_", "case_sensitive": False, "extra": "ignore"}

    def to_legacy_dict(self) -> dict:
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


class GameConfig(BaseSettings):
    """Game-specific configuration."""

    default_player_room: str = Field(
        default="earth_arkhamcity_sanitarium_room_foyer_001",
        description="Default starting room for E2E tests and new players",
    )
    max_connections_per_player: int = Field(default=3, description="Max simultaneous connections per player")
    rate_limit_window: int = Field(default=60, description="Rate limit window in seconds")
    rate_limit_max_requests: int = Field(default=100, description="Max requests per window")
    max_command_length: int = Field(default=1000, description="Maximum command length")
    max_alias_depth: int = Field(default=10, description="Maximum alias expansion depth")
    max_alias_length: int = Field(default=500, description="Maximum alias command length")
    max_aliases_per_player: int = Field(default=50, description="Maximum aliases per player")
    aliases_dir: str = Field(..., description="Directory for alias storage (required)")
    motd_file: str = Field(default="data/motd.html", description="Message of the day file")

    # Game mechanics
    dp_regen_rate: int = Field(default=1, description="Determination regeneration rate")
    combat_tick_interval: int = Field(default=6, description="Combat tick interval in seconds (1 Mythos minute)")
    server_tick_rate: float = Field(default=0.1, description="Server tick rate in seconds (100ms default)")
    weather_update_interval: int = Field(default=300, description="Weather update interval in seconds")
    save_interval: int = Field(default=60, description="Player save interval in seconds")

    # Combat system configuration
    combat_enabled: bool = Field(default=True, description="Enable/disable combat system")
    combat_timeout_seconds: int = Field(default=180, description="Combat timeout in seconds")
    combat_xp_multiplier: float = Field(default=1.0, description="XP multiplier for combat rewards")
    combat_logging_enabled: bool = Field(default=True, description="Enable combat audit logging")
    combat_monitoring_enabled: bool = Field(default=True, description="Enable combat monitoring and alerting")
    combat_alert_threshold: int = Field(default=5, description="Alert threshold for combat events")
    combat_performance_threshold: int = Field(default=1000, description="Performance threshold in milliseconds")
    combat_error_threshold: int = Field(default=3, description="Error threshold for combat failures")

    # Combat damage configuration
    basic_unarmed_damage: int = Field(default=10, description="Base damage for unarmed melee attacks")

    @field_validator("max_connections_per_player")
    @classmethod
    def validate_max_connections(cls, v: int) -> int:
        """Validate max connections is reasonable."""
        if v < 1 or v > 10:
            raise ValueError("Max connections per player must be between 1 and 10")
        return v

    @field_validator("aliases_dir")
    @classmethod
    def validate_aliases_dir(cls, v: str) -> str:
        """Validate aliases directory path."""
        if not v:
            raise ValueError("Aliases directory must be specified")
        return v

    @field_validator("combat_tick_interval")
    @classmethod
    def validate_combat_tick_interval(cls, v: int) -> int:
        """Validate combat tick interval."""
        if not 1 <= v <= 60:
            raise ValueError("Combat tick interval must be between 1 and 60 seconds")
        return v

    @field_validator("combat_timeout_seconds")
    @classmethod
    def validate_combat_timeout(cls, v: int) -> int:
        """Validate combat timeout."""
        if not 60 <= v <= 1800:
            raise ValueError("Combat timeout must be between 60 and 1800 seconds")
        return v

    @field_validator("combat_xp_multiplier")
    @classmethod
    def validate_combat_xp_multiplier(cls, v: float) -> float:
        """Validate combat XP multiplier."""
        if not 1.0 <= v <= 5.0:
            raise ValueError("XP multiplier must be between 1.0 and 5.0")
        return v

    @field_validator("combat_alert_threshold")
    @classmethod
    def validate_combat_alert_threshold(cls, v: int) -> int:
        """Validate combat alert threshold."""
        if not 1 <= v <= 100:
            raise ValueError("Alert threshold must be between 1 and 100")
        return v

    @field_validator("combat_performance_threshold")
    @classmethod
    def validate_combat_performance_threshold(cls, v: int) -> int:
        """Validate combat performance threshold."""
        if not 100 <= v <= 5000:
            raise ValueError("Performance threshold must be between 100 and 5000 milliseconds")
        return v

    @field_validator("combat_error_threshold")
    @classmethod
    def validate_combat_error_threshold(cls, v: int) -> int:
        """Validate combat error threshold."""
        if not 1 <= v <= 50:
            raise ValueError("Error threshold must be between 1 and 50")
        return v

    model_config = {"env_prefix": "GAME_", "case_sensitive": False, "extra": "ignore"}


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

    model_config = {"env_prefix": "CHAT_", "case_sensitive": False, "extra": "ignore"}


class TimeConfig(BaseSettings):
    """Temporal compression configuration for the MythosChronicle."""

    compression_ratio: float = Field(default=9.6, description="Mythos hours per real hour")
    real_epoch_utc: datetime = Field(
        default_factory=lambda: datetime(2025, 1, 1, tzinfo=UTC),
        description="Reference UTC timestamp anchoring real time calculations",
    )
    mythos_epoch: datetime = Field(
        default_factory=lambda: datetime(1930, 1, 1, tzinfo=UTC),
        description="Reference Mythos timestamp paired with the real epoch",
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

    model_config = {"env_prefix": "TIME_", "case_sensitive": False, "extra": "ignore"}


class CORSConfig(BaseSettings):
    """Cross-origin resource sharing configuration."""

    allow_origins: list[str] = Field(
        default_factory=_default_cors_origins,
        validation_alias=AliasChoices("allow_origins", "origins", "allowed_origins"),
        description="Origins permitted to access the MythosMUD API",
    )
    allow_credentials: bool = Field(
        default=True,
        validation_alias=AliasChoices("allow_credentials", "credentials"),
        description="Whether credentialed requests are accepted",
    )
    allow_methods: list[str] = Field(
        default_factory=lambda: ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        validation_alias=AliasChoices("allow_methods", "methods"),
        description="HTTP methods permitted by CORS responses",
    )
    allow_headers: list[str] = Field(
        default_factory=lambda: [
            "Content-Type",
            "Authorization",
            "X-Requested-With",
            "Accept",
            "Accept-Language",
        ],
        validation_alias=AliasChoices("allow_headers", "headers"),
        description="Request headers permitted by CORS responses",
    )
    expose_headers: list[str] = Field(
        default_factory=list,
        validation_alias=AliasChoices("expose_headers"),
        description="Response headers exposed to browser clients",
    )
    max_age: int = Field(
        default=600,
        validation_alias=AliasChoices("max_age"),
        description="Seconds browsers may cache CORS preflight responses",
    )

    model_config = {
        "env_prefix": "CORS_",
        "case_sensitive": False,
        "extra": "ignore",
    }

    def __init__(self, **kwargs: Any) -> None:
        # Initialize with standard sources
        super().__init__(**kwargs)
        # Post-init: ensure environment variables override defaults reliably
        env_raw = (
            os.getenv("CORS_ALLOW_ORIGINS")
            or os.getenv("CORS_ORIGINS")
            or os.getenv("CORS_ALLOWED_ORIGINS")
            or os.getenv("ALLOWED_ORIGINS")
        )
        if env_raw is not None and str(env_raw).strip():
            # Override allow_origins with parsed environment value
            parsed = self._parse_csv(env_raw, allow_empty=False)
            try:
                object.__setattr__(self, "allow_origins", parsed)
            except (AttributeError, TypeError):
                # Fallback assignment if model is mutable
                self.allow_origins = parsed

    @model_validator(mode="after")
    def _apply_env_overrides(self) -> "CORSConfig":
        """As a last step, ensure env-specified origins take precedence."""
        env_raw = (
            os.getenv("CORS_ALLOW_ORIGINS")
            or os.getenv("CORS_ORIGINS")
            or os.getenv("CORS_ALLOWED_ORIGINS")
            or os.getenv("ALLOWED_ORIGINS")
        )
        if env_raw is not None and str(env_raw).strip():
            parsed = self._parse_csv(env_raw, allow_empty=False)
            try:
                object.__setattr__(self, "allow_origins", parsed)
            except (AttributeError, TypeError):
                self.allow_origins = parsed
        return self

    @classmethod
    def _parse_allow_origins_from_env(cls) -> list[str] | None:
        """Parse CORS allow origins from environment variables."""
        cors_env = os.getenv("CORS_ALLOW_ORIGINS") or os.getenv("CORS_ORIGINS") or os.getenv("CORS_ALLOWED_ORIGINS")
        if cors_env is not None:
            return cls._parse_csv(cors_env, allow_empty=False)

        legacy = os.getenv("ALLOWED_ORIGINS")
        if legacy is not None:
            return cls._parse_csv(legacy, allow_empty=False)

        return None

    @classmethod
    def _parse_allow_methods_from_env(cls) -> list[str] | None:
        """Parse CORS allow methods from environment variables."""
        raw_methods = os.getenv("CORS_ALLOW_METHODS") or os.getenv("ALLOWED_METHODS")
        if raw_methods is not None:
            return [m.upper() for m in cls._parse_csv(raw_methods, allow_empty=False)]
        return None

    @classmethod
    def _parse_allow_headers_from_env(cls) -> list[str] | None:
        """Parse CORS allow headers from environment variables."""
        raw_headers = os.getenv("CORS_ALLOW_HEADERS") or os.getenv("ALLOWED_HEADERS")
        if raw_headers is not None:
            return cls._parse_csv(raw_headers, allow_empty=False)
        return None

    @classmethod
    def _parse_max_age_from_env(cls) -> int | None:
        """Parse CORS max age from environment variables."""
        raw_max_age = os.getenv("CORS_MAX_AGE")
        if raw_max_age is not None and raw_max_age.isdigit():
            return int(raw_max_age)
        return None

    @classmethod
    def _parse_allow_credentials_from_env(cls) -> bool | None:
        """Parse CORS allow credentials from environment variables."""
        raw_creds = os.getenv("CORS_ALLOW_CREDENTIALS")
        if raw_creds is not None:
            return str(raw_creds).strip().lower() in {"1", "true", "yes", "on"}
        return None

    @classmethod
    def settings_customise_sources(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Pydantic settings customization requires many parameters for configuration sources
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
        **_kwargs,
    ):
        def manual_env_source() -> dict[str, Any]:
            """Manually parse environment for CORS fields to avoid JSON decoding issues."""
            state: dict[str, Any] = {}

            allow_origins = cls._parse_allow_origins_from_env()
            if allow_origins is not None:
                state["allow_origins"] = allow_origins

            allow_methods = cls._parse_allow_methods_from_env()
            if allow_methods is not None:
                state["allow_methods"] = allow_methods

            allow_headers = cls._parse_allow_headers_from_env()
            if allow_headers is not None:
                state["allow_headers"] = allow_headers

            max_age = cls._parse_max_age_from_env()
            if max_age is not None:
                state["max_age"] = max_age

            allow_credentials = cls._parse_allow_credentials_from_env()
            if allow_credentials is not None:
                state["allow_credentials"] = allow_credentials

            return state

        return init_settings, manual_env_source, dotenv_settings, file_secret_settings

    @staticmethod
    def _validate_non_empty(cleaned: list[str], allow_empty: bool) -> None:
        """Validate that cleaned list is not empty if allow_empty is False."""
        if not cleaned and not allow_empty:
            raise ValueError("At least one entry must be provided")

    @staticmethod
    def _clean_list_items(items: list[Any]) -> list[str]:
        """Clean and filter list items, removing empty strings."""
        return [str(item).strip() for item in items if str(item).strip()]

    @staticmethod
    def _parse_json_array(candidate: str, allow_empty: bool) -> list[str] | None:
        """Parse JSON array string if it looks like one, otherwise return None."""
        if not (candidate.startswith("[") and candidate.endswith("]")):
            return None

        try:
            loaded = json.loads(candidate)
            if isinstance(loaded, list):
                cleaned = CORSConfig._clean_list_items(loaded)
                CORSConfig._validate_non_empty(cleaned, allow_empty)
                return cleaned
        except json.JSONDecodeError:
            pass

        return None

    @staticmethod
    def _parse_comma_separated(candidate: str, allow_empty: bool) -> list[str]:
        """Parse comma-separated string into cleaned list."""
        items = [item.strip() for item in candidate.split(",") if item.strip()]
        CORSConfig._validate_non_empty(items, allow_empty)
        return items

    @staticmethod
    def _parse_csv(value: object, allow_empty: bool) -> list[str]:
        """Parse comma separated strings or lists into a cleaned list of strings."""
        if value is None:
            if allow_empty:
                return []
            raise ValueError("At least one entry must be provided")

        if isinstance(value, list):
            cleaned = CORSConfig._clean_list_items(value)
            CORSConfig._validate_non_empty(cleaned, allow_empty)
            return cleaned

        if isinstance(value, str):
            candidate = value.strip()
            json_result = CORSConfig._parse_json_array(candidate, allow_empty)
            if json_result is not None:
                return json_result

            return CORSConfig._parse_comma_separated(candidate, allow_empty)

        raise ValueError("Value must be a list of strings or a comma-separated string")

    @field_validator("allow_origins", mode="before")
    @classmethod
    def parse_allow_origins(cls, value: object) -> list[str]:
        """Parse allowed origins with environment taking precedence over defaults."""
        # Prefer environment variables first (CORS_* then ALLOWED_ORIGINS)
        env_raw = (
            os.getenv("CORS_ALLOW_ORIGINS")
            or os.getenv("CORS_ORIGINS")
            or os.getenv("CORS_ALLOWED_ORIGINS")
            or os.getenv("ALLOWED_ORIGINS")
        )
        if env_raw is not None and str(env_raw).strip():
            return cls._parse_csv(env_raw, allow_empty=False)

        # Fall back to provided value (from init or defaults)
        if isinstance(value, list):
            return cls._parse_csv(value, allow_empty=False)
        if isinstance(value, str) and value.strip():
            return cls._parse_csv(value, allow_empty=False)

        # Final fallback to the model default
        field_info = cls.model_fields.get("allow_origins")
        if field_info is None:
            raise ValueError("Field 'allow_origins' not found in model fields")
        default_factory = field_info.default_factory
        defaults = list(default_factory()) if default_factory else []  # type: ignore[call-arg]  # Reason: Pydantic FieldInfo.default_factory is callable but mypy cannot infer the call signature, this is safe at runtime
        if not defaults:
            raise ValueError("At least one CORS origin must be provided")
        return defaults

    @field_validator("allow_methods", mode="before")
    @classmethod
    def parse_allow_methods(cls, value: object) -> list[str]:
        """Parse and validate CORS allowed methods.

        Args:
            value: The value to parse (can be string, list, or other)

        Returns:
            list[str]: List of uppercase HTTP method names
        """
        # Prefer explicit env overrides when present to ensure reliable behavior
        env_methods = os.getenv("CORS_ALLOW_METHODS") or os.getenv("ALLOWED_METHODS")
        if env_methods:
            methods = cls._parse_csv(env_methods, allow_empty=False)
        else:
            methods = cls._parse_csv(value, allow_empty=False)
        return [method.upper() for method in methods]

    @field_validator("allow_headers", mode="before")
    @classmethod
    def parse_allow_headers(cls, value: object) -> list[str]:
        """Parse and validate CORS allowed headers.

        Args:
            value: The value to parse (can be string, list, or other)

        Returns:
            list[str]: List of allowed header names
        """
        env_headers = os.getenv("CORS_ALLOW_HEADERS") or os.getenv("ALLOWED_HEADERS")
        if env_headers:
            return cls._parse_csv(env_headers, allow_empty=False)
        return cls._parse_csv(value, allow_empty=False)

    @field_validator("max_age", mode="before")
    @classmethod
    def parse_max_age(cls, value: object) -> int:
        """Parse and validate CORS max age value.

        Args:
            value: The value to parse (can be int, string, or other)

        Returns:
            int: The max age in seconds (defaults to 600 if invalid)
        """
        env_max_age = os.getenv("CORS_MAX_AGE")
        if env_max_age is not None and env_max_age:
            try:
                return int(env_max_age)
            except ValueError:
                pass
        return int(value) if isinstance(value, int | str) and str(value).isdigit() else 600

    @field_validator("expose_headers", mode="before")
    @classmethod
    def parse_expose_headers(cls, value: object) -> list[str]:
        """Parse and validate CORS exposed headers.

        Args:
            value: The value to parse (can be string, list, or other)

        Returns:
            list[str]: List of exposed header names
        """
        return cls._parse_csv(value, allow_empty=True)

    @field_validator("max_age")
    @classmethod
    def validate_max_age(cls, value: int) -> int:
        """Validate that max_age is non-negative.

        Args:
            value: The max age value to validate

        Returns:
            int: The validated max age value

        Raises:
            ValueError: If max_age is negative
        """
        if value < 0:
            raise ValueError("max_age must be non-negative")
        return value


class PlayerStatsConfig(BaseSettings):
    """Default player statistics configuration."""

    strength: int = Field(default=50, description="Default strength")
    dexterity: int = Field(default=50, description="Default dexterity")
    constitution: int = Field(default=50, description="Default constitution")
    size: int = Field(default=50, description="Default size")
    intelligence: int = Field(default=50, description="Default intelligence")
    power: int = Field(default=50, description="Default power")
    education: int = Field(default=50, description="Default education")
    charisma: int = Field(default=50, description="Default charisma")
    luck: int = Field(default=50, description="Default luck")
    max_dp: int = Field(default=20, description="Default max determination points (DP)")
    max_magic_points: int = Field(default=10, description="Default max magic points (MP)")
    max_lucidity: int = Field(default=100, description="Default max lucidity")
    determination_points: int = Field(default=20, description="Default starting determination points (DP)")
    magic_points: int = Field(default=10, description="Default starting magic points (MP)")
    lucidity: int = Field(default=100, description="Default starting lucidity")
    corruption: int = Field(default=0, description="Default corruption level")
    occult: int = Field(default=0, description="Default occult knowledge")

    @field_validator(
        "strength", "dexterity", "constitution", "size", "intelligence", "power", "education", "charisma", "luck"
    )
    @classmethod
    def validate_stat_range(cls, v: int) -> int:
        """Validate stats are in valid range."""
        # No hard caps as requested - just ensure positive
        if v < 1:
            raise ValueError("Stats must be at least 1")
        return v

    @field_validator(
        "max_dp",
        "max_magic_points",
        "max_lucidity",
        "determination_points",
        "magic_points",
        "lucidity",
    )
    @classmethod
    def validate_derived_stats(cls, v: int) -> int:
        """Validate derived stats values."""
        if v < 0:
            raise ValueError("Derived stats must be non-negative")
        return v

    model_config = {"env_prefix": "DEFAULT_STATS_", "case_sensitive": False, "extra": "ignore"}

    def to_dict(self) -> dict:
        """Convert to dictionary format expected by game code."""
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "size": self.size,
            "intelligence": self.intelligence,
            "power": self.power,
            "education": self.education,
            "charisma": self.charisma,
            "luck": self.luck,
            "max_dp": self.max_dp,
            "max_magic_points": self.max_magic_points,
            "max_lucidity": self.max_lucidity,
            "determination_points": self.determination_points,
            "magic_points": self.magic_points,
            "lucidity": self.lucidity,
            "corruption": self.corruption,
            "occult": self.occult,
        }


class AppConfig(BaseSettings):
    """
    Composite application configuration.

    This is the main configuration class that aggregates all other configs.
    Access via get_config() singleton function.
    """

    # Sub-configurations
    server: ServerConfig = Field(default_factory=ServerConfig)
    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    nats: NATSConfig = Field(default_factory=NATSConfig)
    security: SecurityConfig = Field(default_factory=SecurityConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    game: GameConfig = Field(default_factory=GameConfig)
    chat: ChatConfig = Field(default_factory=ChatConfig)
    time: TimeConfig = Field(default_factory=TimeConfig)
    cors: CORSConfig = Field(default_factory=CORSConfig)
    default_player_stats: PlayerStatsConfig = Field(default_factory=PlayerStatsConfig)

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "case_sensitive": False, "extra": "ignore"}

    def __init__(self, **kwargs):
        """Initialize configuration and set environment variables for legacy compatibility."""
        try:
            super().__init__(**kwargs)
        except SettingsError as error:
            if "allow_origins" in str(error):
                self._sanitize_environment_for_nested_configs()
                super().__init__(**kwargs)
            else:
                raise

        # Avoid mutating environment for CORS values to prevent cross-test leakage

    @model_validator(mode="after")
    def set_legacy_environment_variables(self) -> "AppConfig":
        """Set environment variables for legacy code that reads them directly."""
        # In mode="after", all fields are validated and instantiated as their config types
        # pylint: disable=no-member  # Reason: Pydantic model fields are dynamically accessible after validation, pylint cannot detect them statically
        database = self.database
        game = self.game

        if database.url:
            os.environ["DATABASE_URL"] = database.url

        if database.npc_url:
            os.environ["NPC_DATABASE_URL"] = database.npc_url

        if game.aliases_dir:
            os.environ["ALIASES_DIR"] = game.aliases_dir
        # pylint: enable=no-member

        return self

    @staticmethod
    def _sanitize_environment_for_nested_configs() -> None:
        """Normalize environment variables so nested configs can parse them reliably."""

        raw_origins = (
            os.getenv("CORS_ALLOW_ORIGINS")
            or os.getenv("CORS_ORIGINS")
            or os.getenv("CORS_ALLOWED_ORIGINS")
            or os.getenv("ALLOWED_ORIGINS")
        )
        if raw_origins and not raw_origins.strip().startswith("["):
            parsed = [item.strip() for item in raw_origins.split(",") if item.strip()]
            if parsed:
                serialized = json.dumps(parsed)
                os.environ["CORS_ALLOW_ORIGINS"] = serialized
                os.environ["CORS_ORIGINS"] = serialized
                os.environ["CORS_ALLOWED_ORIGINS"] = serialized

    def to_legacy_dict(self) -> dict:
        """
        Convert to legacy dict format for backward compatibility.

        This allows gradual migration of code that expects dict-based config access.
        """
        # Pylint can't detect Pydantic dynamic attributes, so disable no-member for this method
        # pylint: disable=no-member  # Reason: Pydantic model fields are dynamically accessible, pylint cannot detect them statically but they exist at runtime
        server = self.server
        database = self.database
        security = self.security
        logging_config = self.logging
        game = self.game
        nats = self.nats
        chat = self.chat
        cors = self.cors
        default_player_stats = self.default_player_stats

        return {
            # Server
            "host": server.host,
            "port": server.port,
            # Database
            "database_url": database.url,
            "npc_database_url": database.npc_url,
            # Security
            "admin_password": security.admin_password,
            "invite_codes_file": security.invite_codes_file,
            # Logging (convert to nested dict)
            "logging": logging_config.to_legacy_dict(),
            # Game
            "default_player_room": game.default_player_room,
            "max_connections_per_player": game.max_connections_per_player,
            "rate_limit_window": game.rate_limit_window,
            "rate_limit_max_requests": game.rate_limit_max_requests,
            "max_command_length": game.max_command_length,
            "max_alias_depth": game.max_alias_depth,
            "max_alias_length": game.max_alias_length,
            "max_aliases_per_player": game.max_aliases_per_player,
            "aliases_dir": game.aliases_dir,
            "motd_file": game.motd_file,
            "dp_regen_rate": game.dp_regen_rate,
            "combat_tick_interval": game.combat_tick_interval,
            "server_tick_rate": game.server_tick_rate,
            "weather_update_interval": game.weather_update_interval,
            "save_interval": game.save_interval,
            # Combat configuration
            "combat_enabled": game.combat_enabled,
            "combat_timeout_seconds": game.combat_timeout_seconds,
            "combat_xp_multiplier": game.combat_xp_multiplier,
            "combat_logging_enabled": game.combat_logging_enabled,
            "combat_monitoring_enabled": game.combat_monitoring_enabled,
            "combat_alert_threshold": game.combat_alert_threshold,
            "combat_performance_threshold": game.combat_performance_threshold,
            "combat_error_threshold": game.combat_error_threshold,
            # NATS (convert to nested dict)
            "nats": {
                "enabled": nats.enabled,
                "url": nats.url,
                "max_payload": nats.max_payload,
                "reconnect_time_wait": nats.reconnect_time_wait,
                "max_reconnect_attempts": nats.max_reconnect_attempts,
                "connect_timeout": nats.connect_timeout,
                "ping_interval": nats.ping_interval,
                "max_outstanding_pings": nats.max_outstanding_pings,
            },
            # Chat (convert to nested dict)
            "chat": {
                "rate_limiting": {
                    "enabled": True,
                    "global": chat.rate_limit_global,
                    "local": chat.rate_limit_local,
                    "say": chat.rate_limit_say,
                    "party": chat.rate_limit_party,
                    "whisper": chat.rate_limit_whisper,
                },
                "content_filtering": {
                    "enabled": chat.content_filtering_enabled,
                    "profanity_filter": chat.profanity_filter,
                    "keyword_detection": chat.keyword_detection,
                },
                "message_history": {
                    "enabled": chat.message_history_enabled,
                    "retention_days": chat.message_retention_days,
                    "max_messages_per_channel": chat.max_messages_per_channel,
                },
            },
            # CORS configuration
            "cors": {
                "allow_origins": cors.allow_origins,
                "allow_credentials": cors.allow_credentials,
                "allow_methods": cors.allow_methods,
                "allow_headers": cors.allow_headers,
                "expose_headers": cors.expose_headers,
                "max_age": cors.max_age,
            },
            # Default player stats
            "default_player_stats": default_player_stats.to_dict(),
        }
        # pylint: enable=no-member
