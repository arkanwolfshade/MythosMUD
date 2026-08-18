# server app lifespan protocols nats

> 84 nodes

## Key Concepts

- **test_lifespan_startup.py** (43 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **asyncio** (18 connections)
- **FastAPI** (16 connections)
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **FastAPI** (13 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (6 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **test_setup_connection_manager()** (6 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **_log_npc_startup_errors()** (5 connections) — `server/app/lifespan_startup.py`
- **mock_app()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_chat_service()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_combat_services()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_async_registry()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_no_item_factory()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_legacy_service_none()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- *... and 59 more nodes in this community*

## Relationships

- [server app lifespan startup](server_app_lifespan_startup.md) (19 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (12 shared connections)
- [server app lifespan](server_app_lifespan.md) (8 shared connections)
- [server app lifespan magic](server_app_lifespan_magic.md) (3 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (2 shared connections)
- [server events combat events](server_events_combat_events.md) (2 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (2 shared connections)
- [memorymonitor](memorymonitor.md) (1 shared connections)
- [server game chat service chatservice](server_game_chat_service_chatservice.md) (1 shared connections)
- [server services combat event publisher](server_services_combat_event_publisher.md) (1 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (1 shared connections)
- [server services combat service types](server_services_combat_service_types.md) (1 shared connections)

## Source Files

- `server/app/lifespan_protocols.py`
- `server/app/lifespan_startup.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 207 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*