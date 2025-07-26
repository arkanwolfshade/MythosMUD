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

_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "server_config.yaml")
_config = None

_DEFAULTS = {
    "db_path": "../data/players.db",
    "log_path": "./persistence.log",
    "log_level": "INFO",
    "host": "0.0.0.0",
    "port": 4000,
    "max_connections": 100,
    "connection_timeout": 60,
    "data_dir": "./data/",
    "player_dir": "./data/players/",
    "log_dir": "./logs/",
    "motd_file": "./data/motd.txt",
    "start_room": "arkham_001",
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
    "weather_update_interval": 60,
    "save_interval": 300,
}

_FIELD_TYPES = {
    "db_path": str,
    "log_path": str,
    "log_level": str,
    "host": str,
    "port": int,
    "max_connections": int,
    "connection_timeout": int,
    "data_dir": str,
    "player_dir": str,
    "log_dir": str,
    "motd_file": str,
    "start_room": str,
    "starting_level": int,
    "allow_multiplay": bool,
    "max_players": int,
    "enable_combat": bool,
    "enable_weather": bool,
    "enable_pvp": bool,
    "enable_stack_traces": bool,
    "auth_backend": str,
    "auth_db_file": str,
    "registration_enabled": bool,
    "allow_guest_login": bool,
    "areas": list,
    "npcs": list,
    "quests": list,
    "admin_password": str,
    "admin_port": int,
    "enable_remote_console": bool,
    "xp_multiplier": float,
    "hp_regen_rate": int,
    "combat_tick_interval": int,
    "game_tick_rate": float,
    "weather_update_interval": int,
    "save_interval": int,
}


def get_config(config_path: str = None):
    """
    Load and return the server config as a dict (singleton).
    Falls back to defaults if config file is missing or invalid.
    """
    global _config
    if _config is not None and (config_path is None or config_path == _CONFIG_PATH):
        return _config
    path = config_path or _CONFIG_PATH
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if not isinstance(data, dict):
                data = {}
    except Exception:
        data = {}
    # Merge with defaults
    config = dict(_DEFAULTS)
    config.update({k: v for k, v in (data or {}).items() if v is not None})
    # Validate types
    for k, typ in _FIELD_TYPES.items():
        if k in config:
            try:
                if typ is bool:
                    # YAML can parse 'true'/'false' as bool, but also as str
                    if isinstance(config[k], str):
                        config[k] = config[k].lower() == "true"
                elif typ is list:
                    if not isinstance(config[k], list):
                        config[k] = [config[k]] if config[k] is not None else []
                else:
                    config[k] = typ(config[k])
            except Exception:
                config[k] = _DEFAULTS[k]
        else:
            config[k] = _DEFAULTS[k]
    _config = config
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
            assert isinstance(
                config[k], typ
            ), f"Config key {k} should be {typ.__name__}"
    return True
