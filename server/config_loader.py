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

_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "server_config.yaml")
_config = None

_DEFAULTS = {
    "host": "127.0.0.1",
    "port": 54731,
    "max_connections": 100,
    "connection_timeout": 60,
    "data_dir": "./data/",
    "player_dir": "./data/players/",
    "log_dir": "./logs/",
    "motd_file": "./data/motd.txt",
    "start_room": "earth_arkham_city_campus_E_College_St_003",
    "starting_level": 1,
    "allow_multiplay": False,
    "max_players": 100,
    "enable_combat": True,
    "enable_weather": True,
    "enable_pvp": False,
    "enable_stack_traces": True,
    "auth_backend": "sqlite",
    "auth_db_file": "./data/users.db",
    "registration_enabled": True,
    "allow_guest_login": False,
    "areas": ["./data/rooms/arkham/"],
    "npcs": ["./data/npcs/guards.json"],
    "quests": ["./data/quests/tutorial.json"],
    "admin_password": "changeme",
    "admin_port": 5001,
    "enable_remote_console": False,
    "xp_multiplier": 1.0,
    "hp_regen_rate": 5,
    "combat_tick_interval": 2,
    "game_tick_rate": 1.0,
    "weather_update_interval": 300,
    "save_interval": 60,
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
}


def _get_config_path() -> str:
    """
    Determine the appropriate config file path based on environment.

    Returns:
        Path to the production config file
    """
    # Production always uses the main config file
    logger.debug("Getting config path", config_path=_CONFIG_PATH)
    return _CONFIG_PATH


def reset_config():
    """Reset the config cache for testing purposes."""
    global _config
    logger.debug("Resetting config cache")
    _config = None


def get_config(config_path: str = None):
    """
    Load and return the server config as a dict (singleton).
    Falls back to defaults if config file is missing or invalid.
    """
    global _config
    if _config is not None and (config_path is None or config_path == _CONFIG_PATH):
        logger.debug("Returning cached config")
        return _config

    # Use environment-based path if no specific path provided
    if config_path is None:
        config_path = _get_config_path()

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
