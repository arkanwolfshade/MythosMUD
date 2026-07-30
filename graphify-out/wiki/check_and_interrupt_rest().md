# .check and interrupt rest()

> 87 nodes

## Key Concepts

- **test_rest_command.py** (38 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (26 connections) — `server/commands/rest_command.py`
- **handle_rest_command()** (22 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (19 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **Any** (11 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **UUID** (9 connections)
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **test_rest_interrupts_combat_action()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_handle_rest_command_no_app()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_already_resting()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_in_combat()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_rest_location_instant()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_starts_countdown()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 62 more nodes in this community*

## Relationships

- [test magic commands](test_magic_commands.md) (9 shared connections)
- [Any](Any.md) (8 shared connections)
- [command admin](command_admin.md) (5 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (4 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [real time](real_time.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (2 shared connections)
- [DropResolved](DropResolved.md) (2 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (2 shared connections)
- [Validate that player is in](Validate_that_player_is_in.md) (2 shared connections)
- [test connection establishment](test_connection_establishment.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 336 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*