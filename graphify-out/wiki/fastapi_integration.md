# fastapi integration

> 40 nodes

## Key Concepts

- **bind_request_context()** (15 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (11 connections) — `server/structured_logging/logging_context.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **CorrelationMiddleware** (6 connections) — `server/middleware/correlation_middleware.py`
- **logging_context.py** (6 connections) — `server/structured_logging/logging_context.py`
- **WebSocketCorrelationMiddleware** (5 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **get_current_context()** (5 connections) — `server/structured_logging/logging_context.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **_get_header()** (4 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (4 connections) — `server/middleware/correlation_middleware.py`
- **migration_example_5()** (3 connections) — `docs/examples/logging/migration_examples.py`
- **test_context_binding()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **test_logging_correlation_ids()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (3 connections) — `server/middleware/correlation_middleware.py`
- **Any** (3 connections)
- **Scope** (2 connections)
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- **Any** (2 connections)
- **Demonstrate correct request context binding.** (1 connections) — `docs/examples/logging/correct_patterns.py`
- **Example 5: Request context migration.** (1 connections) — `docs/examples/logging/migration_examples.py`
- **Test request context binding functionality.** (1 connections) — `docs/examples/logging/testing_examples.py`
- **Test logging correlation IDs.** (1 connections) — `docs/examples/logging/testing_examples.py`
- **ASGIApp** (1 connections)
- *... and 15 more nodes in this community*

## Relationships

- [world](world.md) (12 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (6 shared connections)
- [item](item.md) (3 shared connections)
- [testing examples](testing_examples.md) (2 shared connections)
- [websocket integration](websocket_integration.md) (2 shared connections)
- [migration examples](migration_examples.md) (1 shared connections)
- [Tests for get container dependency](Tests_for_get_container_dependency.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/migration_examples.py`
- `docs/examples/logging/testing_examples.py`
- `server/middleware/correlation_middleware.py`
- `server/structured_logging/logging_context.py`

## Audit Trail

- EXTRACTED: 89 (76%)
- INFERRED: 28 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*