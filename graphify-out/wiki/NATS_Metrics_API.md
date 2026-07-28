# NATS Metrics API

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
- **_replay_message_safely()** (7 connections) — `server/api/metrics.py`
- **_get_nats_handler()** (6 connections) — `server/api/metrics.py`
- **metrics_data.py** (6 connections) — `server/schemas/metrics/metrics_data.py`
- **MetricsResponse** (5 connections)
- **BaseModel** (5 connections)
- *... and 23 more nodes in this community*

## Relationships

- [Dual Connection Deployment](Dual_Connection_Deployment.md) (31 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (10 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (6 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (6 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (3 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Community 2199](Community_2199.md) (1 shared connections)
- [Community 2205](Community_2205.md) (1 shared connections)

## Source Files

- `server/api/metrics.py`
- `server/schemas/metrics/__init__.py`
- `server/schemas/metrics/metrics.py`
- `server/schemas/metrics/metrics_data.py`

## Audit Trail

- EXTRACTED: 230 (83%)
- INFERRED: 48 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*