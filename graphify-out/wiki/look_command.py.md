# look_command.py

> 85 nodes

## Key Concepts

- **look_command.py** (57 connections) — `server/commands/look_command.py`
- **test_look_command.py** (26 connections) — `server/tests/unit/commands/test_look_command.py`
- **handle_look_command()** (18 connections) — `server/commands/look_command.py`
- **_handle_implicit_target_lookup()** (13 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (13 connections) — `server/commands/look_command.py`
- **_route_look_command()** (12 connections) — `server/commands/look_command.py`
- **_get_app_and_persistence()** (11 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (11 connections) — `server/commands/look_command.py`
- **_is_direction()** (11 connections) — `server/commands/look_helpers.py`
- **create_websocket_request_context()** (11 connections) — `server/realtime/request_context.py`
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

- [test_look_helpers.py](test_look_helpers.py.md) (12 shared connections)
- [test_look_room.py](test_look_room.py.md) (8 shared connections)
- [test_look_player.py](test_look_player.py.md) (8 shared connections)
- [test_look_item.py](test_look_item.py.md) (5 shared connections)
- [WebSocketRequestContext](WebSocketRequestContext.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_look_container.py](test_look_container.py.md) (4 shared connections)
- [test_look_npc.py](test_look_npc.py.md) (3 shared connections)
- [test_look_container_helpers.py](test_look_container_helpers.py.md) (3 shared connections)
- [command_service.py](command_service.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)

## Source Files

- `server/commands/look_command.py`
- `server/commands/look_helpers.py`
- `server/realtime/request_context.py`
- `server/tests/unit/commands/test_look_command.py`

## Audit Trail

- EXTRACTED: 244 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*