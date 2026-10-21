# _RecordingRoom

> 85 nodes · cohesion 0.05

## Key Concepts

- **look_command.py** (58 connections) — `server/commands/look_command.py`
- **test_look_command.py** (25 connections) — `server/tests/unit/commands/test_look_command.py`
- **handle_look_command()** (18 connections) — `server/commands/look_command.py`
- **LookRequest** (15 connections) — `server/commands/look_helpers.py`
- **_handle_implicit_target_lookup()** (14 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (13 connections) — `server/commands/look_command.py`
- **_route_look_command()** (12 connections) — `server/commands/look_command.py`
- **_get_app_and_persistence()** (11 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (11 connections) — `server/commands/look_command.py`
- **_get_room_drops()** (10 connections) — `server/commands/look_command.py`
- **FastAPI** (10 connections)
- **_try_direction_look()** (10 connections) — `server/commands/look_command.py`
- **_try_explicit_player_look()** (10 connections) — `server/commands/look_command.py`
- **asyncio** (10 connections)
- **_LookPersistence** (9 connections) — `server/commands/look_command.py`
- **LookRouteCtx** (9 connections) — `server/commands/look_command.py`
- **CommandResponse** (9 connections)
- **_try_explicit_container_look()** (9 connections) — `server/commands/look_command.py`
- **_try_explicit_item_look()** (9 connections) — `server/commands/look_command.py`
- **_as_response()** (8 connections) — `server/commands/look_command.py`
- **_container_from_app()** (7 connections) — `server/commands/look_command.py`
- **_LookRoom** (7 connections) — `server/commands/look_command.py`
- **_connection_manager_from_app()** (6 connections) — `server/commands/look_command.py`
- **_prototype_registry_from_app()** (6 connections) — `server/commands/look_command.py`
- **_try_implicit_target_lookup()** (6 connections) — `server/commands/look_command.py`
- *... and 60 more nodes in this community*

## Relationships

- [look_helpers.py](look_helpers.py.md) (8 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (7 shared connections)
- [command_parser.py](command_parser.py.md) (6 shared connections)
- [asyncio](asyncio.md) (6 shared connections)
- [Actionable Recommendations](Actionable_Recommendations.md) (5 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (5 shared connections)
- [test_logout_commands.py](test_logout_commands.py.md) (3 shared connections)
- [test_hallucination_services.py](test_hallucination_services.py.md) (3 shared connections)
- [PlayerRepositoryProtocol](PlayerRepositoryProtocol.md) (3 shared connections)
- [test_logging_file_categories.py](test_logging_file_categories.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (2 shared connections)

## Source Files

- `server/commands/look_command.py`
- `server/commands/look_helpers.py`
- `server/tests/unit/commands/test_look_command.py`

## Audit Trail

- EXTRACTED: 235 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*