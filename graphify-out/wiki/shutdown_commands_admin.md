# shutdown commands admin

> 14 nodes

## Key Concepts

- **parse_shutdown_parameters()** (11 connections) — `server/commands/admin_shutdown_command.py`
- **test_parse_shutdown_parameters_no_args()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_cancel()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_seconds()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_invalid_negative()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_invalid_zero()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **test_parse_shutdown_parameters_invalid_string()** (3 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Parse shutdown command parameters.      Args:         command_data: Command data** (1 connections) — `server/commands/admin_shutdown_command.py`
- **Test parse_shutdown_parameters() with no args defaults to 10 seconds.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test parse_shutdown_parameters() with cancel action.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test parse_shutdown_parameters() with seconds.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test parse_shutdown_parameters() with negative seconds.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test parse_shutdown_parameters() with zero seconds.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`
- **Test parse_shutdown_parameters() with invalid string.** (1 connections) — `server/tests/unit/commands/test_admin_shutdown_command.py`

## Relationships

- [shutdown admin command](shutdown_admin_command.md) (10 shared connections)

## Source Files

- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*