# look_command.py

> 58 nodes

## Key Concepts

- **look_command.py** (38 connections) — `server/commands/look_command.py`
- **test_look_command.py** (22 connections) — `server/tests/unit/commands/test_look_command.py`
- **handle_look_command()** (13 connections) — `server/commands/look_command.py`
- **Any** (12 connections)
- **_route_look_command()** (10 connections) — `server/commands/look_command.py`
- **_get_room_drops()** (9 connections) — `server/commands/look_command.py`
- **_handle_implicit_target_lookup()** (9 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (9 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (9 connections) — `server/commands/look_command.py`
- **asyncio** (9 connections)
- **_get_app_and_persistence()** (7 connections) — `server/commands/look_command.py`
- **_try_direction_look()** (7 connections) — `server/commands/look_command.py`
- **_try_explicit_container_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_item_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_player_look()** (5 connections) — `server/commands/look_command.py`
- **_try_implicit_target_lookup()** (5 connections) — `server/commands/look_command.py`
- **test_handle_look_command_explicit_player_target()** (4 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_handle_look_command_implicit_target_not_found()** (4 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_handle_look_command_routes_to_room_look()** (4 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_handle_look_command_setup_failure()** (4 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_setup_look_command_success()** (4 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_try_direction_look_delegates()** (4 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_validate_look_prerequisites_no_persistence()** (4 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_validate_look_prerequisites_player_not_found()** (4 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_validate_look_prerequisites_room_missing()** (4 connections) — `server/tests/unit/commands/test_look_command.py`
- *... and 33 more nodes in this community*

## Relationships

- [test_look_player.py](test_look_player.py.md) (8 shared connections)
- [_find_item_in_equipped](_find_item_in_equipped.md) (5 shared connections)
- [look_container.py](look_container.py.md) (5 shared connections)
- [test_look_room.py](test_look_room.py.md) (5 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [test_go_command.py](test_go_command.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)

## Source Files

- `server/commands/look_command.py`
- `server/tests/unit/commands/test_look_command.py`

## Audit Trail

- EXTRACTED: 144 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*