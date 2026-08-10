# Test Value Distribution

> 44 nodes

## Key Concepts

- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **UUID** (12 connections)
- **Any** (10 connections)
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **.__init__()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_occupants_snapshot_to_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_updates_to_entering_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_left()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **._prepare_room_data()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_update_to_player()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.log_player_movement()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._send_room_name_message()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._log_occupants_info()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.query_room_occupants_snapshot()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_state_to_player()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_room_state_event()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.broadcast_player_entered_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.subscribe_player_to_room()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.build_room_occupants_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **._process_player_entered_event()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.unsubscribe_player_from_room()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **.broadcast_player_left_message()** (4 connections) — `server/realtime/player_event_handlers_room.py`
- **player_room_event_handler()** (3 connections) — `server/tests/unit/realtime/conftest.py`
- **Handles room-related player events (entered, left, occupants).** (1 connections) — `server/realtime/player_event_handlers_room.py`
- **Initialize room event handler.          Args:             connection_manager: Co** (1 connections) — `server/realtime/player_event_handlers_room.py`
- *... and 19 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (11 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (5 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_room.py`
- `server/tests/unit/realtime/conftest.py`

## Audit Trail

- EXTRACTED: 174 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*