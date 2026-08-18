# server config init

> 302 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
- **AppConfig** (31 connections) — `server/config/models/app.py`
- **config/models/__init__.py** (28 connections) — `server/config/models/__init__.py`
- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- **server/config/__init__.py** (26 connections) — `server/config/__init__.py`
- **NPCCombatIntegrationBase** (25 connections) — `server/npc/combat_integration_base.py`
- **combat_integration_base.py** (23 connections) — `server/npc/combat_integration_base.py`
- **app.py** (21 connections) — `server/config/models/app.py`
- **test_config_models.py** (20 connections) — `server/tests/unit/config/test_config_models.py`
- **GameConfig** (15 connections) — `server/config/models/game.py`
- **DatabaseConfig** (14 connections) — `server/config/models/server_db.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **_parse_env_list()** (12 connections) — `server/config/models/_helpers.py`
- **_helpers.py** (12 connections) — `server/config/models/_helpers.py`
- **test_config_model_helpers.py** (12 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **nats.py** (11 connections) — `server/config/models/nats.py`
- **LoggingConfig** (10 connections) — `server/config/models/security_logging.py`
- **._perform_direct_npc_attack()** (10 connections) — `server/npc/combat_integration_base.py`
- **server_db.py** (10 connections) — `server/config/models/server_db.py`
- **TimeConfig** (9 connections) — `server/config/models/chat_time.py`
- **PlayerStatsConfig** (9 connections) — `server/config/models/player_stats.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **_default_cors_origins()** (9 connections) — `server/config/models/_helpers.py`
- **cors.py** (9 connections) — `server/config/models/cors.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- *... and 277 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (29 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (9 shared connections)
- [server npc combat integration npccombatintegration](server_npc_combat_integration_npccombatintegration.md) (8 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (8 shared connections)
- [server services aggro threat](server_services_aggro_threat.md) (7 shared connections)
- [server events combat events](server_events_combat_events.md) (7 shared connections)
- [server config models nats natsconfig](server_config_models_nats_natsconfig.md) (6 shared connections)
- [server config models cors corsconfig](server_config_models_cors_corsconfig.md) (6 shared connections)
- [server models combat](server_models_combat.md) (5 shared connections)
- [server services combat configuration service](server_services_combat_configuration_service.md) (5 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (4 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (4 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/__init__.py`
- `server/config/models/_helpers.py`
- `server/config/models/app.py`
- `server/config/models/chat_time.py`
- `server/config/models/cors.py`
- `server/config/models/game.py`
- `server/config/models/nats.py`
- `server/config/models/player_stats.py`
- `server/config/models/security_logging.py`
- `server/config/models/server_db.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_base.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/user_manager.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/config/test_config_model_helpers.py`
- `server/tests/unit/config/test_config_models.py`
- `server/tests/unit/test_config_smoke.py`

## Audit Trail

- EXTRACTED: 650 (98%)
- INFERRED: 16 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*