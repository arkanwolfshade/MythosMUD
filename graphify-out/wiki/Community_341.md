# Community 341

> 49 nodes

## Key Concepts

- **bind_request_context()** (20 connections) — `server/structured_logging/logging_context.py`
- **log_with_context()** (19 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (15 connections) — `server/structured_logging/logging_context.py`
- **test_websocket_correlation_context.py** (12 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **test_logging_context.py** (12 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **logging_context.py** (10 connections) — `server/structured_logging/logging_context.py`
- **get_current_context()** (9 connections) — `server/structured_logging/logging_context.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **update_player_background_task()** (7 connections) — `docs/examples/logging/fastapi_integration.py`
- **.disconnect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **test_connection_binds_context_fields_before_message_loop()** (5 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **_clear_context_around_test()** (4 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **test_message_loop_assigns_fresh_correlation_id_per_message()** (4 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **test_message_loop_ignores_client_supplied_correlation_id()** (4 connections) — `server/tests/unit/realtime/test_websocket_correlation_context.py`
- **.broadcast_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.connect()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.send_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_get_current_context_returns_empty_on_error()** (3 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **Any** (3 connections)
- **asyncio** (3 connections)
- **test_bind_request_context_generates_correlation_id()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_bind_request_context_omits_none_values()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- **test_clear_request_context()** (2 connections) — `server/tests/unit/structured_logging/test_logging_context.py`
- *... and 24 more nodes in this community*

## Relationships

- [Community 336](Community_336.md) (11 shared connections)
- [Community 301](Community_301.md) (6 shared connections)
- [Community 351](Community_351.md) (4 shared connections)
- [Community 430](Community_430.md) (3 shared connections)
- [Community 239](Community_239.md) (3 shared connections)
- [Community 255](Community_255.md) (3 shared connections)
- [Community 704](Community_704.md) (3 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (3 shared connections)
- [Community 183](Community_183.md) (2 shared connections)
- [Community 266](Community_266.md) (2 shared connections)
- [Community 583](Community_583.md) (2 shared connections)
- [Community 447](Community_447.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/websocket_integration.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`
- `server/tests/unit/realtime/test_websocket_correlation_context.py`
- `server/tests/unit/structured_logging/test_logging_context.py`

## Audit Trail

- EXTRACTED: 87 (74%)
- INFERRED: 31 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*