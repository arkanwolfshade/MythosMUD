# AppConfig

> 178 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **config/models/__init__.py** (24 connections) — `server/config/models/__init__.py`
- **app.py** (20 connections) — `server/config/models/app.py`
- **NATSConfig** (19 connections) — `server/config/models/nats.py`
- **test_config_models.py** (19 connections) — `server/tests/unit/config/test_config_models.py`
- **GameConfig** (15 connections) — `server/config/models/game.py`
- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **_parse_env_list()** (11 connections) — `server/config/models/_helpers.py`
- **server/config/__init__.py** (11 connections) — `server/config/__init__.py`
- **_helpers.py** (11 connections) — `server/config/models/_helpers.py`
- **LoggingConfig** (10 connections) — `server/config/models/security_logging.py`
- **TimeConfig** (9 connections) — `server/config/models/chat_time.py`
- **PlayerStatsConfig** (9 connections) — `server/config/models/player_stats.py`
- **server_db.py** (9 connections) — `server/config/models/server_db.py`
- **ChatConfig** (8 connections) — `server/config/models/chat_time.py`
- **field_validator** (8 connections)
- **nats.py** (8 connections) — `server/config/models/nats.py`
- **SecurityConfig** (7 connections) — `server/config/models/security_logging.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **_default_cors_origins()** (7 connections) — `server/config/models/_helpers.py`
- **security_logging.py** (7 connections) — `server/config/models/security_logging.py`
- **Any** (6 connections)
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- *... and 153 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (19 shared connections)
- [CORSConfig](CORSConfig.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (2 shared connections)
- [reset_config](reset_config.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)
- [nats_broker](nats_broker.md) (1 shared connections)
- [nats_service](nats_service.md) (1 shared connections)
- [test_nats_broker.py](test_nats_broker.py.md) (1 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [test_command_factories_utility.py](test_command_factories_utility.py.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/__init__.py`
- `server/config/models/_helpers.py`
- `server/config/models/app.py`
- `server/config/models/chat_time.py`
- `server/config/models/game.py`
- `server/config/models/nats.py`
- `server/config/models/player_stats.py`
- `server/config/models/security_logging.py`
- `server/config/models/server_db.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 306 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*