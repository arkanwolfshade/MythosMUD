# .app

> 66 nodes

## Key Concepts

- **.app()** (33 connections) — `server/commands/look_helpers.py`
- **rescue_commands.py** (33 connections) — `server/commands/rescue_commands.py`
- **handle_ground_command()** (27 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (24 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **asyncio** (17 connections)
- **handle_rescue_command()** (15 connections) — `server/commands/rescue_commands.py`
- **Any** (9 connections)
- **_run_ground_session()** (8 connections) — `server/commands/rescue_commands.py`
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **patch** (7 connections)
- **_get_ground_services()** (6 connections) — `server/commands/rescue_commands.py`
- **test_handle_ground_command_apply_lucidity_error()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_player_key()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **UUID** (6 connections)
- **_complete_ground_command()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_success_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- **test_handle_ground_command_lucidity_record_not_found()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_target_player_key()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **_send_grounding_channeling_events()** (4 connections) — `server/commands/rescue_commands.py`
- *... and 41 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (10 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (5 shared connections)
- [real_time.py](real_time.py.md) (4 shared connections)
- [get_session_maker](get_session_maker.md) (4 shared connections)
- [position_commands.py](position_commands.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (3 shared connections)
- [websocket_handler_commands.py](websocket_handler_commands.py.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (2 shared connections)
- [server/commands/__init__.py](server-commands-__init__.py.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)

## Source Files

- `server/commands/look_helpers.py`
- `server/commands/rescue_commands.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 162 (79%)
- INFERRED: 42 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*