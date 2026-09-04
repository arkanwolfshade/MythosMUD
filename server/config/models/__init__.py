"""
Pydantic-based configuration models for MythosMUD server.

This package replaces the legacy single-file models.py with type-safe,
validated configuration using Pydantic BaseSettings. All public config
classes and helpers are re-exported here so existing imports continue
to work:

    from server.config.models import AppConfig, NATSConfig, ...
    from server.config.models import _default_cors_origins, _parse_env_list
"""

from ._helpers import _default_cors_origins, _parse_env_list
from .app import AppConfig
from .chat_time import ChatConfig, TimeConfig
from .cors import CORSConfig
from .game import GameConfig
from .nats import NATSConfig
from .player_stats import PlayerStatsConfig
from .security_logging import LoggingConfig, SecurityConfig
from .server_db import DatabaseConfig, ServerConfig

__all__ = [
    "AppConfig",
    "ChatConfig",
    "CORSConfig",
    "DatabaseConfig",
    "GameConfig",
    "LoggingConfig",
    "NATSConfig",
    "PlayerStatsConfig",
    "SecurityConfig",
    "ServerConfig",
    "TimeConfig",
    "_default_cors_origins",
    "_parse_env_list",
]
