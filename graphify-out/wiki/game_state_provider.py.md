# game_state_provider.py

> 55 nodes

## Key Concepts

- **game_state_provider.py** (28 connections) — `server/realtime/integration/game_state_provider.py`
- **build_room_update_event()** (21 connections) — `server/realtime/room_update_event_builder.py`
- **room_viewer_fanout.py** (20 connections) — `server/realtime/room_viewer_fanout.py`
- **get_viewer_phantom_names()** (13 connections) — `server/services/phantom_visibility.py`
- **send_personalized_room_events()** (11 connections) — `server/realtime/room_viewer_fanout.py`
- **room_has_hallucinating_viewer()** (10 connections) — `server/services/phantom_visibility.py`
- **phantom_visibility.py** (10 connections) — `server/services/phantom_visibility.py`
- **test_phantom_visibility.py** (9 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **send_personalized_occupants_update()** (8 connections) — `server/realtime/room_viewer_fanout.py`
- **test_websocket_room_updates_build_event.py** (8 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **RoomOccupancyPayload** (7 connections) — `server/realtime/room_update_event_builder.py`
- **._send_room_occupants_update_internal()** (5 connections) — `server/realtime/event_handler.py`
- **server/realtime/integration/__init__.py** (5 connections) — `server/realtime/integration/__init__.py`
- **test_build_room_update_event()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_build_room_update_event_hallucinates_exits_for_deranged_viewer()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_build_room_update_event_no_viewer_id_leaves_exits_untouched()** (4 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **.send_room_occupants_update()** (3 connections) — `server/realtime/event_handler.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- **test_get_viewer_phantom_names_matches_own_room()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_get_viewer_phantom_names_no_viewer_or_room()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_room_has_hallucinating_viewer_false_when_no_phantoms_or_deranged()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_room_has_hallucinating_viewer_true_when_any_player_has_phantoms()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_room_has_hallucinating_viewer_true_when_any_player_is_deranged()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **asyncio** (3 connections)
- **mock_room()** (2 connections) — `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- *... and 30 more nodes in this community*

## Relationships

- [build_event](build_event.md) (19 shared connections)
- [event_handler.py](event_handler.py.md) (9 shared connections)
- [look_command.py](look_command.py.md) (6 shared connections)
- [GameStateProvider](GameStateProvider.md) (5 shared connections)
- [ConnectionManager](ConnectionManager.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [get_hallucinated_exits](get_hallucinated_exits.md) (3 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (2 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/integration/__init__.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/room_update_event_builder.py`
- `server/realtime/room_viewer_fanout.py`
- `server/services/phantom_visibility.py`
- `server/tests/unit/realtime/test_websocket_room_updates_build_event.py`
- `server/tests/unit/services/test_phantom_visibility.py`

## Audit Trail

- EXTRACTED: 144 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*