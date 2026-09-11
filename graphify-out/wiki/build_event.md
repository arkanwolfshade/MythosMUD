# build_event

> 249 nodes

## Key Concepts

- **build_event()** (117 connections) — `server/realtime/envelope.py`
- **.state()** (39 connections) — `server/realtime/connection_state_machine.py`
- **test_websocket_room_updates.py** (35 connections) — `server/tests/unit/realtime/test_websocket_room_updates.py`
- **websocket_room_updates.py** (34 connections) — `server/realtime/websocket_room_updates.py`
- **envelope.py** (32 connections) — `server/realtime/envelope.py`
- **broadcast_room_update()** (31 connections) — `server/realtime/websocket_room_updates.py`
- **GameStateProvider** (30 connections) — `server/realtime/integration/game_state_provider.py`
- **game_state_provider.py** (28 connections) — `server/realtime/integration/game_state_provider.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **asyncio** (21 connections)
- **room_viewer_fanout.py** (20 connections) — `server/realtime/room_viewer_fanout.py`
- **websocket_handler_connection.py** (18 connections) — `server/realtime/websocket_handler_connection.py`
- **.send_initial_game_state()** (14 connections) — `server/realtime/integration/game_state_provider.py`
- **UUID** (14 connections)
- **get_viewer_phantom_names()** (13 connections) — `server/services/phantom_visibility.py`
- **Any** (13 connections)
- **get_player_occupants()** (12 connections) — `server/realtime/websocket_room_updates.py`
- **send_personalized_room_events()** (11 connections) — `server/realtime/room_viewer_fanout.py`
- **get_npc_occupants()** (11 connections) — `server/realtime/websocket_room_updates.py`
- **test_game_state_provider_hallucination.py** (11 connections) — `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- **room_has_hallucinating_viewer()** (10 connections) — `server/services/phantom_visibility.py`
- **phantom_visibility.py** (10 connections) — `server/services/phantom_visibility.py`
- **.connection_manager()** (9 connections) — `server/realtime/nats_message_handler.py`
- **test_phantom_visibility.py** (9 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- *... and 224 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (22 shared connections)
- [room_update_event_builder.py](room_update_event_builder.py.md) (17 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (13 shared connections)
- [event_types.py](event_types.py.md) (12 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (11 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (10 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (8 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (7 shared connections)
- [ConnectionManager](ConnectionManager.md) (7 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (6 shared connections)
- [Room](Room.md) (6 shared connections)
- [RoomEventHandler](RoomEventHandler.md) (5 shared connections)

## Source Files

- `server/realtime/connection_state_machine.py`
- `server/realtime/envelope.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/room_update_event_builder.py`
- `server/realtime/room_viewer_fanout.py`
- `server/realtime/running_app.py`
- `server/realtime/websocket_handler_connection.py`
- `server/realtime/websocket_room_updates.py`
- `server/services/phantom_visibility.py`
- `server/tests/unit/realtime/integration/test_game_state_provider_hallucination.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_websocket_room_updates.py`
- `server/tests/unit/services/test_phantom_visibility.py`

## Audit Trail

- EXTRACTED: 634 (91%)
- INFERRED: 61 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*