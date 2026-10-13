# Community 435

> 40 nodes

## Key Concepts

- **bind_request_context()** (21 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (16 connections) — `server/structured_logging/logging_context.py`
- **test_logging_context.py** (12 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **get_current_context()** (10 connections) — `server/structured_logging/logging_context.py`
- **logging_context.py** (10 connections) — `server/structured_logging/logging_context.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **update_player_background_task()** (7 connections) — `docs/examples/logging/fastapi_integration.py`
- **add_request_context()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **websocket_endpoint()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **.disconnect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **_clear_context_around_test()** (4 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **.broadcast_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.connect()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.send_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **test_get_current_context_returns_empty_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Any** (3 connections)
- **test_bind_request_context_generates_correlation_id()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_bind_request_context_omits_none_values()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_clear_request_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_get_current_context_returns_contextvars()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_log_with_context_merges_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **.__init__()** (1 connections) — `docs/examples/logging/websocket_integration.py`
- **websocket** (1 connections)
- **fixture** (1 connections)
- *... and 15 more nodes in this community*

## Relationships

- [Community 229](Community_229.md) (10 shared connections)
- [Community 307](Community_307.md) (6 shared connections)
- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (5 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (4 shared connections)
- [Community 423](Community_423.md) (3 shared connections)
- [Community 589](Community_589.md) (3 shared connections)
- [Community 647](Community_647.md) (3 shared connections)
- [Community 95](Community_95.md) (2 shared connections)
- [Community 280](Community_280.md) (2 shared connections)
- [Community 285](Community_285.md) (1 shared connections)
- [Community 466](Community_466.md) (1 shared connections)
- [Community 170](Community_170.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/websocket_integration.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/realtime/test_websocket_correlation_context.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 77 (80%)
- INFERRED: 19 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*