# server config init create config

> 235 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **CORSConfig** (31 connections) — `server/config/models/cors.py`
- **config/models/__init__.py** (28 connections) — `server/config/models/__init__.py`
- **NATSServicePoolMixin** (26 connections) — `server/services/nats_service_pool.py`
- **app.py** (21 connections) — `server/config/models/app.py`
- **test_config_models.py** (20 connections) — `server/tests/unit/config/test_config_models.py`
- **GameConfig** (15 connections) — `server/config/models/game.py`
- **NATSConfig** (15 connections) — `server/config/models/nats.py`
- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **nats_service_pool.py** (14 connections) — `server/services/nats_service_pool.py`
- **test_cors_config.py** (14 connections) — `server/tests/unit/config/test_cors_config.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **nats.py** (11 connections) — `server/config/models/nats.py`
- **LoggingConfig** (10 connections) — `server/config/models/security_logging.py`
- **._parse_csv()** (10 connections) — `server/config/models/cors.py`
- **PlayerStatsConfig** (9 connections) — `server/config/models/player_stats.py`
- **NatsConnectOptions** (9 connections) — `server/services/nats_service_connect.py`
- **cors.py** (9 connections) — `server/config/models/cors.py`
- **nats_service_connect.py** (9 connections) — `server/services/nats_service_connect.py`
- **ChatConfig** (8 connections) — `server/config/models/chat_time.py`
- **._flush_batch()** (8 connections) — `server/services/nats_service_pool.py`
- **.publish_with_pool()** (8 connections) — `server/services/nats_service_pool.py`
- **field_validator** (8 connections)
- **SecurityConfig** (7 connections) — `server/config/models/security_logging.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- *... and 210 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (23 shared connections)
- [server config models helpers apply](server_config_models_helpers_apply.md) (13 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (6 shared connections)
- [holidayresolver](holidayresolver.md) (5 shared connections)
- [baseexception](baseexception.md) (5 shared connections)
- [server infrastructure message broker](server_infrastructure_message_broker.md) (4 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (3 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)
- [scripts generate openapi spec](scripts_generate_openapi_spec.md) (2 shared connections)
- [server tests unit infrastructure test](server_tests_unit_infrastructure_test.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [server config models chat time](server_config_models_chat_time.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/__init__.py`
- `server/config/models/app.py`
- `server/config/models/chat_time.py`
- `server/config/models/cors.py`
- `server/config/models/game.py`
- `server/config/models/nats.py`
- `server/config/models/player_stats.py`
- `server/config/models/security_logging.py`
- `server/config/models/server_db.py`
- `server/services/nats_service_connect.py`
- `server/services/nats_service_pool.py`
- `server/tests/unit/config/test_config_models.py`
- `server/tests/unit/config/test_cors_config.py`

## Audit Trail

- EXTRACTED: 418 (95%)
- INFERRED: 24 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*