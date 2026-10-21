# security.ts

> 174 nodes · cohesion 0.02

## Key Concepts

- **AttributeError** (47 connections)
- **websocket_room_updates.py** (40 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (37 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **broadcast_room_update()** (30 connections) — `server/realtime/websocket_room_updates.py`
- **room_update_event_builder.py** (25 connections) — `server/realtime/room_update_event_builder.py`
- **build_room_update_event()** (22 connections) — `server/realtime/room_update_event_builder.py`
- **room_viewer_fanout.py** (22 connections) — `server/realtime/room_viewer_fanout.py`
- **asyncio** (21 connections)
- **phantom_visibility.py** (15 connections) — `server/services/phantom_visibility.py`
- **get_viewer_phantom_occupants()** (15 connections) — `server/services/phantom_visibility.py`
- **test_npc_disposition_wire.py** (15 connections) — `server/tests/unit/realtime/test_npc_disposition_wire.py`
- **get_npc_occupants()** (14 connections) — `server/realtime/websocket_room_updates.py`
- **send_personalized_room_events()** (12 connections) — `server/realtime/room_viewer_fanout.py`
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_fanout.py** (12 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **room_has_hallucinating_viewer()** (10 connections) — `server/services/phantom_visibility.py`
- **RoomOccupancyPayload** (9 connections) — `server/realtime/room_update_event_builder.py`
- **send_personalized_occupants_update()** (9 connections) — `server/realtime/room_viewer_fanout.py`
- **test_phantom_visibility.py** (9 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **connection_manager_from_running_app()** (8 connections) — `server/realtime/running_app.py`
- **_looks_like_player_uuid()** (8 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_build_event.py** (8 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_broadcast_room_update_personalizes_for_hallucinating_viewer()** (8 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **_broadcast_full_room_update()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- *... and 149 more nodes in this community*

## Relationships

- [look_container.py](look_container.py.md) (23 shared connections)
- [alias_storage.py](alias_storage.py.md) (11 shared connections)
- [Room](Room.md) (10 shared connections)
- [.publish_with_pool](publish_with_pool.md) (9 shared connections)
- [test_game.py](test_game.py.md) (6 shared connections)
- [ChatService](ChatService.md) (6 shared connections)
- [test_logout_commands.py](test_logout_commands.py.md) (5 shared connections)
- [ChatLogger](ChatLogger.md) (5 shared connections)
- [session](session.md) (4 shared connections)
- [test_look_container.py](test_look_container.py.md) (3 shared connections)
- [HolidayEntry](HolidayEntry.md) (3 shared connections)
- [required](required.md) (3 shared connections)

## Source Files

- `server/realtime/room_update_event_builder.py`
- `server/realtime/room_viewer_fanout.py`
- `server/realtime/running_app.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/phantom_visibility.py`
- `server/tests/unit/realtime/test_npc_disposition_wire.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- `server/tests/unit/services/test_phantom_visibility.py`
- `server/tests/unit/services/test_room_sync_service.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 384 (85%)
- INFERRED: 67 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*