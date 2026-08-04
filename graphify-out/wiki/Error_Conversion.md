# Error Conversion

> 87 nodes

## Key Concepts

- **ApplicationContainer** (151 connections) — `server/container/main.py`
- **.get_instance()** (35 connections) — `server/container/main.py`
- **main.py** (34 connections) — `server/container/main.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **realtime.py** (13 connections) — `server/container/bundles/realtime.py`
- **monitoring.py** (12 connections) — `server/container/bundles/monitoring.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **__init__.py** (7 connections) — `server/container/__init__.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **_flatten_bundle()** (6 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **test_get_and_reset_container_helpers()** (5 connections) — `server/tests/unit/container/test_application_container_main.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_reset_container()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_get_container_singleton()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container_creates_new_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_reset_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **.__init__()** (3 connections) — `server/container/main.py`
- **mock_request()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **test_get_container()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_is_initialized()** (3 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_service()** (3 connections) — `server/tests/unit/test_application_container.py`
- *... and 62 more nodes in this community*

## Relationships

- [nats services service](nats_services_service.md) (40 shared connections)
- [player death service](player_death_service.md) (14 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (12 shared connections)
- [models npc rationale](models_npc_rationale.md) (12 shared connections)
- [Loot Generation](Loot_Generation.md) (8 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (7 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (6 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (6 shared connections)
- [fixtures mock helpers](fixtures_mock_helpers.md) (4 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (4 shared connections)
- [npc shopkeeper rationale](npc_shopkeeper_rationale.md) (4 shared connections)
- [command base models](command_base_models.md) (4 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/main.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 467 (96%)
- INFERRED: 19 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*