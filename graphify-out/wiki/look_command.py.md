# look_command.py

> 85 nodes

## Key Concepts

- **look_command.py** (58 connections) — `server/commands/look_command.py`
- **test_look_command.py** (26 connections) — `server/tests/unit/commands/test_look_command.py`
- **handle_look_command()** (18 connections) — `server/commands/look_command.py`
- **LookRequest** (15 connections) — `server/commands/look_helpers.py`
- **_handle_implicit_target_lookup()** (14 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (13 connections) — `server/commands/look_command.py`
- **_route_look_command()** (12 connections) — `server/commands/look_command.py`
- **_get_app_and_persistence()** (11 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (11 connections) — `server/commands/look_command.py`
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
- **_try_implicit_target_lookup()** (6 connections) — `server/commands/look_command.py`
- *... and 60 more nodes in this community*

## Relationships

- [test_look_room.py](test_look_room.py.md) (10 shared connections)
- [test_look_container_helpers.py](test_look_container_helpers.py.md) (8 shared connections)
- [test_look_helpers.py](test_look_helpers.py.md) (6 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [test_look_player.py](test_look_player.py.md) (5 shared connections)
- [_find_item_in_equipped](_find_item_in_equipped.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_look_container.py](test_look_container.py.md) (3 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (3 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)

## Source Files

- `server/commands/look_command.py`
- `server/commands/look_helpers.py`
- `server/tests/unit/commands/test_look_command.py`

## Audit Trail

- EXTRACTED: 236 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*