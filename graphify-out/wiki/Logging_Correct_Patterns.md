# Logging Correct Patterns

> 65 nodes · cohesion 0.04

## Key Concepts

- **log_with_context()** (18 connections) — `server/structured_logging/logging_context.py`
- **correct_patterns.py** (17 connections) — `docs/examples/logging/correct_patterns.py`
- **bind_request_context()** (15 connections) — `server/structured_logging/logging_context.py`
- **clear_request_context()** (11 connections) — `server/structured_logging/logging_context.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **correct_async_logging()** (5 connections) — `docs/examples/logging/correct_patterns.py`
- **correct_performance_logging()** (5 connections) — `docs/examples/logging/correct_patterns.py`
- **add_request_context()** (5 connections) — `docs/examples/logging/fastapi_integration.py`
- **WebSocketCorrelationMiddleware** (5 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (5 connections) — `server/middleware/correlation_middleware.py`
- **logging_context.py** (5 connections) — `server/structured_logging/logging_context.py`
- **get_current_context()** (5 connections) — `server/structured_logging/logging_context.py`
- **correct_exception_tracking()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **correct_request_context()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **database** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **.execute()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **risky_operation()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **_get_header()** (4 connections) — `server/middleware/correlation_middleware.py`
- **correct_database_logging()** (3 connections) — `docs/examples/logging/correct_patterns.py`
- **correct_error_handling()** (3 connections) — `docs/examples/logging/correct_patterns.py`
- **.query()** (3 connections) — `docs/examples/logging/correct_patterns.py`
- **process_data()** (3 connections) — `docs/examples/logging/correct_patterns.py`
- **create_websocket_correlation_middleware()** (3 connections) — `server/middleware/correlation_middleware.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (3 connections) — `server/structured_logging/logging_context.py`
- *... and 40 more nodes in this community*

## Relationships

- [[NPC Admin API]] (13 shared connections)
- [[FastAPI Auth Integration]] (8 shared connections)
- [[App Lifespan Management]] (3 shared connections)
- [[Memory Leak Metrics]] (3 shared connections)
- [[Logging Migration Examples]] (2 shared connections)
- [[FastAPI App Factory]] (2 shared connections)
- [[Logging Testing Examples]] (2 shared connections)
- [[WebSocket Auth Integration]] (2 shared connections)
- [[Performance Monitor Metrics]] (2 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `docs/examples/logging/fastapi_integration.py`
- `server/middleware/correlation_middleware.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/logging_context.py`

## Audit Trail

- EXTRACTED: 154 (78%)
- INFERRED: 43 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
