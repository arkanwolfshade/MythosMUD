# websocket_room_updates.py

> 153 nodes

## Key Concepts

- **websocket_room_updates.py** (37 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates.py** (35 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **game_state_provider.py** (31 connections) — `server/realtime/integration/game_state_provider.py`
- **broadcast_room_update()** (30 connections) — `server/realtime/websocket_room_updates.py`
- **room_update_event_builder.py** (23 connections) — `server/realtime/room_update_event_builder.py`
- **build_room_update_event()** (21 connections) — `server/realtime/room_update_event_builder.py`
- **asyncio** (21 connections)
- **room_viewer_fanout.py** (20 connections) — `server/realtime/room_viewer_fanout.py`
- **get_viewer_phantom_names()** (13 connections) — `server/services/phantom_visibility.py`
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **test_websocket_room_updates_fanout.py** (12 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **send_personalized_room_events()** (11 connections) — `server/realtime/room_viewer_fanout.py`
- **get_npc_name_from_instance()** (11 connections) — `server/realtime/websocket_helpers.py`
- **get_npc_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **room_has_hallucinating_viewer()** (10 connections) — `server/services/phantom_visibility.py`
- **phantom_visibility.py** (10 connections) — `server/services/phantom_visibility.py`
- **RoomOccupancyPayload** (9 connections) — `server/realtime/room_update_event_builder.py`
- **test_phantom_visibility.py** (9 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **send_personalized_occupants_update()** (8 connections) — `server/realtime/room_viewer_fanout.py`
- **_looks_like_player_uuid()** (8 connections) — `server/realtime/websocket_room_updates.py`
- **test_broadcast_room_update_personalizes_for_hallucinating_viewer()** (8 connections) — `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- **lucidity_tier_cache.py** (8 connections) — `server/services/lucidity_tier_cache.py`
- **test_websocket_room_updates_build_event.py** (8 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **update_player_room_subscription()** (7 connections) — `server/realtime/websocket_room_updates.py`
- **_broadcast_full_room_update()** (6 connections) — `server/realtime/websocket_room_updates.py`
- *... and 128 more nodes in this community*

## Relationships

- [build_event](build_event.md) (11 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_look_room.py](test_look_room.py.md) (9 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (8 shared connections)
- [ConnectionManager](ConnectionManager.md) (8 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (7 shared connections)
- [NPCDefinition](NPCDefinition.md) (6 shared connections)
- [GameStateProvider](GameStateProvider.md) (6 shared connections)
- [connection_manager.py](connection_manager.py.md) (6 shared connections)
- [test_room_renderer.py](test_room_renderer.py.md) (5 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (3 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/room_update_event_builder.py`
- `server/realtime/room_viewer_fanout.py`
- `server/realtime/websocket_helpers.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/lucidity_tier_cache.py`
- `server/services/phantom_visibility.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/realtime/test_websocket_room_updates_fanout.py`
- `server/tests/unit/services/test_phantom_visibility.py`

## Audit Trail

- EXTRACTED: 369 (97%)
- INFERRED: 13 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*