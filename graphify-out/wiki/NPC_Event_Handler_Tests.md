# NPC Event Handler Tests

> 166 nodes

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
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **._get_player_for_position_change()** (5 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (5 connections) — `server/services/player_position_service.py`
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **._extract_player_info()** (4 connections) — `server/services/player_position_service.py`
- *... and 141 more nodes in this community*

## Relationships

- [Container Persistence Queries](Container_Persistence_Queries.md) (9 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (8 shared connections)
- [Container Open Events](Container_Open_Events.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (6 shared connections)
- [Player Left Room Tests](Player_Left_Room_Tests.md) (5 shared connections)
- [NPC Admin Commands](NPC_Admin_Commands.md) (5 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (5 shared connections)
- [Health Check Models](Health_Check_Models.md) (4 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [Chat Channel Logger](Chat_Channel_Logger.md) (3 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_rest_command.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 585 (99%)
- INFERRED: 8 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*