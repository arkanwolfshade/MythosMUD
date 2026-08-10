# Commands Command Look

> 29 nodes

## Key Concepts

- **look_command.py** (37 connections) — `server/commands/look_command.py`
- **Any** (12 connections)
- **_is_direction()** (11 connections) — `server/commands/look_helpers.py`
- **_route_look_command()** (10 connections) — `server/commands/look_command.py`
- **_handle_implicit_target_lookup()** (9 connections) — `server/commands/look_command.py`
- **handle_look_command()** (8 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (7 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (5 connections) — `server/commands/look_command.py`
- **_get_room_drops()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_player_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_item_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_container_look()** (5 connections) — `server/commands/look_command.py`
- **_try_implicit_target_lookup()** (5 connections) — `server/commands/look_command.py`
- **_try_direction_look()** (5 connections) — `server/commands/look_command.py`
- **_get_app_and_persistence()** (4 connections) — `server/commands/look_command.py`
- **Look command for MythosMUD.  This module handles the look command for examining** (1 connections) — `server/commands/look_command.py`
- **Extract app and persistence from request.** (1 connections) — `server/commands/look_command.py`
- **Validate and retrieve player and room for look command.** (1 connections) — `server/commands/look_command.py`
- **Get room drops from room manager.** (1 connections) — `server/commands/look_command.py`
- **Setup and validate look command prerequisites.** (1 connections) — `server/commands/look_command.py`
- **Try to handle explicit player look.** (1 connections) — `server/commands/look_command.py`
- **Try to handle explicit item look.** (1 connections) — `server/commands/look_command.py`
- **Try to handle explicit container look or container inspection.** (1 connections) — `server/commands/look_command.py`
- **Handle implicit target lookup with priority resolution.** (1 connections) — `server/commands/look_command.py`
- **Try to handle implicit target lookup, returns (result, direction).** (1 connections) — `server/commands/look_command.py`
- *... and 4 more nodes in this community*

## Relationships

- [Look Player Command](Look_Player_Command.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (8 shared connections)
- [Look Container Command](Look_Container_Command.md) (5 shared connections)
- [Archive Circuit Breaker](Archive_Circuit_Breaker.md) (5 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (5 shared connections)
- [Config Model Tests](Config_Model_Tests.md) (4 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (3 shared connections)
- [Look Display Helpers](Look_Display_Helpers.md) (3 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)

## Source Files

- `server/commands/look_command.py`
- `server/commands/look_helpers.py`

## Audit Trail

- EXTRACTED: 145 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*