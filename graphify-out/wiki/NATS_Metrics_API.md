# NATS Metrics API

> 59 nodes · cohesion 0.10

## Key Concepts

- **test_metrics_endpoints.py** (35 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **metrics.py** (28 connections) — `server/api/metrics.py`
- **User** (15 connections) — `server/api/metrics.py`
- **Any** (14 connections) — `server/api/metrics.py`
- **replay_dlq_message()** (13 connections) — `server/api/metrics.py`
- **_admin_user()** (13 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **Request** (13 connections) — `server/api/metrics.py`
- **DLQReplayResponse** (12 connections) — `server/api/metrics.py`
- **StatusMessageResponse** (12 connections) — `server/api/metrics.py`
- **delete_dlq_message()** (10 connections) — `server/api/metrics.py`
- **get_metrics()** (10 connections) — `server/api/metrics.py`
- **_load_dlq_message()** (10 connections) — `server/api/metrics.py`
- **reset_circuit_breaker()** (10 connections) — `server/api/metrics.py`
- **DLQMessagesResponse** (10 connections) — `server/api/metrics.py`
- **MetricsSummaryResponse** (10 connections) — `server/api/metrics.py`
- **MetricsResponse** (10 connections) — `server/api/metrics.py`
- **get_dlq_messages()** (9 connections) — `server/api/metrics.py`
- **get_metrics_summary()** (9 connections) — `server/api/metrics.py`
- **_handle_replay_error()** (9 connections) — `server/api/metrics.py`
- **verify_admin_access()** (9 connections) — `server/api/metrics.py`
- **Path** (9 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **_replay_message_safely()** (8 connections) — `server/api/metrics.py`
- **reset_metrics()** (8 connections) — `server/api/metrics.py`
- **Path** (7 connections) — `server/api/metrics.py`
- **_get_nats_handler()** (6 connections) — `server/api/metrics.py`
- *... and 34 more nodes in this community*

## Relationships

- [[Container Exception Handlers]] (11 shared connections)
- [[NPC Admin API]] (8 shared connections)
- [[Admin NPC Schemas]] (7 shared connections)
- [[API Test Fixtures]] (3 shared connections)
- [[Database Manager Tests]] (2 shared connections)
- [[FastAPI App Factory]] (1 shared connections)

## Source Files

- `server/api/metrics.py`
- `server/tests/unit/api/test_metrics_endpoints.py`

## Audit Trail

- EXTRACTED: 306 (81%)
- INFERRED: 74 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
