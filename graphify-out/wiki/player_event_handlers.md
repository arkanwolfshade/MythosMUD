# player event handlers

> 30 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **__init__.py** (11 connections) — `server/config/__init__.py`
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
- **Normalize environment variables so nested configs can parse them reliably.** (1 connections) — `server/config/models/app.py`
- *... and 5 more nodes in this community*

## Relationships

- [lucidity npc combat](lucidity_npc_combat.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [command factories exploration](command_factories_exploration.md) (3 shared connections)
- [config models cors](config_models_cors.md) (2 shared connections)
- [invite models rationale](invite_models_rationale.md) (2 shared connections)
- [combat validator validators](combat_validator_validators.md) (2 shared connections)
- [schemas calendar rationale](schemas_calendar_rationale.md) (1 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)
- [persistence container parse](persistence_container_parse.md) (1 shared connections)
- [playerHandlers eventHandlers healthEvent](playerHandlers_eventHandlers_healthEvent.md) (1 shared connections)
- [config models rationale](config_models_rationale.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`

## Audit Trail

- EXTRACTED: 108 (91%)
- INFERRED: 11 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*