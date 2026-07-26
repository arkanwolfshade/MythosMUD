# bind_request_context

> 23 nodes · cohesion 0.10

## Key Concepts

- **bind_request_context()** (15 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (11 connections) — `server/structured_logging/logging_context.py`
- **update_player_background_task()** (8 connections) — `docs/examples/logging/fastapi_integration.py`
- **logging_context.py** (6 connections) — `server/structured_logging/logging_context.py`
- **correct_async_logging()** (5 connections) — `docs/examples/logging/correct_patterns.py`
- **get_current_context()** (5 connections) — `server/structured_logging/logging_context.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **migration_example_5()** (3 connections) — `docs/examples/logging/migration_examples.py`
- **test_context_binding()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **test_logging_correlation_ids()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **Any** (3 connections)
- **async_work()** (2 connections) — `docs/examples/logging/correct_patterns.py`
- **.update_player()** (2 connections) — `docs/examples/logging/fastapi_integration.py`
- **Demonstrate correct request context binding.** (1 connections) — `docs/examples/logging/correct_patterns.py`
- **Demonstrate correct async logging patterns.** (1 connections) — `docs/examples/logging/correct_patterns.py`
- **Background task for player update with enhanced logging.** (1 connections) — `docs/examples/logging/fastapi_integration.py`
- **Example 5: Request context migration.** (1 connections) — `docs/examples/logging/migration_examples.py`
- **Test logging correlation IDs.** (1 connections) — `docs/examples/logging/testing_examples.py`
- **Test request context binding functionality.** (1 connections) — `docs/examples/logging/testing_examples.py`
- **Context management utilities for enhanced logging.  This module provides functio** (1 connections) — `server/structured_logging/logging_context.py`
- **Bind request context to the current logging context.      This function sets up** (1 connections) — `server/structured_logging/logging_context.py`
- **Clear the current request context from logging.** (1 connections) — `server/structured_logging/logging_context.py`
- **Get the current logging context.** (1 connections) — `server/structured_logging/logging_context.py`

## Relationships

- [lifespan.py](lifespan.py.md) (10 shared connections)
- [fastapi_integration.py](fastapi_integration.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [correlation_middleware.py](correlation_middleware.py.md) (4 shared connections)
- [testing_examples.py](testing_examples.py.md) (2 shared connections)
- [websocket_endpoint](websocket_endpoint.md) (2 shared connections)
- [player_service](player_service.md) (1 shared connections)
- [migration_examples.py](migration_examples.py.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/migration_examples.py`
- `docs/examples/logging/testing_examples.py`
- `server/structured_logging/logging_context.py`

## Audit Trail

- EXTRACTED: 51 (64%)
- INFERRED: 29 (36%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*