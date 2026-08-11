# Cursor Plans Pydantic

> 15 nodes

## Key Concepts

- **handle_time_command()** (14 connections) — `server/commands/time_commands.py`
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

- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)
- [Combat UUID Display Bug](Combat_UUID_Display_Bug.md) (1 shared connections)

## Source Files

- `server/commands/time_commands.py`
- `server/tests/unit/commands/test_time_commands.py`

## Audit Trail

- EXTRACTED: 43 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*