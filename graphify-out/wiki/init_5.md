# init

> 31 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **__init__.py** (11 connections) — `server/config/__init__.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
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
- **Configuration module for MythosMUD server.  This module provides type-safe, vali** (1 connections) — `server/config/__init__.py`
- **Create a new AppConfig instance from current environment.      This is a helper** (1 connections) — `server/config/__init__.py`
- **Production config loader with caching.      Uses both @lru_cache and global _con** (1 connections) — `server/config/__init__.py`
- **Test config loader without caching - always returns fresh instances.      This e** (1 connections) — `server/config/__init__.py`
- **BaseSettings** (1 connections)
- **Composite application configuration.      This is the main configuration class t** (1 connections) — `server/config/models/app.py`
- **Initialize configuration and set environment variables for legacy compatibility.** (1 connections) — `server/config/models/app.py`
- **Set environment variables for legacy code that reads them directly.** (1 connections) — `server/config/models/app.py`
- **Return first set CORS origins env var to reduce CCN in _sanitize.** (1 connections) — `server/config/models/app.py`
- *... and 6 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (10 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (7 shared connections)
- [CORSConfig](CORSConfig.md) (2 shared connections)
- [GameConfig](GameConfig.md) (2 shared connections)
- [nats config()](nats_config%28%29.md) (2 shared connections)
- [default cors origins()](default_cors_origins%28%29.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [test command factories utility](test_command_factories_utility.md) (2 shared connections)
- [get app instance()](get_app_instance%28%29.md) (1 shared connections)
- [combat](combat.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [lifespan](lifespan.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 109 (86%)
- INFERRED: 18 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*