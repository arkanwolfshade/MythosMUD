# middleware correlation rationale

> 32 nodes

## Key Concepts

- **bind_request_context()** (15 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (11 connections) — `server/structured_logging/logging_context.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **logging_context.py** (6 connections) — `server/structured_logging/logging_context.py`
- **WebSocketCorrelationMiddleware** (5 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **get_current_context()** (5 connections) — `server/structured_logging/logging_context.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **_get_header()** (4 connections) — `server/middleware/correlation_middleware.py`
- **migration_example_5()** (3 connections) — `docs/examples/logging/migration_examples.py`
- **test_context_binding()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **test_logging_correlation_ids()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **create_websocket_correlation_middleware()** (3 connections) — `server/middleware/correlation_middleware.py`
- **Any** (3 connections)
- **Scope** (2 connections)
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- **Demonstrate correct request context binding.** (1 connections) — `docs/examples/logging/correct_patterns.py`
- **Example 5: Request context migration.** (1 connections) — `docs/examples/logging/migration_examples.py`
- **Test request context binding functionality.** (1 connections) — `docs/examples/logging/testing_examples.py`
- **Test logging correlation IDs.** (1 connections) — `docs/examples/logging/testing_examples.py`
- **Receive** (1 connections)
- **Send** (1 connections)
- **Return first header value for name (case-insensitive) from ASGI scope.** (1 connections) — `server/middleware/correlation_middleware.py`
- **ASGI application interface.          Args:             scope: ASGI connection sc** (1 connections) — `server/middleware/correlation_middleware.py`
- **Middleware for adding correlation IDs to WebSocket connections.      This middle** (1 connections) — `server/middleware/correlation_middleware.py`
- *... and 7 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [examples logging testing](examples_logging_testing.md) (2 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [lucidity active service](lucidity_active_service.md) (2 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (2 shared connections)
- [examples migration logging](examples_migration_logging.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/migration_examples.py`
- `docs/examples/logging/testing_examples.py`
- `server/middleware/correlation_middleware.py`
- `server/structured_logging/logging_context.py`

## Audit Trail

- EXTRACTED: 70 (71%)
- INFERRED: 28 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*