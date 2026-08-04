# middleware correlation rationale

> 47 nodes

## Key Concepts

- **fastapi_integration.py** (27 connections) — `docs/examples/logging/fastapi_integration.py`
- **websocket_endpoint()** (9 connections) — `docs/examples/logging/fastapi_integration.py`
- **HTTPException** (6 connections)
- **upload_avatar()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **create_player()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **http_exception_handler()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **general_exception_handler()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **update_player_background()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **list_players()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **WebSocket** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **Request** (4 connections)
- **get_player()** (4 connections) — `docs/examples/logging/fastapi_integration.py`
- **get_current_user()** (4 connections) — `docs/examples/logging/fastapi_integration.py`
- **log_api_requests()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **auth_service()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **process_websocket_message()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **.verify_token()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **BackgroundTasks** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **UploadFile** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **Exception** (2 connections)
- **.create_player()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **.get_player()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **.list_players()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **.upload_avatar()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **.accept()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- *... and 22 more nodes in this community*

## Relationships

- [world loader room](world_loader_room.md) (6 shared connections)
- [models player related](models_player_related.md) (5 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (5 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (3 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (2 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`

## Audit Trail

- EXTRACTED: 143 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*