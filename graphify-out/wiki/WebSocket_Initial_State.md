# WebSocket Initial State

> 73 nodes

## Key Concepts

- **websocket_room_updates.py** (32 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (32 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **get_player_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_build_event.py** (6 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **_resolve_room_with_fallback()** (4 connections) — `server/realtime/websocket_room_updates.py`
- **test_get_player_occupants_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_fallback_npc_method()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_empty()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_filters_dead()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_wrong_room()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_no_service()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fallback_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fallback_filters_dead()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fallback_no_service()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_build_room_update_event()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_build_room_update_event_with_drops()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_update_player_room_subscription_success()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- *... and 48 more nodes in this community*

## Relationships

- [Party Service Management](Party_Service_Management.md) (5 shared connections)
- [Look Display Helpers](Look_Display_Helpers.md) (5 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (4 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (3 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (3 shared connections)
- [API Type Guards](API_Type_Guards.md) (3 shared connections)
- [Player Combat XP](Player_Combat_XP.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`

## Audit Trail

- EXTRACTED: 260 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*