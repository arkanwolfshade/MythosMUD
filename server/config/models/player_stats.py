"""
Default player statistics configuration model.
"""

from typing import Any

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


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

    model_config = SettingsConfigDict(env_prefix="DEFAULT_STATS_", case_sensitive=False, extra="ignore")

    def to_dict(self) -> dict[str, Any]:
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
