# AttributeError

> 218 nodes

## Key Concepts

- **AttributeError** (38 connections)
- **websocket_helpers.py** (37 connections) — `server/realtime/websocket_helpers.py`
- **test_websocket_helpers.py** (36 connections) — `server/tests/unit/realtime/test_websocket_helpers.py`
- **websocket_room_updates.py** (32 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (32 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **broadcast_room_update()** (23 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_helpers_player.py** (23 connections) — `server/tests/unit/realtime/test_websocket_helpers_player.py`
- **asyncio** (22 connections)
- **get_player_and_room()** (14 connections) — `server/realtime/websocket_helpers.py`
- **validate_occupant_name()** (14 connections) — `server/realtime/websocket_helpers.py`
- **build_room_update_event()** (13 connections) — `server/realtime/websocket_room_updates.py`
- **check_shutdown_and_reject()** (12 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_name_from_instance()** (12 connections) — `server/realtime/websocket_helpers.py`
- **prepare_player_data()** (12 connections) — `server/realtime/websocket_helpers.py`
- **convert_uuids_to_strings()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_occupant_names()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_occupants_from_lifecycle_manager()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **get_player_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **lifespan_event_subscriptions.py** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **get_player_stats_data()** (9 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_occupants_fallback()** (9 connections) — `server/realtime/websocket_room_updates.py`
- **asyncio** (9 connections)
- **get_player_service_from_connection_manager()** (8 connections) — `server/realtime/websocket_helpers.py`
- **build_basic_player_data()** (7 connections) — `server/realtime/websocket_helpers.py`
- **convert_schema_to_dict()** (7 connections) — `server/realtime/websocket_helpers.py`
- *... and 193 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (13 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (13 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (7 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (6 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [test_room_renderer.py](test_room_renderer.py.md) (5 shared connections)
- [test_users.py](test_users.py.md) (4 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (3 shared connections)

## Source Files

- `server/app/lifespan_event_subscriptions.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/realtime/test_websocket_helpers.py`
- `server/tests/unit/realtime/test_websocket_helpers_player.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/services/test_room_sync_service.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 447 (91%)
- INFERRED: 45 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*