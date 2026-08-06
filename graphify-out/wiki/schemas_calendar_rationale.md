# schemas calendar rationale

> 15 nodes

## Key Concepts

- **handle_time_command()** (13 connections) — `server/commands/time_commands.py`
- **test_time_commands.py** (8 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_success()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_with_holidays()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holidays()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_holiday_service_error()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holiday_service()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Any** (1 connections)
- **Handle the time command, exposing the current Mythos time and active holidays.** (1 connections) — `server/commands/time_commands.py`
- **Unit tests for time command handlers.  Tests the time command functionality.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() returns time information.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() includes active holidays.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles no active holidays.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles holiday service errors.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles missing holiday service.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`

## Relationships

- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (1 shared connections)
- [commands who rationale](commands_who_rationale.md) (1 shared connections)

## Source Files

- `server/commands/time_commands.py`
- `server/tests/unit/commands/test_time_commands.py`

## Audit Trail

- EXTRACTED: 43 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*