# Server Process Termination

> 24 nodes

## Key Concepts

- **utility_commands.py** (20 connections) — `server/commands/utility_commands.py`
- **handle_status_command()** (14 connections) — `server/commands/status_commands.py`
- **handle_whoami_command()** (12 connections) — `server/commands/status_commands.py`
- **test_utility_commands_whoami.py** (5 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **test_handle_status_command_error_handling()** (4 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_status_command_success()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_whoami_command()** (3 connections) — `server/tests/unit/commands/test_status_commands.py`
- **test_handle_whoami_command()** (3 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **test_handle_whoami_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **test_handle_whoami_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **Handle the status command for showing player status.      Args:         command_** (1 connections) — `server/commands/status_commands.py`
- **Handle the whoami command as an alias for status.      Mirrors handle_status_com** (1 connections) — `server/commands/status_commands.py`
- **Utility commands for MythosMUD.  This module contains handlers for utility comma** (1 connections) — `server/commands/utility_commands.py`
- **Test handle_status_command returns error when no persistence.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test handle_status_command returns error when player not found.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test handle_status_command returns status information successfully.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test handle_status_command handles errors gracefully.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Test handle_whoami_command calls handle_status_command.** (1 connections) — `server/tests/unit/commands/test_status_commands.py`
- **Unit tests for utility command handlers.  Tests the whoami command functionality** (1 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **Test handle_whoami_command() returns player information.** (1 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **Test handle_whoami_command() handles missing persistence.** (1 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`
- **Test handle_whoami_command() handles player not found.** (1 connections) — `server/tests/unit/commands/test_utility_commands_whoami.py`

## Relationships

- [Status Command Handlers](Status_Command_Handlers.md) (14 shared connections)
- [Container Open Events](Container_Open_Events.md) (4 shared connections)
- [Combat UUID Display Bug](Combat_UUID_Display_Bug.md) (4 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (2 shared connections)
- [App Creation Flow Screens](App_Creation_Flow_Screens.md) (2 shared connections)
- [Logging Migration Examples](Logging_Migration_Examples.md) (2 shared connections)
- [Logout Command Tests](Logout_Command_Tests.md) (2 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (2 shared connections)
- [Exploration Command Factory](Exploration_Command_Factory.md) (1 shared connections)
- [WebSocket Initial State](WebSocket_Initial_State.md) (1 shared connections)

## Source Files

- `server/commands/status_commands.py`
- `server/commands/utility_commands.py`
- `server/tests/unit/commands/test_status_commands.py`
- `server/tests/unit/commands/test_utility_commands_whoami.py`

## Audit Trail

- EXTRACTED: 79 (90%)
- INFERRED: 9 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*