# test_lifespan_startup.py

> 76 nodes

## Key Concepts

- **test_lifespan_startup.py** (41 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **asyncio** (18 connections)
- **FastAPI** (13 connections)
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (8 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_log_npc_startup_errors()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **_start_npc_thread_manager_and_pending()** (4 connections) — `server/app/lifespan_startup.py`
- **test_get_item_prototype_count_non_iterable()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_get_item_prototype_entries_async_failure()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_get_item_prototype_entries_missing_all_method()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_get_item_prototype_entries_none_registry()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_chat_service()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_combat_services()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_async_registry()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_and_legacy_services_no_item_factory()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_initialize_container_legacy_service_none()** (4 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- *... and 51 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (17 shared connections)
- [lifespan.py](lifespan.py.md) (16 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (7 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [NATSConfig](NATSConfig.md) (1 shared connections)
- [.initialize](initialize.md) (1 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (1 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 172 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*