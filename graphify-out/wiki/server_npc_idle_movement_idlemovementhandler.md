# server npc idle movement idlemovementhandler

> 49 nodes

## Key Concepts

- **NPCMovementIntegration** (50 connections) — `server/npc/movement_integration.py`
- **test_movement_integration.py** (30 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **.__init__()** (5 connections) — `server/npc/idle_movement.py`
- **.__init__()** (5 connections) — `server/npc/movement_integration.py`
- **._get_destination_subzone()** (4 connections) — `server/npc/movement_integration.py`
- **.validate_subzone_boundary()** (3 connections) — `server/npc/movement_integration.py`
- **.find_path_between_rooms()** (2 connections) — `server/npc/movement_integration.py`
- **.get_available_exits()** (2 connections) — `server/npc/movement_integration.py`
- **.get_npc_room()** (2 connections) — `server/npc/movement_integration.py`
- **.get_room_npcs()** (2 connections) — `server/npc/movement_integration.py`
- **.validate_npc_movement()** (2 connections) — `server/npc/movement_integration.py`
- **persistence()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_find_path_direct_connection()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_find_path_returns_none_without_connection()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_available_exits_empty_when_missing()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_destination_subzone_from_room_id()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_npc_room_returns_none()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_npcs_and_exits()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_npcs_empty_when_missing()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_objects_missing_destination()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_get_room_objects_missing_room()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_init_requires_persistence()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_is_npc_in_combat_true()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_blocked_in_combat()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- **test_move_npc_exception_returns_false()** (2 connections) — `server/tests/unit/npc/test_movement_integration.py`
- *... and 24 more nodes in this community*

## Relationships

- [server npc movement integration npcmovementintegration](server_npc_movement_integration_npcmovementintegration.md) (6 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (4 shared connections)
- [server npc idle movement](server_npc_idle_movement.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (2 shared connections)
- [server npc init](server_npc_init.md) (1 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)
- [moduletype](moduletype.md) (1 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (1 shared connections)
- [server game movement service movementservice](server_game_movement_service_movementservice.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/npc/idle_movement.py`
- `server/npc/movement_integration.py`
- `server/tests/unit/npc/test_movement_integration.py`

## Audit Trail

- EXTRACTED: 70 (72%)
- INFERRED: 27 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*