# .check and interrupt rest()

> 80 nodes

## Key Concepts

- **websocket_room_updates.py** (35 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (32 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **broadcast_room_update()** (24 connections) — `server/realtime/websocket_room_updates.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_player_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **update_player_room_subscription()** (8 connections) — `server/realtime/websocket_room_updates.py`
- **UUID** (6 connections)
- **_decorate_occupant_name()** (6 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_build_event.py** (6 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **_resolve_room_with_fallback()** (5 connections) — `server/realtime/websocket_room_updates.py`
- **_parse_occupant_player_id()** (4 connections) — `server/realtime/websocket_room_updates.py`
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
- *... and 55 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (6 shared connections)
- [circuit breaker](circuit_breaker.md) (6 shared connections)
- [login grace period](login_grace_period.md) (6 shared connections)
- [test build room drop summary](test_build_room_drop_summary.md) (5 shared connections)
- [get current tick()](get_current_tick%28%29.md) (4 shared connections)
- [create access token()](create_access_token%28%29.md) (3 shared connections)
- [message formatters](message_formatters.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [command admin](command_admin.md) (2 shared connections)
- [.reset instance()](reset_instance%28%29.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [world](world.md) (2 shared connections)

## Source Files

- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`

## Audit Trail

- EXTRACTED: 297 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*