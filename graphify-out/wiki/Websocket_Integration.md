# Websocket Integration

> 39 nodes

## Key Concepts

- **log_with_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **bind_request_context()** (16 connections) — `server/structured_logging/logging_context.py`
- **test_logging_context.py** (13 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **clear_request_context()** (11 connections) — `server/structured_logging/logging_context.py`
- **get_current_context()** (8 connections) — `server/structured_logging/logging_context.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **add_request_context()** (6 connections) — `docs/examples/logging/fastapi_integration.py`
- **.disconnect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **test_context_binding()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **test_logging_correlation_ids()** (3 connections) — `docs/examples/logging/testing_examples.py`
- **.broadcast_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.connect()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.send_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_get_current_context_returns_empty_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Any** (3 connections)
- **test_bind_request_context_generates_correlation_id()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_bind_request_context_omits_none_values()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_clear_request_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_get_current_context_returns_contextvars()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_log_with_context_merges_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **.__init__()** (1 connections) — `docs/examples/logging/websocket_integration.py`
- **BoundLogger** (1 connections)
- **Demonstrate correct request context binding.** (1 connections) — `docs/examples/logging/correct_patterns.py`
- *... and 14 more nodes in this community*

## Relationships

- [Fastapi Integration](Fastapi_Integration.md) (5 shared connections)
- [Test Websocket Helpers](Test_Websocket_Helpers.md) (5 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (4 shared connections)
- [Test Error Logging](Test_Error_Logging.md) (4 shared connections)
- [Correct Patterns](Correct_Patterns.md) (3 shared connections)
- [Monitoring Dashboard](Monitoring_Dashboard.md) (3 shared connections)
- [Testing Examples](Testing_Examples.md) (2 shared connections)
- [Performance Monitor](Performance_Monitor.md) (2 shared connections)
- [Websocket Integration](Websocket_Integration.md) (1 shared connections)
- [Test Security Headers](Test_Security_Headers.md) (1 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (1 shared connections)
- [Migration Examples](Migration_Examples.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/testing_examples.py`
- `docs/examples/logging/websocket_integration.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 61 (69%)
- INFERRED: 28 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*