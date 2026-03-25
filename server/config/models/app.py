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

    def to_legacy_dict(self) -> dict[str, Any]:
        """
        Convert to legacy dict format for backward compatibility.

        This allows gradual migration of code that expects dict-based config access.
        """
        # pylint: disable=no-member  # Reason: Pydantic model fields are dynamically accessible at runtime
        s, db, sec, log_cfg = self.server, self.database, self.security, self.logging
        game, nats, chat, cors = self.game, self.nats, self.chat, self.cors
        base = {
            "host": s.host,
            "port": s.port,
            "database_url": db.url,
            "npc_database_url": db.npc_url,
            "admin_password": sec.admin_password,
            "invite_codes_file": sec.invite_codes_file,
            "logging": log_cfg.to_legacy_dict(),
            **self._legacy_game_entries(game),
            "nats": self._legacy_nats_dict(nats),
            "chat": self._legacy_chat_dict(chat),
            "cors": self._legacy_cors_dict(cors),
            "default_player_stats": self.default_player_stats.to_dict(),
        }
        # pylint: enable=no-member
        return base

    @staticmethod
    def _legacy_game_entries(game: GameConfig) -> dict[str, Any]:
        """Build legacy dict entries for game config."""
        return {
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
            "combat_enabled": game.combat_enabled,
            "combat_timeout_seconds": game.combat_timeout_seconds,
            "combat_xp_multiplier": game.combat_xp_multiplier,
            "combat_logging_enabled": game.combat_logging_enabled,
            "combat_monitoring_enabled": game.combat_monitoring_enabled,
            "combat_alert_threshold": game.combat_alert_threshold,
            "combat_performance_threshold": game.combat_performance_threshold,
            "combat_error_threshold": game.combat_error_threshold,
        }

    @staticmethod
    def _legacy_nats_dict(nats: NATSConfig) -> dict[str, Any]:
        """Build legacy nats nested dict."""
        return {
            "enabled": nats.enabled,
            "url": nats.url,
            "max_payload": nats.max_payload,
            "reconnect_time_wait": nats.reconnect_time_wait,
            "max_reconnect_attempts": nats.max_reconnect_attempts,
            "connect_timeout": nats.connect_timeout,
            "ping_interval": nats.ping_interval,
            "max_outstanding_pings": nats.max_outstanding_pings,
        }

    @staticmethod
    def _legacy_chat_dict(chat: ChatConfig) -> dict[str, Any]:
        """Build legacy chat nested dict."""
        return {
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
        }

    @staticmethod
    def _legacy_cors_dict(cors: CORSConfig) -> dict[str, Any]:
        """Build legacy cors nested dict."""
        return {
            "allow_origins": cors.allow_origins,
            "allow_credentials": cors.allow_credentials,
            "allow_methods": cors.allow_methods,
            "allow_headers": cors.allow_headers,
            "expose_headers": cors.expose_headers,
            "max_age": cors.max_age,
        }
