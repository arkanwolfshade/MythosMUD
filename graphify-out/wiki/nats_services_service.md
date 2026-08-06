# nats services service

> 95 nodes

## Key Concepts

- **ApplicationContainer** (151 connections) — `server/container/main.py`
- **main.py** (34 connections) — `server/container/main.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **combat.py** (14 connections) — `server/container/bundles/combat.py`
- **realtime.py** (13 connections) — `server/container/bundles/realtime.py`
- **monitoring.py** (12 connections) — `server/container/bundles/monitoring.py`
- **chat.py** (11 connections) — `server/container/bundles/chat.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **__init__.py** (8 connections) — `server/tests/fixtures/unit/__init__.py`
- **__init__.py** (7 connections) — `server/container/__init__.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **test_get_and_reset_container_helpers()** (5 connections) — `server/tests/unit/container/test_application_container_main.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **dummy_request()** (4 connections) — `server/tests/fixtures/unit/__init__.py`
- **test_reset_container()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_get_container_singleton()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_reset_container_creates_new_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_reset_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_container()** (3 connections) — `server/tests/fixtures/unit/__init__.py`
- *... and 70 more nodes in this community*

## Relationships

- [websocket realtime handler](websocket_realtime_handler.md) (42 shared connections)
- [Error Conversion](Error_Conversion.md) (30 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (13 shared connections)
- [dead letter queue](dead_letter_queue.md) (11 shared connections)
- [aggro threat services](aggro_threat_services.md) (9 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (8 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (6 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (6 shared connections)
- [player respawn event](player_respawn_event.md) (5 shared connections)
- [realtime player connection](realtime_player_connection.md) (5 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (4 shared connections)
- [command base models](command_base_models.md) (4 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/combat.py`
- `server/container/bundles/magic.py`
- `server/container/bundles/monitoring.py`
- `server/container/bundles/realtime.py`
- `server/container/main.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 504 (96%)
- INFERRED: 20 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*