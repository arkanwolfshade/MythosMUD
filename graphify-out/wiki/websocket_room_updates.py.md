# websocket_room_updates.py

> 110 nodes

## Key Concepts

- **websocket_room_updates.py** (37 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (35 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **broadcast_room_update()** (30 connections) — `server/realtime/websocket_room_updates.py`
- **build_room_update_event()** (21 connections) — `server/realtime/room_update_event_builder.py`
- **asyncio** (21 connections)
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_fanout.py** (12 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **send_personalized_room_events()** (11 connections) — `server/realtime/room_viewer_fanout.py`
- **get_npc_name_from_instance()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **RoomOccupancyPayload** (9 connections) — `server/realtime/room_update_event_builder.py`
- **_looks_like_player_uuid()** (8 connections) — `server/realtime/websocket_room_updates.py`
- **test_broadcast_room_update_personalizes_for_hallucinating_viewer()** (8 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **_broadcast_full_room_update()** (6 connections) — `server/realtime/websocket_room_updates.py`
- **_broadcast_occupants_event()** (6 connections) — `server/realtime/websocket_room_updates.py`
- **_resolve_broadcast_connection_manager()** (5 connections) — `server/realtime/websocket_room_updates.py`
- **_resolve_room_with_fallback()** (5 connections) — `server/realtime/websocket_room_updates.py`
- **test_broadcast_room_update_no_hallucinators_uses_broadcast()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **test_broadcast_room_update_propagates_subscription_error()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_npc_occupants_fails_closed_on_lookup_error()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **test_get_player_occupants_handles_exception()** (5 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **_make_mock_room()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **mock_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **_setup_hallucinating_room()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- *... and 85 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (7 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [get_viewer_phantom_names](get_viewer_phantom_names.md) (5 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (5 shared connections)
- [test_websocket_room_updates_build_event.py](test_websocket_room_updates_build_event.py.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [CorruptionTier](CorruptionTier.md) (3 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [test_room_renderer.py](test_room_renderer.py.md) (2 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (2 shared connections)

## Source Files

- `server/realtime/room_update_event_builder.py`
- `server/realtime/room_viewer_fanout.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`

## Audit Trail

- EXTRACTED: 245 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*