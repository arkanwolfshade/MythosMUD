# get health status()

> 17 nodes

## Key Concepts

- **handle_time_command()** (14 connections) — `server/commands/time_commands.py`
- **time_commands.py** (10 connections) — `server/commands/time_commands.py`
- **test_time_commands.py** (8 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_success()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_with_holidays()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holidays()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_holiday_service_error()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holiday_service()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Any** (1 connections)
- **Time command handlers for MythosMUD.  This module contains handlers for the time** (1 connections) — `server/commands/time_commands.py`
- **Handle the time command, exposing the current Mythos time and active holidays.** (1 connections) — `server/commands/time_commands.py`
- **Unit tests for time command handlers.  Tests the time command functionality.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() returns time information.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() includes active holidays.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles no active holidays.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles holiday service errors.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles missing holiday service.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`

## Relationships

- [Any](Any.md) (3 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [disconnect player connections()](disconnect_player_connections%28%29.md) (2 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)

## Source Files

- `server/commands/time_commands.py`
- `server/tests/unit/commands/test_time_commands.py`

## Audit Trail

- EXTRACTED: 54 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*