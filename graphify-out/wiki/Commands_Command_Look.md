# Commands Command Look

> 38 nodes

## Key Concepts

- **look_command.py** (37 connections) — `server/commands/look_command.py`
- **Any** (12 connections)
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **_route_look_command()** (10 connections) — `server/commands/look_command.py`
- **_handle_implicit_target_lookup()** (9 connections) — `server/commands/look_command.py`
- **handle_explore_command()** (8 connections) — `server/commands/exploration_commands.py`
- **handle_look_command()** (8 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (7 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (5 connections) — `server/commands/look_command.py`
- **_get_room_drops()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_player_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_item_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_container_look()** (5 connections) — `server/commands/look_command.py`
- **_try_implicit_target_lookup()** (5 connections) — `server/commands/look_command.py`
- **_try_direction_look()** (5 connections) — `server/commands/look_command.py`
- **test_exploration_commands.py** (5 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **_get_app_and_persistence()** (4 connections) — `server/commands/look_command.py`
- **test_handle_explore_command()** (3 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **test_handle_explore_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_exploration_commands.py`
- **Any** (1 connections)
- **Exploration commands for MythosMUD.  This module contains handlers for explorati** (1 connections) — `server/commands/exploration_commands.py`
- **Handle exploration requests by returning a simple message.      This lightweight** (1 connections) — `server/commands/exploration_commands.py`
- **Look command for MythosMUD.  This module handles the look command for examining** (1 connections) — `server/commands/look_command.py`
- **Extract app and persistence from request.** (1 connections) — `server/commands/look_command.py`
- **Validate and retrieve player and room for look command.** (1 connections) — `server/commands/look_command.py`
- *... and 13 more nodes in this community*

## Relationships

- [Look Player Command](Look_Player_Command.md) (8 shared connections)
- [Player State Command Factory](Player_State_Command_Factory.md) (5 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (5 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (5 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (4 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (4 shared connections)
- [Look NPC Command](Look_NPC_Command.md) (3 shared connections)
- [Look Display Helpers](Look_Display_Helpers.md) (3 shared connections)
- [Player Left Room Tests](Player_Left_Room_Tests.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (1 shared connections)

## Source Files

- `server/commands/exploration_commands.py`
- `server/commands/look_command.py`
- `server/tests/unit/commands/test_exploration_commands.py`

## Audit Trail

- EXTRACTED: 168 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*