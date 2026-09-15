# test_lifespan_startup.py

> 64 nodes

## Key Concepts

- **test_lifespan_startup.py** (42 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **asyncio** (18 connections)
- **FastAPI** (16 connections)
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (7 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (6 connections) — `server/app/lifespan_startup.py`
- **test_setup_connection_manager()** (6 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **_log_npc_startup_errors()** (5 connections) — `server/app/lifespan_startup.py`
- **mock_app()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_chat_service()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_combat_services()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_async_registry()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_no_item_factory()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_legacy_service_none()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_magic_services()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_mythos_time_consumer()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_mythos_time_consumer_missing_deps()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_nats_and_combat_services()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_npc_services()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_npc_startup_spawning()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_setup_connection_manager_no_manager()** (5 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_get_item_prototype_count_non_iterable()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_get_item_prototype_entries_async_failure()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- *... and 39 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (26 shared connections)
- [lifespan.py](lifespan.py.md) (5 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [HolidayService](HolidayService.md) (1 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (1 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 148 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*