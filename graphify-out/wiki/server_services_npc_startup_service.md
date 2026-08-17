# server services npc startup service

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

- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (3 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (3 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (3 shared connections)
- [draft7validator](draft7validator.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [server services container websocket events](server_services_container_websocket_events.md) (2 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (2 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (1 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_container_websocket_events.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 212 (83%)
- INFERRED: 43 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*