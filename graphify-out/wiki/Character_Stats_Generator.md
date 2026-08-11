# Character Stats Generator

> 347 nodes

## Key Concepts

- **PlayerNameExtractor** (104 connections) — `server/realtime/player_name_utils.py`
- **TestPlayerNameExtractor** (62 connections) — `server/tests/unit/realtime/test_player_name_utils.py`
- **PlayerEventHandlerUtils** (42 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerRoomEventHandler** (30 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers.py** (26 connections) — `server/realtime/player_event_handlers.py`
- **PlayerEventHandler** (26 connections) — `server/realtime/player_event_handlers.py`
- **MessageBuilder** (22 connections) — `server/realtime/message_builders.py`
- **RoomOccupantManager** (22 connections) — `server/realtime/room_occupant_manager.py`
- **conftest.py** (22 connections) — `server/tests/unit/realtime/conftest.py`
- **player_event_handlers_room.py** (17 connections) — `server/realtime/player_event_handlers_room.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **PlayerStateEventHandler** (14 connections) — `server/realtime/player_event_handlers_state.py`
- **Any** (14 connections)
- **player_name_utils.py** (13 connections) — `server/realtime/player_name_utils.py`
- **UUID** (12 connections)
- **Any** (10 connections)
- **Any** (9 connections)
- **.handle_player_entered()** (9 connections) — `server/realtime/player_event_handlers_room.py`
- **.__init__()** (9 connections) — `server/realtime/room_occupant_manager.py`
- **test_player_event_handlers_utils_grace_period.py** (9 connections) — `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- **._initialize_modules()** (8 connections) — `server/realtime/event_handler.py`
- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **.__init__()** (8 connections) — `server/realtime/player_event_handlers.py`
- **UUID** (8 connections)
- **._validate_name_not_uuid()** (8 connections) — `server/realtime/player_name_utils.py`
- *... and 322 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (28 shared connections)
- [Client Event Store](Client_Event_Store.md) (15 shared connections)
- [API Type Guards](API_Type_Guards.md) (12 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (11 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (10 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (5 shared connections)
- [player_event_handler_utils](player_event_handler_utils.md) (5 shared connections)
- [App Creation Flow Screens](App_Creation_Flow_Screens.md) (3 shared connections)
- [Game Client Container](Game_Client_Container.md) (3 shared connections)
- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (3 shared connections)
- [Archive Lucidity System](Archive_Lucidity_System.md) (3 shared connections)
- [Room Exploration API](Room_Exploration_API.md) (3 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/message_builders.py`
- `server/realtime/player_event_handlers.py`
- `server/realtime/player_event_handlers_room.py`
- `server/realtime/player_event_handlers_state.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/realtime/player_name_utils.py`
- `server/realtime/room_occupant_manager.py`
- `server/tests/unit/realtime/conftest.py`
- `server/tests/unit/realtime/test_player_event_handlers_utils_grace_period.py`
- `server/tests/unit/realtime/test_player_name_utils.py`

## Audit Trail

- EXTRACTED: 1206 (96%)
- INFERRED: 44 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*