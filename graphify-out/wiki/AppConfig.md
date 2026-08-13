# AppConfig

> 155 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **config/models/__init__.py** (24 connections) — `server/config/models/__init__.py`
- **app.py** (20 connections) — `server/config/models/app.py`
- **test_config_models.py** (19 connections) — `server/tests/unit/config/test_config_models.py`
- **GameConfig** (15 connections) — `server/config/models/game.py`
- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **_parse_env_list()** (11 connections) — `server/config/models/_helpers.py`
- **_helpers.py** (11 connections) — `server/config/models/_helpers.py`
- **LoggingConfig** (10 connections) — `server/config/models/security_logging.py`
- **TimeConfig** (9 connections) — `server/config/models/chat_time.py`
- **PlayerStatsConfig** (9 connections) — `server/config/models/player_stats.py`
- **server_db.py** (9 connections) — `server/config/models/server_db.py`
- **ChatConfig** (8 connections) — `server/config/models/chat_time.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **field_validator** (8 connections)
- **nats.py** (8 connections) — `server/config/models/nats.py`
- **SecurityConfig** (7 connections) — `server/config/models/security_logging.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **_default_cors_origins()** (7 connections) — `server/config/models/_helpers.py`
- **security_logging.py** (7 connections) — `server/config/models/security_logging.py`
- **Any** (6 connections)
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._legacy_chat_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_cors_dict()** (5 connections) — `server/config/models/app.py`
- *... and 130 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [get_config](get_config.md) (7 shared connections)
- [NATSConfig](NATSConfig.md) (6 shared connections)
- [CORSConfig](CORSConfig.md) (4 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [MythosChronicle](MythosChronicle.md) (3 shared connections)
- [test_command_factories_utility.py](test_command_factories_utility.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [error_handling_middleware.py](error_handling_middleware.py.md) (1 shared connections)

## Source Files

- `server/config/models/__init__.py`
- `server/config/models/_helpers.py`
- `server/config/models/app.py`
- `server/config/models/chat_time.py`
- `server/config/models/game.py`
- `server/config/models/nats.py`
- `server/config/models/player_stats.py`
- `server/config/models/security_logging.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_models.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 264 (94%)
- INFERRED: 17 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*