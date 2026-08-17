# server commands time commands handle

> 15 nodes

## Key Concepts

- **handle_time_command()** (14 connections) — `server/commands/time_commands.py`
- **test_time_commands.py** (9 connections) — `server/tests/unit/commands/test_time_commands.py`
- **asyncio** (5 connections)
- **test_handle_time_command_holiday_service_error()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holiday_service()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holidays()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_success()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_with_holidays()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() includes active holidays.** (2 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Any** (1 connections)
- **Handle the time command, exposing the current Mythos time and active holidays.** (1 connections) — `server/commands/time_commands.py`
- **Unit tests for time command handlers. Tests the time command functionality.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles holiday service errors.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles missing holiday service.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() returns time information.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`

## Relationships

- [holidayresolver](holidayresolver.md) (3 shared connections)
- [server commands utility commands](server_commands_utility_commands.md) (1 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (1 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/time_commands.py`
- `server/tests/unit/commands/test_time_commands.py`

## Audit Trail

- EXTRACTED: 30 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*