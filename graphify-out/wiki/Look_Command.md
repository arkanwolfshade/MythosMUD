# Look Command

> 87 nodes

## Key Concepts

- **look_command.py** (58 connections) — `server/commands/look_command.py`
- **test_look_command.py** (26 connections) — `server/tests/unit/commands/test_look_command.py`
- **handle_look_command()** (17 connections) — `server/commands/look_command.py`
- **LookRequest** (15 connections) — `server/commands/look_helpers.py`
- **_handle_implicit_target_lookup()** (14 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (13 connections) — `server/commands/look_command.py`
- **_route_look_command()** (12 connections) — `server/commands/look_command.py`
- **_get_app_and_persistence()** (11 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (11 connections) — `server/commands/look_command.py`
- **_is_direction()** (11 connections) — `server/commands/look_helpers.py`
- **_get_room_drops()** (10 connections) — `server/commands/look_command.py`
- **_try_direction_look()** (10 connections) — `server/commands/look_command.py`
- **_try_explicit_player_look()** (10 connections) — `server/commands/look_command.py`
- **FastAPI** (10 connections)
- **asyncio** (10 connections)
- **_LookPersistence** (9 connections) — `server/commands/look_command.py`
- **LookRouteCtx** (9 connections) — `server/commands/look_command.py`
- **_try_explicit_container_look()** (9 connections) — `server/commands/look_command.py`
- **_try_explicit_item_look()** (9 connections) — `server/commands/look_command.py`
- **CommandResponse** (9 connections)
- **_as_response()** (8 connections) — `server/commands/look_command.py`
- **_LookRoom** (7 connections) — `server/commands/look_command.py`
- **_container_from_app()** (7 connections) — `server/commands/look_command.py`
- **_connection_manager_from_app()** (6 connections) — `server/commands/look_command.py`
- **_prototype_registry_from_app()** (6 connections) — `server/commands/look_command.py`
- *... and 62 more nodes in this community*

## Relationships

- [Test Look Helpers](Test_Look_Helpers.md) (12 shared connections)
- [Test Look Room](Test_Look_Room.md) (7 shared connections)
- [Test Look Container](Test_Look_Container.md) (6 shared connections)
- [Test Look Container Helpers](Test_Look_Container_Helpers.md) (5 shared connections)
- [Test Look Player](Test_Look_Player.md) (5 shared connections)
- [Look Item](Look_Item.md) (5 shared connections)
- [Test Room Renderer](Test_Room_Renderer.md) (3 shared connections)
- [Test Look Npc Helpers](Test_Look_Npc_Helpers.md) (3 shared connections)
- [Test Request Context](Test_Request_Context.md) (3 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (2 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)

## Source Files

- `server/commands/look_command.py`
- `server/commands/look_helpers.py`
- `server/tests/unit/commands/test_look_command.py`

## Audit Trail

- EXTRACTED: 245 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*