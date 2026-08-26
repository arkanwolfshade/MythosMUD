"""
Composite application configuration model.
"""

import json
import os
from typing import Any

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict, SettingsError

from .chat_time import ChatConfig, TimeConfig
from .cors import CORSConfig
from .game import GameConfig
from .nats import NATSConfig
from .player_stats import PlayerStatsConfig
from .security_logging import LoggingConfig, SecurityConfig
from .server_db import DatabaseConfig, ServerConfig


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

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore")

    def __init__(self, **kwargs: Any) -> None:
        """Initialize configuration and set environment variables for legacy compatibility."""
        try:
            super().__init__(**kwargs)
        except SettingsError as error:
            if "allow_origins" in str(error):
                self._sanitize_environment_for_nested_configs()
                super().__init__(**kwargs)
            else:
                raise

    @model_validator(mode="after")
    def set_legacy_environment_variables(self) -> "AppConfig":
        """Set environment variables for legacy code that reads them directly."""
        # pylint: disable=no-member  # Reason: Pydantic model fields are dynamically accessible after validation
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
    def _first_cors_origins_env() -> str | None:
        """Return first set CORS origins env var to reduce CCN in _sanitize."""
        for key in ("CORS_ALLOW_ORIGINS", "CORS_ORIGINS", "CORS_ALLOWED_ORIGINS", "ALLOWED_ORIGINS"):
            val = os.getenv(key)
            if val:
                return val
        return None

    @staticmethod
    def _sanitize_environment_for_nested_configs() -> None:
        """Normalize environment variables so nested configs can parse them reliably."""
        raw_origins = AppConfig._first_cors_origins_env()
        if not raw_origins or raw_origins.strip().startswith("["):
            return
        parsed = [item.strip() for item in raw_origins.split(",") if item.strip()]
        if not parsed:
            return
        serialized = json.dumps(parsed)
        os.environ["CORS_ALLOW_ORIGINS"] = serialized
        os.environ["CORS_ORIGINS"] = serialized
        os.environ["CORS_ALLOWED_ORIGINS"] = serialized
