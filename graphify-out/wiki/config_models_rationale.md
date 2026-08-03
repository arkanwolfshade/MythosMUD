# config models rationale

> 179 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **__init__.py** (24 connections) — `server/config/models/__init__.py`
- **NATSConfig** (22 connections) — `server/config/models/nats.py`
- **app.py** (20 connections) — `server/config/models/app.py`
- **test_config_models.py** (19 connections) — `server/tests/unit/config/test_config_models.py`
- **GameConfig** (15 connections) — `server/config/models/game.py`
- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **__init__.py** (11 connections) — `server/config/__init__.py`
- **_helpers.py** (11 connections) — `server/config/models/_helpers.py`
- **_parse_env_list()** (11 connections) — `server/config/models/_helpers.py`
- **LoggingConfig** (10 connections) — `server/config/models/security_logging.py`
- **TimeConfig** (9 connections) — `server/config/models/chat_time.py`
- **PlayerStatsConfig** (9 connections) — `server/config/models/player_stats.py`
- **server_db.py** (9 connections) — `server/config/models/server_db.py`
- **ChatConfig** (8 connections) — `server/config/models/chat_time.py`
- **nats.py** (8 connections) — `server/config/models/nats.py`
- **_get_combat_container_services()** (8 connections) — `server/services/combat_turn_participant_actions.py`
- **_default_cors_origins()** (7 connections) — `server/config/models/_helpers.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **security_logging.py** (7 connections) — `server/config/models/security_logging.py`
- **SecurityConfig** (7 connections) — `server/config/models/security_logging.py`
- **.__init__()** (7 connections) — `server/services/nats_service.py`
- **Any** (6 connections)
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- *... and 154 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (15 shared connections)
- [Item Instances](Item_Instances.md) (11 shared connections)
- [time service rationale](time_service_rationale.md) (5 shared connections)
- [config models cors](config_models_cors.md) (4 shared connections)
- [nats services service](nats_services_service.md) (4 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (4 shared connections)
- [config rationale reset](config_rationale_reset.md) (2 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (2 shared connections)
- [infrastructure nats broker](infrastructure_nats_broker.md) (2 shared connections)
- [manager subject services](manager_subject_services.md) (2 shared connections)
- [npc combat services](npc_combat_services.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)

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
- `server/services/combat_turn_participant_actions.py`
- `server/services/nats_service.py`
- `server/tests/unit/config/test_config_models.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 557 (96%)
- INFERRED: 24 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*