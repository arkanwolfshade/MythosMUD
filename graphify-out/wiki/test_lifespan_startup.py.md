# test_lifespan_startup.py

> 70 nodes

## Key Concepts

- **test_lifespan_startup.py** (43 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **asyncio** (18 connections)
- **FastAPI** (16 connections)
- **initialize_container_and_legacy_services()** (15 connections) — `server/app/lifespan_startup.py`
- **initialize_combat_services()** (12 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_mythos_time_consumer()** (9 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_entries()** (7 connections) — `server/app/lifespan_startup.py`
- **_validate_npc_services_prerequisites()** (7 connections) — `server/app/lifespan_startup.py`
- **_get_item_prototype_count()** (6 connections) — `server/app/lifespan_startup.py`
- **test_setup_connection_manager()** (6 connections) — `server/tests/unit/app/test_lifespan_startup.py`
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
- *... and 45 more nodes in this community*

## Relationships

- [lifespan_startup.py](lifespan_startup.py.md) (29 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (7 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (3 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (1 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)
- [models/player.py](models-player.py.md) (1 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (1 shared connections)
- [test_passive_lucidity_flux_service.py](test_passive_lucidity_flux_service.py.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/tests/unit/app/test_lifespan_startup.py`

## Audit Trail

- EXTRACTED: 172 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*