# build_event

> 95 nodes

## Key Concepts

- **AttributeError** (44 connections)
- **test_websocket_room_updates.py** (35 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **websocket_room_updates.py** (26 connections) — `server/realtime/websocket_room_updates.py`
- **asyncio** (24 connections)
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **get_player_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **build_room_update_event()** (10 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_from_lifecycle_manager()** (10 connections) — `server/realtime/websocket_room_updates.py`
- **get_npc_occupants_fallback()** (8 connections) — `server/realtime/websocket_room_updates.py`
- **connection_manager_from_running_app()** (7 connections) — `server/realtime/running_app.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_build_event.py** (7 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_broadcast_room_update_fallback_npc_method()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_from_lifecycle_manager_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **running_app.py** (5 connections) — `server/realtime/running_app.py`
- **_resolve_room_with_fallback()** (4 connections) — `server/realtime/websocket_room_updates.py`
- **test_build_room_update_event()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_broadcast_room_update_handles_exception()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_room_not_found()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_broadcast_room_update_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_build_room_update_event()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_build_room_update_event_with_drops()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- *... and 70 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (6 shared connections)
- [CombatAuditLogger](CombatAuditLogger.md) (5 shared connections)
- [test_goto_helpers.py](test_goto_helpers.py.md) (3 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (2 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (2 shared connections)
- [test_logging_handlers.py](test_logging_handlers.py.md) (2 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (2 shared connections)
- [test_status_commands.py](test_status_commands.py.md) (2 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (2 shared connections)

## Source Files

- `server/realtime/running_app.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/services/test_room_sync_service.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 192 (81%)
- INFERRED: 44 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*