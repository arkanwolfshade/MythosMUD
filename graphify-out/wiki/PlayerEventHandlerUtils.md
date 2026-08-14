# PlayerEventHandlerUtils

> 134 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **NATSMessageHandler** (24 connections) — `server/realtime/nats_message_handler.py`
- **realtime/conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **fixture** (15 connections)
- **UUID** (12 connections)
- **Any** (10 connections)
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **._initialize_handlers()** (7 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_left()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.__init__()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_occupants_snapshot_to_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_updates_to_entering_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **Any** (7 connections)
- **._prepare_room_data()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_update_to_player()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **UUID** (6 connections)
- **.get_room_state_event()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._log_occupants_info()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.log_player_movement()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.query_room_occupants_snapshot()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._send_room_name_message()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_state_to_player()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_player_info()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- *... and 109 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (26 shared connections)
- [test_player_event_handlers_respawn.py](test_player_event_handlers_respawn.py.md) (7 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (2 shared connections)
- [test_player_event_handlers_state.py](test_player_event_handlers_state.py.md) (2 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (1 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [EventHandler](EventHandler.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 250 (92%)
- INFERRED: 21 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*