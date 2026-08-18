# server commands look command

> 85 nodes

## Key Concepts

- **look_command.py** (57 connections) — `server/commands/look_command.py`
- **test_look_command.py** (26 connections) — `server/tests/unit/commands/test_look_command.py`
- **handle_look_command()** (18 connections) — `server/commands/look_command.py`
- **LookRequest** (15 connections) — `server/commands/look_helpers.py`
- **_handle_implicit_target_lookup()** (13 connections) — `server/commands/look_command.py`
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
- *... and 60 more nodes in this community*

## Relationships

- [server commands look helpers](server_commands_look_helpers.md) (12 shared connections)
- [server commands look container containerlookargs](server_commands_look_container_containerlookargs.md) (6 shared connections)
- [server commands look container](server_commands_look_container.md) (5 shared connections)
- [server commands look player](server_commands_look_player.md) (5 shared connections)
- [server commands look item](server_commands_look_item.md) (5 shared connections)
- [server commands look room](server_commands_look_room.md) (5 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (3 shared connections)
- [server commands look npc](server_commands_look_npc.md) (3 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (3 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (3 shared connections)
- [server commands exploration commands](server_commands_exploration_commands.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)

## Source Files

- `server/commands/look_command.py`
- `server/commands/look_helpers.py`
- `server/tests/unit/commands/test_look_command.py`

## Audit Trail

- EXTRACTED: 242 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*