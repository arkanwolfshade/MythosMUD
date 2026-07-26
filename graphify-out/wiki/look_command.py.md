# look_command.py

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

- [test_look_helpers.py](test_look_helpers.py.md) (14 shared connections)
- [test_look_container.py](test_look_container.py.md) (10 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [test_look_player.py](test_look_player.py.md) (6 shared connections)
- [_find_item_in_equipped](_find_item_in_equipped.md) (5 shared connections)
- [test_look_room.py](test_look_room.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (3 shared connections)
- [test_room_renderer.py](test_room_renderer.py.md) (3 shared connections)
- [__init__.py](__init__.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)

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