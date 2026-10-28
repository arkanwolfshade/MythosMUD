# verify_enhanced_logging_compliance.py

> 82 nodes · cohesion 0.03

## Key Concepts

- **fastapi_integration.py** (27 connections) — `docs/examples/logging/fastapi_integration.py`
- **bind_request_context()** (21 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (16 connections) — `server/structured_logging/logging_context.py`
- **test_logging_context.py** (12 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **logging_context.py** (10 connections) — `server/structured_logging/logging_context.py`
- **get_current_context()** (10 connections) — `server/structured_logging/logging_context.py`
- **http_exception_handler()** (7 connections) — `docs/examples/logging/fastapi_integration.py`
- **player_service()** (7 connections) — `docs/examples/logging/fastapi_integration.py`
- **update_player_background_task()** (7 connections) — `docs/examples/logging/fastapi_integration.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **add_request_context()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **general_exception_handler()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **HTTPException** (6 connections)
- **upload_avatar()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **websocket_endpoint()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **create_player()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **list_players()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **update_player_background()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **WebSocket** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **.disconnect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **get_player()** (4 connections) — `docs/examples/logging/fastapi_integration.py`
- **auth_service()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **BackgroundTasks** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **process_websocket_message()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- *... and 57 more nodes in this community*

## Relationships

- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (11 shared connections)
- [_prepare_command_for_processing](_prepare_command_for_processing.md) (7 shared connections)
- [Room](Room.md) (5 shared connections)
- [AttributeError](AttributeError.md) (5 shared connections)
- [test_chat_validator.py](test_chat_validator.py.md) (3 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [manual_dependency_analysis.py](manual_dependency_analysis.py.md) (2 shared connections)
- [test_look_player.py](test_look_player.py.md) (2 shared connections)
- [test_player_repository_room.py](test_player_repository_room.py.md) (2 shared connections)
- [test_corpse_lifecycle_decay.py](test_corpse_lifecycle_decay.py.md) (2 shared connections)
- [PlayerMute](PlayerMute.md) (2 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/websocket_integration.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 145 (87%)
- INFERRED: 21 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*