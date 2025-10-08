"""
Config loader for MythosMUD server.

Supported config fields:
- db_path: str
- log_path: str
- log_level: str
- host: str
- port: int
- max_connections: int
- connection_timeout: int
- data_dir: str
- player_dir: str
- log_dir: str
- motd_file: str
- start_room: str
- starting_level: int
- allow_multiplay: bool
- max_players: int
- enable_combat: bool
- enable_weather: bool
- enable_pvp: bool
- enable_stack_traces: bool
- auth_backend: str
- auth_db_file: str
- registration_enabled: bool
- allow_guest_login: bool
- areas: list
- npcs: list
- quests: list
- admin_password: str
- admin_port: int
- enable_remote_console: bool
- xp_multiplier: float
- hp_regen_rate: int
- combat_tick_interval: int
- game_tick_rate: float
- weather_update_interval: int
- save_interval: int
# ...plus future/advanced fields
"""

import os

import yaml

from .logging_config import get_logger

logger = get_logger(__name__)

# CRITICAL: No default config file - explicit configuration is REQUIRED
# Server must be started with MYTHOSMUD_CONFIG_PATH environment variable
_config = None

_DEFAULTS = {
    "host": "127.0.0.1",
    "port": 54731,
    # Environment-based fields - these will be set from environment variables
    "database_url": None,  # Will be set from DATABASE_URL environment variable
    "admin_password": None,  # Must be set via environment variable
    "invite_codes_file": "invites.json",
    "motd_file": "data/motd.html",
    "aliases_dir": None,  # Will be set from ALIASES_DIR environment variable
    # New logging configuration
    "logging": {
        "environment": "development",
        "level": "DEBUG",  # Most verbose logging level
        "format": "colored",  # json, human, colored
        "log_base": "logs",
        "rotation": {"max_size": "100MB", "backup_count": 5},
        "compression": True,
        "disable_logging": False,
    },
    "max_connections_per_player": 3,
    "rate_limit_window": 60,
    "rate_limit_max_requests": 100,
    "max_command_length": 1000,
    "max_alias_depth": 10,
    "max_alias_length": 500,
    "max_aliases_per_player": 50,
    "default_player_room": "earth_arkhamcity_northside_intersection_derby_high",
    "default_player_stats": {
        "strength": 10,
        "dexterity": 10,
        "constitution": 10,
        "intelligence": 10,
        "wisdom": 10,
        "charisma": 10,
        "max_health": 100,
        "max_sanity": 100,
        "health": 100,
        "sanity": 100,
        "fear": 0,
        "corruption": 0,
        "occult_knowledge": 0,
    },
    "hp_regen_rate": 1,
    "combat_tick_interval": 6,
    "game_tick_rate": 1.0,
    "weather_update_interval": 300,
    "save_interval": 60,
    # NATS configuration for real-time messaging
    "nats": {
        "enabled": True,
        "url": "nats://localhost:4222",
        "max_payload": 1048576,  # 1MB max message size
        "reconnect_time_wait": 1,
        "max_reconnect_attempts": 5,
        "connect_timeout": 5,
        "ping_interval": 30,
        "max_outstanding_pings": 5,
    },
    # Chat system configuration
    "chat": {
        "rate_limiting": {
            "enabled": True,
            "global": 10,  # messages per minute
            "local": 20,
            "say": 15,
            "party": 30,
            "whisper": 5,
        },
        "content_filtering": {
            "enabled": True,
            "profanity_filter": True,
            "keyword_detection": True,
        },
        "message_history": {
            "enabled": True,
            "retention_days": 30,
            "max_messages_per_channel": 1000,
        },
    },
}

_FIELD_TYPES = {
    "host": str,
    "port": int,
    "logging": dict,
    "database_url": str,
    "admin_password": str,
    "invite_codes_file": str,
    "motd_file": str,
    "aliases_dir": str,
    "max_connections_per_player": int,
    "rate_limit_window": int,
    "rate_limit_max_requests": int,
    "max_command_length": int,
    "max_alias_depth": int,
    "max_alias_length": int,
    "max_aliases_per_player": int,
    "default_player_room": str,
    "default_player_stats": dict,
    "hp_regen_rate": int,
    "combat_tick_interval": int,
    "game_tick_rate": float,
    "weather_update_interval": int,
    "save_interval": int,
    "nats": dict,
    "chat": dict,
}


def _get_config_path() -> str:
    """
    Determine the appropriate config file path based on environment.

    REQUIRES: MYTHOSMUD_CONFIG_PATH environment variable must be set.

    Returns:
        Path to the config file to use

    Raises:
        ValueError: If MYTHOSMUD_CONFIG_PATH is not set or file doesn't exist
    """
    # Check for explicit config path from environment variable
    config_path = os.getenv("MYTHOSMUD_CONFIG_PATH")

    if not config_path:
        error_msg = (
            "CRITICAL: MYTHOSMUD_CONFIG_PATH environment variable is not set!\n"
            "The server REQUIRES explicit configuration. Please set MYTHOSMUD_CONFIG_PATH to one of:\n"
            "  - server/server_config.local.yaml (for local development)\n"
            "  - server/server_config.unit_test.yaml (for unit tests)\n"
            "  - server/server_config.e2e_test.yaml (for E2E tests)\n"
            "  - server/server_config.production.yaml (for production)\n"
        )
        logger.error(error_msg)
        raise ValueError(error_msg)

    if not os.path.exists(config_path):
        error_msg = (
            f"CRITICAL: Configuration file not found at: {config_path}\n"
            f"MYTHOSMUD_CONFIG_PATH is set but the file doesn't exist.\n"
            f"Please verify the path is correct."
        )
        logger.error(error_msg)
        raise FileNotFoundError(error_msg)

    logger.debug("Using config path from environment", config_path=config_path)
    return config_path


def reset_config():
    """Reset the config cache for testing purposes."""
    global _config
    logger.debug("Resetting config cache")
    _config = None


def get_config(config_path: str = None):
    """
    Load and return the server config as a dict (singleton).

    REQUIRES: MYTHOSMUD_CONFIG_PATH environment variable must be set.

    Args:
        config_path: Optional explicit path to config file. If not provided,
                    uses MYTHOSMUD_CONFIG_PATH environment variable.

    Raises:
        ValueError: If neither config_path nor MYTHOSMUD_CONFIG_PATH is set
        FileNotFoundError: If config file doesn't exist
    """
    global _config
    if _config is not None and config_path is None:
        logger.debug("Returning cached config")
        return _config

    # Use environment-based path if no specific path provided
    if config_path is None:
        config_path = _get_config_path()  # Will raise if not set

    logger.info("Loading configuration", config_path=config_path)

    try:
        with open(config_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if not isinstance(data, dict):
                logger.warning("Config file is not a dictionary, using empty dict")
                data = {}
        logger.debug("Config file loaded successfully", config_path=config_path)
    except Exception as e:
        logger.warning("Failed to load config file, using defaults", config_path=config_path, error=str(e))
        data = {}

    # Merge with defaults
    config = dict(_DEFAULTS)
    config.update({k: v for k, v in (data or {}).items() if v is not None})
    logger.debug("Config merged with defaults")

    # Map YAML field names to expected config keys
    if "db_path" in config and config["database_url"] is None:
        config["database_url"] = config.pop("db_path")

    # Handle legacy logging configuration
    if "log_level" in config:
        if "logging" not in config:
            config["logging"] = {}
        config["logging"]["level"] = config.pop("log_level")

    if "log_path" in config:
        if "logging" not in config:
            config["logging"] = {}
        config["logging"]["log_base"] = config.pop("log_path")

    # Handle environment variables for path configuration (prioritize over YAML)
    if os.getenv("DATABASE_URL"):
        logger.debug("Using DATABASE_URL from environment")
        config["database_url"] = os.getenv("DATABASE_URL")

    # Legacy PERSIST_LOG handling removed - now using centralized logging

    if os.getenv("ALIASES_DIR"):
        logger.debug("Using ALIASES_DIR from environment")
        config["aliases_dir"] = os.getenv("ALIASES_DIR")

    # Validate types
    for k, typ in _FIELD_TYPES.items():
        if k in config:
            try:
                if typ is bool:
                    # Handle various boolean representations
                    if isinstance(config[k], str):
                        config[k] = config[k].lower() == "true"
                    elif isinstance(config[k], bool):
                        pass  # Already correct type
                    else:
                        # Invalid type for boolean, will fall back to default
                        raise ValueError(f"Invalid boolean value: {config[k]}")
                elif typ is list:
                    if not isinstance(config[k], list):
                        config[k] = [config[k]] if config[k] is not None else []
                else:
                    config[k] = typ(config[k])
            except Exception:
                config[k] = _DEFAULTS[k]
        else:
            config[k] = _DEFAULTS[k]
    # Handle environment variables for sensitive data
    if "admin_password" in config and config["admin_password"] is None:
        admin_password = os.getenv("MYTHOSMUD_ADMIN_PASSWORD")
        if admin_password:
            logger.debug("Using MYTHOSMUD_ADMIN_PASSWORD from environment")
            config["admin_password"] = admin_password
        else:
            logger.warning("MYTHOSMUD_ADMIN_PASSWORD environment variable not set")
            raise ValueError("MYTHOSMUD_ADMIN_PASSWORD environment variable must be set")

    # Handle environment variables for path configuration
    if "database_url" in config and config["database_url"] is None:
        database_url = os.getenv("DATABASE_URL")
        if database_url:
            logger.debug("Using DATABASE_URL from environment")
            config["database_url"] = database_url
        else:
            logger.error("DATABASE_URL environment variable not set")
            raise ValueError("DATABASE_URL environment variable must be set")

    if "aliases_dir" in config and config["aliases_dir"] is None:
        aliases_dir = os.getenv("ALIASES_DIR")
        if aliases_dir:
            logger.debug("Using ALIASES_DIR from environment")
            config["aliases_dir"] = aliases_dir
        else:
            logger.warning("ALIASES_DIR environment variable not set")
            raise ValueError("ALIASES_DIR environment variable must be set")

    # Remove legacy persistence_log handling since we now use structured logging

    _config = config
    logger.info(
        "Configuration loaded successfully",
        host=config.get("host"),
        port=config.get("port"),
        environment=config.get("logging", {}).get("environment", "unknown"),
    )
    return _config


def validate_config(config: dict) -> bool:
    """
    Validate that the config dict has all required fields and correct types.
    Returns True if valid, raises AssertionError if not.
    """
    for k, typ in _FIELD_TYPES.items():
        assert k in config, f"Missing config key: {k}"
        if typ is list:
            assert isinstance(config[k], list), f"Config key {k} should be a list"
    else:
        assert isinstance(config[k], typ), f"Config key {k} should be {typ.__name__}"
    return True
