# Send a system message to

> 53 nodes

## Key Concepts

- **handle_ground_command()** (32 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (23 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **handle_rescue_command()** (14 connections) — `server/commands/rescue_commands.py`
- **Any** (7 connections)
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **_get_ground_services()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_target()** (4 connections) — `server/commands/rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_player_key()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_apply_lucidity_error()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command()** (3 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_rescue_command()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_target()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_target_player_key()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_app()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_state()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_no_target()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_rescuer_not_found()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_not_found()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_different_rooms()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 28 more nodes in this community*

## Relationships

- [LiabilityStackEntry](LiabilityStackEntry.md) (13 shared connections)
- [test rate limiter utils](test_rate_limiter_utils.md) (7 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (3 shared connections)
- [.state()](state%28%29.md) (2 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (2 shared connections)
- [test magic commands](test_magic_commands.md) (2 shared connections)
- [test player preferences service](test_player_preferences_service.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [test command factories communication](test_command_factories_communication.md) (1 shared connections)
- [DropResolved](DropResolved.md) (1 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)
- [map helpers](map_helpers.md) (1 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 175 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*