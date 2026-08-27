# test_rescue_commands.py

> 40 nodes

## Key Concepts

- **test_rescue_commands.py** (24 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **asyncio** (17 connections)
- **handle_rescue_command()** (15 connections) — `server/commands/rescue_commands.py`
- **patch** (7 connections)
- **test_handle_ground_command_apply_lucidity_error()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_player_key()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_lucidity_record_not_found()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_target_player_key()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_different_rooms()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_no_rescuer_room()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_no_target()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_rescuer_not_found()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_not_found()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_app()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_state()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_target()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Delegate rescue handling to the RescueService for testable, real logic.** (1 connections) — `server/commands/rescue_commands.py`
- **Unit tests for rescue command handlers. Tests the rescue command functionality.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Test handle_ground_command() handles missing target.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **Test handle_ground_command() handles rescuer not found.** (1 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 15 more nodes in this community*

## Relationships

- [rescue_commands.py](rescue_commands.py.md) (15 shared connections)
- [models/player.py](models-player.py.md) (6 shared connections)
- [.state](state.md) (2 shared connections)
- [test_rescue_service.py](test_rescue_service.py.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [get_async_session](get_async_session.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 87 (93%)
- INFERRED: 7 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*