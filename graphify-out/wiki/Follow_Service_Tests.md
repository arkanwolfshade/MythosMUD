# Follow Service Tests

> 65 nodes

## Key Concepts

- **rescue_commands.py** (33 connections) — `server/commands/rescue_commands.py`
- **handle_ground_command()** (28 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (23 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **send_rescue_update_event()** (18 connections) — `server/services/lucidity_event_dispatcher.py`
- **handle_rescue_command()** (14 connections) — `server/commands/rescue_commands.py`
- **Any** (9 connections)
- **_run_ground_session()** (9 connections) — `server/commands/rescue_commands.py`
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **UUID** (6 connections)
- **_get_ground_services()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_success_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_complete_ground_command()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_target()** (4 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_channeling_events()** (4 connections) — `server/commands/rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_player_key()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_apply_lucidity_error()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_target()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_target_player_key()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 40 more nodes in this community*

## Relationships

- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (15 shared connections)
- [Client Event Store](Client_Event_Store.md) (12 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (9 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (6 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (4 shared connections)
- [Player Death Service](Player_Death_Service.md) (3 shared connections)
- [Combat Messaging Tests](Combat_Messaging_Tests.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/services/lucidity_event_dispatcher.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 260 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*