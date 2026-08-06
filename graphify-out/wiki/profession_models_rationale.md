# profession models rationale

> 168 nodes

## Key Concepts

- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **test_player_event_handlers_state.py** (33 connections) — `server/tests/unit/realtime/test_player_event_handlers_state.py`
- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **UUID** (12 connections)
- **Any** (10 connections)
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **.__init__()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_occupants_snapshot_to_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_updates_to_entering_player()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **.handle_player_left()** (7 connections) — `server/realtime/player_event_handlers_room.py`
- **Any** (7 connections)
- **._prepare_room_data()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_update_to_player()** (6 connections) — `server/realtime/player_event_handlers_room.py`
- **UUID** (6 connections)
- **.log_player_movement()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._send_room_name_message()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **._log_occupants_info()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.query_room_occupants_snapshot()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.send_room_state_to_player()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_room_state_event()** (5 connections) — `server/realtime/player_event_handlers_room.py`
- **.get_player_info()** (5 connections) — `server/realtime/player_event_handlers_utils.py`
- *... and 143 more nodes in this community*

## Relationships

- [inventory mutation guard](inventory_mutation_guard.md) (23 shared connections)
- [Error Conversion](Error_Conversion.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (9 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (8 shared connections)
- [Database Config](Database_Config.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [skill service game](skill_service_game.md) (3 shared connections)
- [npc combat base](npc_combat_base.md) (2 shared connections)
- [player event handlers](player_event_handlers.md) (2 shared connections)
- [command parser helpers](command_parser_helpers.md) (2 shared connections)
- [schemas players profession](schemas_players_profession.md) (1 shared connections)
- [player_event_handler_utils](player_event_handler_utils.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_player_event_handlers_state.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`

## Audit Trail

- EXTRACTED: 528 (98%)
- INFERRED: 12 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*