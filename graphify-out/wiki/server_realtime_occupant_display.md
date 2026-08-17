# server realtime occupant display

> 90 nodes

## Key Concepts

- **test_websocket_room_updates.py** (35 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **websocket_room_updates.py** (30 connections) — `server/realtime/websocket_room_updates.py`
- **asyncio** (24 connections)
- **broadcast_room_update()** (21 connections) — `server/realtime/websocket_room_updates.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **occupant_display.py** (11 connections) — `server/realtime/occupant_display.py`
- **format_occupant_display_name()** (10 connections) — `server/realtime/occupant_display.py`
- **convert_uuids_to_strings()** (9 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_build_event.py** (7 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **_apply_grace_badges()** (6 connections) — `server/realtime/occupant_display.py`
- **test_broadcast_room_update_fallback_npc_method()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **_resolve_room_with_fallback()** (4 connections) — `server/realtime/websocket_room_updates.py`
- **test_build_room_update_event()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_broadcast_room_update_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_build_room_update_event()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- *... and 65 more nodes in this community*

## Relationships

- [server realtime websocket handler](server_realtime_websocket_handler.md) (10 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (6 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (5 shared connections)
- [server commands look room](server_commands_look_room.md) (3 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (3 shared connections)
- [attributeerror](attributeerror.md) (3 shared connections)
- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (2 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (2 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (2 shared connections)

## Source Files

- `server/realtime/occupant_display.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`

## Audit Trail

- EXTRACTED: 212 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*