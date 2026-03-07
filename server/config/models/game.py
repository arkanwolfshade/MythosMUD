"""
Game-specific configuration model.
"""

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


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
    combat_tick_interval: int = Field(
        default=10, description="Combat round interval in seconds (100 ticks = 10 seconds)"
    )
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

    # Aggro/threat (ADR-016)
    aggro_stability_margin: float = Field(
        default=0.10, description="Threat must exceed current target by this fraction to switch (0.10 = 10%)"
    )
    aggro_healing_threat_factor: float = Field(
        default=0.5, description="Healing threat as fraction of heal amount (0.5 = 50%)"
    )
    aggro_damage_threat_multiplier: float = Field(
        default=1.0, description="Damage threat multiplier (tanks may use >1.0 later)"
    )

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

    model_config = SettingsConfigDict(env_prefix="GAME_", case_sensitive=False, extra="ignore")
