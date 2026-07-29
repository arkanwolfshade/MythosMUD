# time commands

> 18 nodes

## Key Concepts

- **get_mythos_chronicle()** (24 connections) — `server/time/time_service.py`
- **handle_time_command()** (14 connections) — `server/commands/time_commands.py`
- **time_commands.py** (10 connections) — `server/commands/time_commands.py`
- **test_time_commands.py** (8 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_success()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_with_holidays()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holidays()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_holiday_service_error()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **test_handle_time_command_no_holiday_service()** (3 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() includes active holidays.** (2 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Any** (1 connections)
- **Time command handlers for MythosMUD.  This module contains handlers for the time** (1 connections) — `server/commands/time_commands.py`
- **Handle the time command, exposing the current Mythos time and active holidays.** (1 connections) — `server/commands/time_commands.py`
- **Unit tests for time command handlers.  Tests the time command functionality.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() returns time information.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles holiday service errors.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Test handle_time_command() handles missing holiday service.** (1 connections) — `server/tests/unit/commands/test_time_commands.py`
- **Convenience wrapper mirroring other service access patterns.** (1 connections) — `server/time/time_service.py`

## Relationships

- [Any](Any.md) (8 shared connections)
- [main()](main%28%29.md) (6 shared connections)
- [game tick processing](game_tick_processing.md) (3 shared connections)
- [utility commands](utility_commands.md) (2 shared connections)
- [lifespan](lifespan.md) (2 shared connections)
- [lifespan shutdown](lifespan_shutdown.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [BaseUserManager](BaseUserManager.md) (1 shared connections)
- [get mythos time()](get_mythos_time%28%29.md) (1 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)
- [create npc services on app()](create_npc_services_on_app%28%29.md) (1 shared connections)

## Source Files

- `server/commands/time_commands.py`
- `server/tests/unit/commands/test_time_commands.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 79 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*