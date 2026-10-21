# test_websocket_handler_helpers_extended.py

> 83 nodes · cohesion 0.06

## Key Concepts

- **test_metrics_endpoints.py** (37 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **api/metrics.py** (30 connections) — `server/api/metrics.py`
- **replay_dlq_message()** (14 connections) — `server/api/metrics.py`
- **_admin_user()** (14 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **asyncio** (14 connections)
- **metrics/metrics.py** (12 connections) — `server/schemas/metrics/metrics.py`
- **delete_dlq_message()** (11 connections) — `server/api/metrics.py`
- **get_metrics()** (11 connections) — `server/api/metrics.py`
- **reset_circuit_breaker()** (11 connections) — `server/api/metrics.py`
- **get_dlq_messages()** (10 connections) — `server/api/metrics.py`
- **get_metrics_summary()** (10 connections) — `server/api/metrics.py`
- **_load_dlq_message()** (10 connections) — `server/api/metrics.py`
- **DLQReplayResponse** (10 connections) — `server/schemas/metrics/metrics.py`
- **Any** (9 connections)
- **reset_metrics()** (9 connections) — `server/api/metrics.py`
- **verify_admin_access()** (9 connections) — `server/api/metrics.py`
- **metrics/__init__.py** (9 connections) — `server/schemas/metrics/__init__.py`
- **StatusMessageResponse** (9 connections) — `server/schemas/metrics/metrics.py`
- **_handle_replay_error()** (8 connections) — `server/api/metrics.py`
- **DLQMessagesResponse** (8 connections) — `server/schemas/metrics/metrics.py`
- **MetricsSummaryResponse** (8 connections) — `server/schemas/metrics/metrics.py`
- **_replay_message_safely()** (7 connections) — `server/api/metrics.py`
- **MetricsResponse** (7 connections) — `server/schemas/metrics/metrics.py`
- **Path** (7 connections)
- **_get_nats_handler()** (6 connections) — `server/api/metrics.py`
- *... and 58 more nodes in this community*

## Relationships

- [test_security_validator.py](test_security_validator.py.md) (15 shared connections)
- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (14 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (9 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [Room](Room.md) (3 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (3 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (1 shared connections)

## Source Files

- `server/api/metrics.py`
- `server/schemas/metrics/__init__.py`
- `server/schemas/metrics/metrics.py`
- `server/schemas/metrics/metrics_data.py`
- `server/tests/unit/api/test_metrics_endpoints.py`

## Audit Trail

- EXTRACTED: 236 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*