# NPCStartupService

> 109 nodes

## Key Concepts

- **NPCStartupService** (52 connections) — `server/services/npc_startup_service.py`
- **test_npc_startup_service.py** (40 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **asyncio** (26 connections)
- **npc_startup_service.py** (21 connections) — `server/services/npc_startup_service.py`
- **Any** (16 connections)
- **mock_container()** (13 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **_assign_container_get_instance()** (12 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **get_npc_startup_service()** (8 connections) — `server/services/npc_startup_service.py`
- **._determine_spawn_room()** (8 connections) — `server/services/npc_startup_service.py`
- **._spawn_required_npcs()** (8 connections) — `server/services/npc_startup_service.py`
- **._run_startup_pass()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_arena_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **_errors_len()** (7 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **.spawn_npcs_on_startup()** (6 connections) — `server/services/npc_startup_service.py`
- **test_determine_spawn_room_exception()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback_not_found()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_container()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_persistence()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_room_id_not_found()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_sub_zone_room_not_found()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_with_room_id()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_with_sub_zone()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **_new_spawn_results()** (5 connections) — `server/services/npc_startup_service.py`
- *... and 84 more nodes in this community*

## Relationships

- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [.get_instance](get_instance.md) (3 shared connections)
- [npc_database.py](npc_database.py.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (2 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_container_websocket_events.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 213 (84%)
- INFERRED: 42 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*