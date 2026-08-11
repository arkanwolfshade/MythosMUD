# App Creation Flow Screens

> 57 nodes

## Key Concepts

- **NPCEventHandler** (25 connections) — `server/realtime/npc_event_handlers.py`
- **test_npc_event_handlers_helpers.py** (14 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **.handle_npc_entered()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._send_npc_left_message()** (8 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_spawn_message()** (7 connections) — `server/realtime/npc_event_handlers.py`
- **._send_room_message()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **.handle_npc_left()** (6 connections) — `server/realtime/npc_event_handlers.py`
- **.__init__()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **Any** (5 connections)
- **._get_npc_instance()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_name()** (5 connections) — `server/realtime/npc_event_handlers.py`
- **._get_behavior_config_from_instance()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._parse_behavior_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._extract_spawn_message_from_config()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._determine_direction_from_rooms()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._get_npc_departure_message()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._validate_npc_left_room()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **._schedule_room_occupants_update()** (4 connections) — `server/realtime/npc_event_handlers.py`
- **npc_event_handler()** (3 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **mock_message_builder()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **test_extract_spawn_message_from_config()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **test_extract_spawn_message_from_config_none()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **test_get_npc_spawn_message()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- **test_get_npc_spawn_message_custom()** (2 connections) — `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`
- *... and 32 more nodes in this community*

## Relationships

- [Communication Command Flows](Communication_Command_Flows.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (3 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Archive Advanced Chat](Archive_Advanced_Chat.md) (1 shared connections)
- [test_apply_encounter_lucidity_loss_first_encounter](test_apply_encounter_lucidity_loss_first_encounter.md) (1 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (1 shared connections)

## Source Files

- `server/realtime/npc_event_handlers.py`
- `server/tests/unit/realtime/test_npc_event_handlers_helpers.py`

## Audit Trail

- EXTRACTED: 171 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*