# mock_container

> 25 nodes

## Key Concepts

- **mock_container()** (12 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **_assign_container_get_instance()** (12 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_exception()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback_not_found()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_container()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_persistence()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_room_id_not_found()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_sub_zone_room_not_found()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_with_room_id()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_with_sub_zone()** (6 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **fixture** (2 connections)
- **Create mock connection manager.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Create mock container.** (1 connections) — `server/tests/unit/services/test_container_websocket_events.py`
- **Test _determine_spawn_room() uses NPC's room_id when available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() uses sub_zone default when room_id not available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() uses fallback room when no other option.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Attach a typed get_instance mock to a patched ApplicationContainer.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() returns None when persistence not available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles room_id not found in database.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles sub-zone default room not found.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() returns None when fallback room not found.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles None container.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [asyncio](asyncio.md) (10 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (10 shared connections)
- [NPCStartupService](NPCStartupService.md) (9 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (2 shared connections)

## Source Files

- `server/tests/unit/services/test_container_websocket_events.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 77 (81%)
- INFERRED: 18 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*