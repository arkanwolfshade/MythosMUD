# MP Regeneration Service

> 63 nodes

## Key Concepts

- **rescue_commands.py** (33 connections) — `server/commands/rescue_commands.py`
- **handle_ground_command()** (28 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (23 connections) — `server/tests/unit/commands/test_rescue_commands.py`
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
- **test_handle_rescue_command_no_app()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 38 more nodes in this community*

## Relationships

- [Message Queue Cleanup](Message_Queue_Cleanup.md) (11 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (9 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (8 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (3 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (3 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (2 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (1 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 241 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*