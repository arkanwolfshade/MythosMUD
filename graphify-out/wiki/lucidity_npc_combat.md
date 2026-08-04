# lucidity npc combat

> 35 nodes

## Key Concepts

- **__init__.py** (24 connections) — `server/config/models/__init__.py`
- **app.py** (20 connections) — `server/config/models/app.py`
- **LoggingConfig** (10 connections) — `server/config/models/security_logging.py`
- **TimeConfig** (9 connections) — `server/config/models/chat_time.py`
- **ChatConfig** (8 connections) — `server/config/models/chat_time.py`
- **security_logging.py** (7 connections) — `server/config/models/security_logging.py`
- **SecurityConfig** (7 connections) — `server/config/models/security_logging.py`
- **chat_time.py** (5 connections) — `server/config/models/chat_time.py`
- **game.py** (4 connections) — `server/config/models/game.py`
- **player_stats.py** (4 connections) — `server/config/models/player_stats.py`
- **.to_legacy_dict()** (3 connections) — `server/config/models/security_logging.py`
- **BaseSettings** (2 connections)
- **.validate_rate_limits()** (2 connections) — `server/config/models/chat_time.py`
- **.validate_compression_ratio()** (2 connections) — `server/config/models/chat_time.py`
- **BaseSettings** (2 connections)
- **.validate_admin_password()** (2 connections) — `server/config/models/security_logging.py`
- **.validate_environment()** (2 connections) — `server/config/models/security_logging.py`
- **Pydantic-based configuration models for MythosMUD server.  This package replaces** (1 connections) — `server/config/models/__init__.py`
- **Composite application configuration model.** (1 connections) — `server/config/models/app.py`
- **Chat and time configuration models.** (1 connections) — `server/config/models/chat_time.py`
- **Chat system configuration.** (1 connections) — `server/config/models/chat_time.py`
- **Validate rate limits are reasonable.** (1 connections) — `server/config/models/chat_time.py`
- **Temporal compression configuration for the MythosChronicle.** (1 connections) — `server/config/models/chat_time.py`
- **Ensure we never divide by zero or run the chronicle backward.** (1 connections) — `server/config/models/chat_time.py`
- **Game-specific configuration model.** (1 connections) — `server/config/models/game.py`
- *... and 10 more nodes in this community*

## Relationships

- [player event handlers](player_event_handlers.md) (8 shared connections)
- [admin command setstat](admin_command_setstat.md) (5 shared connections)
- [config models cors](config_models_cors.md) (4 shared connections)
- [config models rationale](config_models_rationale.md) (4 shared connections)
- [invite models rationale](invite_models_rationale.md) (3 shared connections)
- [persistence container parse](persistence_container_parse.md) (3 shared connections)
- [combat validator validators](combat_validator_validators.md) (2 shared connections)
- [playerHandlers eventHandlers healthEvent](playerHandlers_eventHandlers_healthEvent.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)

## Source Files

- `server/config/models/__init__.py`
- `server/config/models/app.py`
- `server/config/models/chat_time.py`
- `server/config/models/game.py`
- `server/config/models/player_stats.py`
- `server/config/models/security_logging.py`

## Audit Trail

- EXTRACTED: 127 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*