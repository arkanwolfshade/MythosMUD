# AppConfig

> 29 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **Any** (6 connections)
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._legacy_chat_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_cors_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_game_entries()** (5 connections) — `server/config/models/app.py`
- **._legacy_nats_dict()** (5 connections) — `server/config/models/app.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **.set_legacy_environment_variables()** (3 connections) — `server/config/models/app.py`
- **BaseSettings** (1 connections)
- **model_validator** (1 connections)
- **Create a new AppConfig instance from current environment. This is a helper…** (1 connections) — `server/config/__init__.py`
- **Production config loader with caching. Uses both @lru_cache and global…** (1 connections) — `server/config/__init__.py`
- **Test config loader without caching - always returns fresh instances. This…** (1 connections) — `server/config/__init__.py`
- **Build legacy dict entries for game config.** (1 connections) — `server/config/models/app.py`
- **Build legacy nats nested dict.** (1 connections) — `server/config/models/app.py`
- **Build legacy chat nested dict.** (1 connections) — `server/config/models/app.py`
- **Build legacy cors nested dict.** (1 connections) — `server/config/models/app.py`
- **Composite application configuration. This is the main configuration class that…** (1 connections) — `server/config/models/app.py`
- **Initialize configuration and set environment variables for legacy compatibility.** (1 connections) — `server/config/models/app.py`
- *... and 4 more nodes in this community*

## Relationships

- [config/models/__init__.py](config-models-__init__.py.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [get_config](get_config.md) (3 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (2 shared connections)
- [NATSService](NATSService.md) (2 shared connections)
- [GameConfig](GameConfig.md) (2 shared connections)
- [CORSConfig](CORSConfig.md) (2 shared connections)
- [_weapon_damage_from_equipped_player](_weapon_damage_from_equipped_player.md) (1 shared connections)
- [test_config_models.py](test_config_models.py.md) (1 shared connections)
- [DatabaseConfig](DatabaseConfig.md) (1 shared connections)
- [PlayerStatsConfig](PlayerStatsConfig.md) (1 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`

## Audit Trail

- EXTRACTED: 57 (84%)
- INFERRED: 11 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*