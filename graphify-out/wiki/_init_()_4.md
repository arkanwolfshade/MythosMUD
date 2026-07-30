# . init ()

> 47 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **GameConfig** (15 connections) — `server/config/models/game.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **Any** (6 connections)
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._legacy_game_entries()** (5 connections) — `server/config/models/app.py`
- **._legacy_nats_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_chat_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_cors_dict()** (5 connections) — `server/config/models/app.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **.set_legacy_environment_variables()** (2 connections) — `server/config/models/app.py`
- **.validate_max_connections()** (2 connections) — `server/config/models/game.py`
- **.validate_aliases_dir()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_tick_interval()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_timeout()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_xp_multiplier()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_alert_threshold()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_performance_threshold()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_error_threshold()** (2 connections) — `server/config/models/game.py`
- **Create a new AppConfig instance from current environment.      This is a helper** (1 connections) — `server/config/__init__.py`
- **Production config loader with caching.      Uses both @lru_cache and global _con** (1 connections) — `server/config/__init__.py`
- *... and 22 more nodes in this community*

## Relationships

- [world](world.md) (17 shared connections)
- [process dead players()](process_dead_players%28%29.md) (3 shared connections)
- [.model dump()](model_dump%28%29.md) (3 shared connections)
- [.get lucidity service()](get_lucidity_service%28%29.md) (2 shared connections)
- [MapZoneContext](MapZoneContext.md) (2 shared connections)
- [get health status()](get_health_status%28%29.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/config/models/game.py`

## Audit Trail

- EXTRACTED: 136 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*