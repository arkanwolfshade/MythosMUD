# metrics.py

> 48 nodes · cohesion 0.10

## Key Concepts

- **metrics.py** (29 connections) — `server/api/metrics.py`
- **replay_dlq_message()** (13 connections) — `server/api/metrics.py`
- **DLQReplayResponse** (13 connections) — `server/schemas/metrics/metrics.py`
- **StatusMessageResponse** (13 connections) — `server/schemas/metrics/metrics.py`
- **metrics.py** (12 connections) — `server/schemas/metrics/metrics.py`
- **get_metrics()** (11 connections) — `server/api/metrics.py`
- **DLQMessagesResponse** (11 connections) — `server/schemas/metrics/metrics.py`
- **MetricsSummaryResponse** (11 connections) — `server/schemas/metrics/metrics.py`
- **Any** (10 connections)
- **reset_circuit_breaker()** (10 connections) — `server/api/metrics.py`
- **MetricsResponse** (10 connections) — `server/schemas/metrics/metrics.py`
- **get_dlq_messages()** (9 connections) — `server/api/metrics.py`
- **get_metrics_summary()** (9 connections) — `server/api/metrics.py`
- **Request** (9 connections)
- **DLQMessage** (9 connections) — `server/schemas/metrics/metrics_data.py`
- **DLQReplayDetails** (9 connections) — `server/schemas/metrics/metrics_data.py`
- **MetricsData** (9 connections) — `server/schemas/metrics/metrics_data.py`
- **MetricsSummary** (9 connections) — `server/schemas/metrics/metrics_data.py`
- **_handle_replay_error()** (8 connections) — `server/api/metrics.py`
- **__init__.py** (8 connections) — `server/schemas/metrics/__init__.py`
- **MetricsResponse** (7 connections)
- **_replay_message_safely()** (7 connections) — `server/api/metrics.py`
- **_get_nats_handler()** (6 connections) — `server/api/metrics.py`
- **metrics_data.py** (6 connections) — `server/schemas/metrics/metrics_data.py`
- **BaseModel** (5 connections)
- *... and 23 more nodes in this community*

## Relationships

- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (31 shared connections)
- [User](User.md) (10 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [__init__.py](__init__.py.md) (6 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [dependencies.py](dependencies.py.md) (1 shared connections)
- [exceptions.py](exceptions.py.md) (1 shared connections)
- [factory.py](factory.py.md) (1 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (1 shared connections)

## Source Files

- `server/api/metrics.py`
- `server/schemas/metrics/__init__.py`
- `server/schemas/metrics/metrics.py`
- `server/schemas/metrics/metrics_data.py`

## Audit Trail

- EXTRACTED: 230 (82%)
- INFERRED: 49 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*