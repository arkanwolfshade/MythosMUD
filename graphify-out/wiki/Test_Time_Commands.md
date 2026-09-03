# Test Time Commands

> 17 nodes

## Key Concepts

- **handle_time_command()** (13 connections) — `server/commands/time_commands.py`
- **time_commands.py** (10 connections) — `server/commands/time_commands.py`
- **test_time_commands.py** (9 connections) — `server/tests/unit/commands/test_time_commands.py`
- **asyncio** (5 connections)
- **test_handle_time_command_holiday_service_error()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holiday_service()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holidays()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_success()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_with_holidays()** (4 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() includes active holidays.** (2 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Any** (1 connections)
- **Time command handlers for MythosMUD. This module contains handlers for the time…** (1 connections) — `server/commands/time_commands.py`
- **Handle the time command, exposing the current Mythos time and active holidays.** (1 connections) — `server/commands/time_commands.py`
- **Unit tests for time command handlers. Tests the time command functionality.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles holiday service errors.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles missing holiday service.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() returns time information.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`

## Relationships

- [Test Game Tick Death](Test_Game_Tick_Death.md) (2 shared connections)
- [Test Who Commands](Test_Who_Commands.md) (2 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [Time Service](Time_Service.md) (1 shared connections)
- [Alias Storage](Alias_Storage.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/commands/time_commands.py`
- `server/tests/unit/commands/test_time_commands.py`

## Audit Trail

- EXTRACTED: 38 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*