# Async Persistence Core

> 37 nodes · cohesion 0.09

## Key Concepts

- **look_command.py** (37 connections) — `server/commands/look_command.py`
- **look_helpers.py** (16 connections) — `server/commands/look_helpers.py`
- **Any** (12 connections)
- **_is_direction()** (11 connections) — `server/commands/look_helpers.py`
- **_route_look_command()** (10 connections) — `server/commands/look_command.py`
- **_try_lookup_container_implicit()** (10 connections) — `server/commands/look_container.py`
- **_handle_implicit_target_lookup()** (9 connections) — `server/commands/look_command.py`
- **handle_look_command()** (8 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (7 connections) — `server/commands/look_command.py`
- **_get_room_drops()** (5 connections) — `server/commands/look_command.py`
- **_try_direction_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_container_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_item_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_player_look()** (5 connections) — `server/commands/look_command.py`
- **_try_implicit_target_lookup()** (5 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (5 connections) — `server/commands/look_command.py`
- **_get_app_and_persistence()** (4 connections) — `server/commands/look_command.py`
- **test_try_lookup_container_implicit_not_found()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **test_try_lookup_container_implicit_success()** (3 connections) — `server/tests/unit/commands/test_look_container.py`
- **Look command for MythosMUD.  This module handles the look command for examining** (1 connections) — `server/commands/look_command.py`
- **Try to handle explicit player look.** (1 connections) — `server/commands/look_command.py`
- **Try to handle explicit item look.** (1 connections) — `server/commands/look_command.py`
- **Try to handle explicit container look or container inspection.** (1 connections) — `server/commands/look_command.py`
- **Handle implicit target lookup with priority resolution.** (1 connections) — `server/commands/look_command.py`
- **Try to handle implicit target lookup, returns (result, direction).** (1 connections) — `server/commands/look_command.py`
- *... and 12 more nodes in this community*

## Relationships

- [Look Display Helpers](Look_Display_Helpers.md) (14 shared connections)
- [Logout Command Helpers](Logout_Command_Helpers.md) (10 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (6 shared connections)
- [Look Player Command](Look_Player_Command.md) (6 shared connections)
- [Look Item Commands](Look_Item_Commands.md) (5 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (5 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Look NPC Command](Look_NPC_Command.md) (3 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (3 shared connections)
- [Commands Inventory Item](Commands_Inventory_Item.md) (2 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)
- [NATS Message Broker](NATS_Message_Broker.md) (1 shared connections)

## Source Files

- `server/commands/look_command.py`
- `server/commands/look_container.py`
- `server/commands/look_helpers.py`
- `server/tests/unit/commands/test_look_container.py`

## Audit Trail

- EXTRACTED: 181 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*