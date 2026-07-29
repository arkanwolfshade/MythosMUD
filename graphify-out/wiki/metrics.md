# metrics

> 80 nodes

## Key Concepts

- **test_metrics_endpoints.py** (37 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **metrics.py** (29 connections) — `server/api/metrics.py`
- **_admin_user()** (14 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **replay_dlq_message()** (13 connections) — `server/api/metrics.py`
- **StatusMessageResponse** (13 connections) — `server/schemas/metrics/metrics.py`
- **DLQReplayResponse** (13 connections) — `server/schemas/metrics/metrics.py`
- **metrics.py** (12 connections) — `server/schemas/metrics/metrics.py`
- **get_metrics()** (11 connections) — `server/api/metrics.py`
- **MetricsSummaryResponse** (11 connections) — `server/schemas/metrics/metrics.py`
- **DLQMessagesResponse** (11 connections) — `server/schemas/metrics/metrics.py`
- **Any** (10 connections)
- **reset_circuit_breaker()** (10 connections) — `server/api/metrics.py`
- **_load_dlq_message()** (10 connections) — `server/api/metrics.py`
- **delete_dlq_message()** (10 connections) — `server/api/metrics.py`
- **MetricsResponse** (10 connections) — `server/schemas/metrics/metrics.py`
- **verify_admin_access()** (9 connections) — `server/api/metrics.py`
- **Request** (9 connections)
- **get_metrics_summary()** (9 connections) — `server/api/metrics.py`
- **get_dlq_messages()** (9 connections) — `server/api/metrics.py`
- **MetricsData** (9 connections) — `server/schemas/metrics/metrics_data.py`
- **MetricsSummary** (9 connections) — `server/schemas/metrics/metrics_data.py`
- **DLQMessage** (9 connections) — `server/schemas/metrics/metrics_data.py`
- **DLQReplayDetails** (9 connections) — `server/schemas/metrics/metrics_data.py`
- **reset_metrics()** (8 connections) — `server/api/metrics.py`
- **_handle_replay_error()** (8 connections) — `server/api/metrics.py`
- *... and 55 more nodes in this community*

## Relationships

- [APIRouter](APIRouter.md) (32 shared connections)
- [Request](Request.md) (6 shared connections)
- [main()](main%28%29.md) (5 shared connections)
- [BaseUserManager](BaseUserManager.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [NATS](NATS.md) (1 shared connections)

## Source Files

- `server/api/metrics.py`
- `server/schemas/metrics/__init__.py`
- `server/schemas/metrics/metrics.py`
- `server/schemas/metrics/metrics_data.py`
- `server/tests/unit/api/test_metrics_endpoints.py`

## Audit Trail

- EXTRACTED: 390 (87%)
- INFERRED: 57 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*