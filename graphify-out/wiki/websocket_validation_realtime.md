# websocket validation realtime

> 37 nodes

## Key Concepts

- **__init__.py** (24 connections) — `server/config/models/__init__.py`
- **app.py** (20 connections) — `server/config/models/app.py`
- **LoggingConfig** (10 connections) — `server/config/models/security_logging.py`
- **TimeConfig** (9 connections) — `server/config/models/chat_time.py`
- **server_db.py** (9 connections) — `server/config/models/server_db.py`
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
- *... and 12 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (9 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (8 shared connections)
- [config models rationale](config_models_rationale.md) (5 shared connections)
- [config models cors](config_models_cors.md) (4 shared connections)
- [realtime message filtering](realtime_message_filtering.md) (3 shared connections)
- [services passive lucidity](services_passive_lucidity.md) (3 shared connections)
- [room validator path](room_validator_path.md) (3 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [calendar models rationale](calendar_models_rationale.md) (1 shared connections)

## Source Files

- `server/config/models/__init__.py`
- `server/config/models/app.py`
- `server/config/models/chat_time.py`
- `server/config/models/game.py`
- `server/config/models/player_stats.py`
- `server/config/models/security_logging.py`
- `server/config/models/server_db.py`

## Audit Trail

- EXTRACTED: 137 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*