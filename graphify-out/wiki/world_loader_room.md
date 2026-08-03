# world loader room

> 24 nodes

## Key Concepts

- **bind_request_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (13 connections) — `server/structured_logging/logging_context.py`
- **test_logging_context.py** (12 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **get_current_context()** (8 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (7 connections) — `server/structured_logging/logging_context.py`
- **add_request_context()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **Any** (3 connections)
- **test_get_current_context_returns_empty_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Any** (2 connections)
- **test_bind_request_context_generates_correlation_id()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_bind_request_context_omits_none_values()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_clear_request_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_get_current_context_returns_contextvars()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_log_with_context_merges_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Demonstrate correct request context binding.** (1 connections) — `docs/examples/logging/correct_patterns.py`
- **Add request context to all log entries using enhanced logging.** (1 connections) — `docs/examples/logging/fastapi_integration.py`
- **Process the WebSocket connection with correlation ID.          Args:** (1 connections) — `server/middleware/correlation_middleware.py`
- **Context management utilities for enhanced logging.  This module provides functio** (1 connections) — `server/structured_logging/logging_context.py`
- **Bind request context to the current logging context.      This function sets up** (1 connections) — `server/structured_logging/logging_context.py`
- **Clear the current request context from logging.** (1 connections) — `server/structured_logging/logging_context.py`
- **Get the current logging context.** (1 connections) — `server/structured_logging/logging_context.py`
- **Unit tests for logging_context utilities.** (1 connections) — `server/tests/unit/structured_logging/test_logging_context.py`

## Relationships

- [middleware correlation rationale](middleware_correlation_rationale.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [app factory rationale](app_factory_rationale.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (3 shared connections)
- [examples logging testing](examples_logging_testing.md) (2 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (2 shared connections)
- [examples migration logging](examples_migration_logging.md) (1 shared connections)
- [look helpers commands](look_helpers_commands.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `server/middleware/correlation_middleware.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 72 (73%)
- INFERRED: 26 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*