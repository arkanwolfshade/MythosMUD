# player event handlers

> 62 nodes

## Key Concepts

- **AppConfig** (31 connections) — `server/config/models/app.py`
- **__init__.py** (11 connections) — `server/config/__init__.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
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
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **test_get_config_returns_app_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_test_mode_returns_fresh_instances()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_server_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- **test_get_config_has_game_config()** (3 connections) — `server/tests/unit/config/test_config.py`
- *... and 37 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (20 shared connections)
- [command inventory factories](command_inventory_factories.md) (9 shared connections)
- [conftest rationale Item](conftest_rationale_Item.md) (2 shared connections)
- [config models cors](config_models_cors.md) (2 shared connections)
- [invite models rationale](invite_models_rationale.md) (2 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (1 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (1 shared connections)
- [persistence container parse](persistence_container_parse.md) (1 shared connections)
- [config models rationale](config_models_rationale.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`

## Audit Trail

- EXTRACTED: 193 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*