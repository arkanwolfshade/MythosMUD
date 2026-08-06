# middleware correlation rationale

> 82 nodes

## Key Concepts

- **fastapi_integration.py** (27 connections) — `docs/examples/logging/fastapi_integration.py`
- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **bind_request_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (13 connections) — `server/structured_logging/logging_context.py`
- **test_logging_context.py** (12 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **websocket_endpoint()** (9 connections) — `docs/examples/logging/fastapi_integration.py`
- **update_player_background_task()** (8 connections) — `docs/examples/logging/fastapi_integration.py`
- **get_current_context()** (8 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (7 connections) — `server/structured_logging/logging_context.py`
- **HTTPException** (6 connections)
- **upload_avatar()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **correct_async_logging()** (5 connections) — `docs/examples/logging/correct_patterns.py`
- **add_request_context()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **create_player()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **http_exception_handler()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **general_exception_handler()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **update_player_background()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **list_players()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **WebSocket** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **Request** (4 connections)
- **get_player()** (4 connections) — `docs/examples/logging/fastapi_integration.py`
- **get_current_user()** (4 connections) — `docs/examples/logging/fastapi_integration.py`
- **log_api_requests()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- *... and 57 more nodes in this community*

## Relationships

- [models lucidity rationale](models_lucidity_rationale.md) (8 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (7 shared connections)
- [models player related](models_player_related.md) (6 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [player game schema](player_game_schema.md) (5 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (3 shared connections)
- [room cache services](room_cache_services.md) (3 shared connections)
- [app factory rationale](app_factory_rationale.md) (2 shared connections)
- [examples logging testing](examples_logging_testing.md) (2 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (2 shared connections)
- [command commands validation](command_commands_validation.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `server/middleware/correlation_middleware.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 242 (83%)
- INFERRED: 48 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*