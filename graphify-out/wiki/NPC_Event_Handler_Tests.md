# NPC Event Handler Tests

> 174 nodes

## Key Concepts

- **PlayerPositionService** (45 connections) — `server/services/player_position_service.py`
- **test_rest_command.py** (38 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **rest_command.py** (26 connections) — `server/commands/rest_command.py`
- **handle_rest_command()** (22 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (17 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **player_position_service.py** (12 connections) — `server/services/player_position_service.py`
- **Any** (11 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **.change_position()** (10 connections) — `server/services/player_position_service.py`
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **UUID** (9 connections)
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **Any** (7 connections)
- **MockPersistence** (7 connections) — `server/tests/unit/commands/test_rest_command.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **._interrupt_rest_for_cast()** (6 connections) — `server/commands/magic_commands.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **AppWithState** (5 connections)
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- *... and 149 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (23 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (6 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (5 shared connections)
- [Player Left Room Tests](Player_Left_Room_Tests.md) (5 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (5 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (4 shared connections)
- [Combat Aggro Threat](Combat_Aggro_Threat.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (2 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/magic_commands.py`
- `server/commands/rest_command.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_rest_command.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 608 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*