# middleware correlation rationale

> 49 nodes

## Key Concepts

- **fastapi_integration.py** (27 connections) — `docs/examples/logging/fastapi_integration.py`
- **bind_request_context()** (15 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (11 connections) — `server/structured_logging/logging_context.py`
- **websocket_endpoint()** (9 connections) — `docs/examples/logging/fastapi_integration.py`
- **update_player_background_task()** (8 connections) — `docs/examples/logging/fastapi_integration.py`
- **add_request_context()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **http_exception_handler()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **general_exception_handler()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **update_player_background()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **WebSocket** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **Request** (4 connections)
- **log_api_requests()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **auth_service()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **process_websocket_message()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **.verify_token()** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **BackgroundTasks** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **UploadFile** (3 connections) — `docs/examples/logging/fastapi_integration.py`
- **migration_example_5()** (3 connections) — `docs/examples/logging/migration_examples.py`
- **test_context_binding()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **test_logging_correlation_ids()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **Exception** (2 connections)
- **.update_player()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **.accept()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **.receive_text()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- *... and 24 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (11 shared connections)
- [models player related](models_player_related.md) (10 shared connections)
- [app factory rationale](app_factory_rationale.md) (4 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (3 shared connections)
- [examples logging testing](examples_logging_testing.md) (2 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (1 shared connections)
- [examples migration logging](examples_migration_logging.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/migration_examples.py`
- `docs/examples/logging/testing_examples.py`
- `server/structured_logging/logging_context.py`

## Audit Trail

- EXTRACTED: 133 (80%)
- INFERRED: 33 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*