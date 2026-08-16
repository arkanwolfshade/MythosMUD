# NATSSubjectManager

> 228 nodes

## Key Concepts

- **NATSSubjectManager** (58 connections) — `server/services/nats_subject_manager/manager.py`
- **nats_service.py** (33 connections) — `server/services/nats_service.py`
- **AppConfig** (31 connections) — `server/config/models/app.py`
- **config/models/__init__.py** (27 connections) — `server/config/models/__init__.py`
- **app.py** (21 connections) — `server/config/models/app.py`
- **server/services/nats_subject_manager/__init__.py** (21 connections) — `server/services/nats_subject_manager/__init__.py`
- **nats_service_pool.py** (20 connections) — `server/services/nats_service_pool.py`
- **test_config_models.py** (20 connections) — `server/tests/unit/config/test_config_models.py`
- **SubjectManagerMetrics** (16 connections) — `server/services/nats_subject_manager/metrics.py`
- **GameConfig** (15 connections) — `server/config/models/game.py`
- **event_publisher.py** (15 connections) — `server/realtime/event_publisher.py`
- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **PatternMatcher** (13 connections) — `server/services/nats_subject_manager/pattern_matcher.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **_parse_env_list()** (12 connections) — `server/config/models/_helpers.py`
- **_helpers.py** (12 connections) — `server/config/models/_helpers.py`
- **test_config_model_helpers.py** (12 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **nats.py** (11 connections) — `server/config/models/nats.py`
- **LoggingConfig** (10 connections) — `server/config/models/security_logging.py`
- **server_db.py** (10 connections) — `server/config/models/server_db.py`
- **TimeConfig** (9 connections) — `server/config/models/chat_time.py`
- **PlayerStatsConfig** (9 connections) — `server/config/models/player_stats.py`
- **_default_cors_origins()** (9 connections) — `server/config/models/_helpers.py`
- **ChatConfig** (8 connections) — `server/config/models/chat_time.py`
- **_apply_url_fallback()** (8 connections) — `server/config/models/_helpers.py`
- *... and 203 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (26 shared connections)
- [SubjectValidator](SubjectValidator.md) (12 shared connections)
- [NATSConfig](NATSConfig.md) (11 shared connections)
- [subject_controller.py](subject_controller.py.md) (11 shared connections)
- [CombatInstance](CombatInstance.md) (10 shared connections)
- [test_manager.py](test_manager.py.md) (9 shared connections)
- [.build_subject](build_subject.md) (8 shared connections)
- [BaseCommand](BaseCommand.md) (7 shared connections)
- [PatternNotFoundError](PatternNotFoundError.md) (6 shared connections)
- [test_pattern_matcher.py](test_pattern_matcher.py.md) (6 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (5 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (5 shared connections)

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
- `server/realtime/event_publisher.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/services/nats_service_pool.py`
- `server/services/nats_subject_manager/__init__.py`
- `server/services/nats_subject_manager/manager.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/services/nats_subject_manager/pattern_matcher.py`
- `server/tests/unit/config/test_config_model_helpers.py`

## Audit Trail

- EXTRACTED: 492 (94%)
- INFERRED: 31 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*