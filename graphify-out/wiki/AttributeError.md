# AttributeError

> 167 nodes

## Key Concepts

- **AttributeError** (47 connections)
- **websocket_room_updates.py** (40 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (37 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **broadcast_room_update()** (30 connections) — `server/realtime/websocket_room_updates.py`
- **room_update_event_builder.py** (25 connections) — `server/realtime/room_update_event_builder.py`
- **build_room_update_event()** (22 connections) — `server/realtime/room_update_event_builder.py`
- **room_viewer_fanout.py** (22 connections) — `server/realtime/room_viewer_fanout.py`
- **asyncio** (21 connections)
- **get_viewer_phantom_occupants()** (15 connections) — `server/services/phantom_visibility.py`
- **phantom_visibility.py** (15 connections) — `server/services/phantom_visibility.py`
- **get_npc_occupants()** (14 connections) — `server/realtime/websocket_room_updates.py`
- **send_personalized_room_events()** (12 connections) — `server/realtime/room_viewer_fanout.py`
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_fanout.py** (12 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **get_npc_name_from_instance()** (11 connections) — `server/realtime/websocket_helpers.py`
- **room_has_hallucinating_viewer()** (10 connections) — `server/services/phantom_visibility.py`
- **RoomOccupancyPayload** (9 connections) — `server/realtime/room_update_event_builder.py`
- **send_personalized_occupants_update()** (9 connections) — `server/realtime/room_viewer_fanout.py`
- **test_phantom_visibility.py** (9 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **connection_manager_from_running_app()** (8 connections) — `server/realtime/running_app.py`
- **_looks_like_player_uuid()** (8 connections) — `server/realtime/websocket_room_updates.py`
- **test_broadcast_room_update_personalizes_for_hallucinating_viewer()** (8 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **test_websocket_room_updates_build_event.py** (8 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **_broadcast_full_room_update()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- *... and 142 more nodes in this community*

## Relationships

- [NpcDisposition](NpcDisposition.md) (24 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [build_event](build_event.md) (9 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (8 shared connections)
- [event_handler.py](event_handler.py.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [test_room_renderer.py](test_room_renderer.py.md) (5 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [get_hallucinated_exits](get_hallucinated_exits.md) (3 shared connections)
- [test_websocket_handler_commands.py](test_websocket_handler_commands.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (3 shared connections)

## Source Files

- `server/realtime/room_update_event_builder.py`
- `server/realtime/room_viewer_fanout.py`
- `server/realtime/running_app.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/phantom_visibility.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/realtime/test_npc_disposition_wire.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- `server/tests/unit/services/test_phantom_visibility.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 374 (86%)
- INFERRED: 62 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*