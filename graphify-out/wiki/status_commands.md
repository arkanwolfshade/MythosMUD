# status commands

> 22 nodes

## Key Concepts

- **test_status_commands.py** (31 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_no_combat_service()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_no_app()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_player_in_combat()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_get_combat_status_player_not_in_combat()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_build_base_status_lines()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_success()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_whoami_command()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Unit tests for status command handlers.  Tests handlers for status and whoami co** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _get_combat_status returns False when no combat service.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _get_combat_status returns False when no app.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _get_combat_status returns True when player is in combat.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _get_combat_status returns False when player is not in combat.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test _build_base_status_lines builds correct status lines.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test handle_status_command returns error when no persistence.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test handle_status_command returns error when player not found.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test handle_status_command returns status information successfully.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test handle_status_command handles errors gracefully.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test handle_whoami_command calls handle_status_command.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`

## Relationships

- [logging utilities](logging_utilities.md) (16 shared connections)
- [Any](Any.md) (6 shared connections)
- [HallucinationFrequencyService](HallucinationFrequencyService.md) (4 shared connections)
- [MutableHeaders](MutableHeaders.md) (4 shared connections)
- [create access token()](create_access_token%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_status_commands.py`

## Audit Trail

- EXTRACTED: 72 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*