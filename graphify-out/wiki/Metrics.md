# Metrics

> 84 nodes

## Key Concepts

- **test_metrics_endpoints.py** (39 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **api/metrics.py** (31 connections) — `server/api/metrics.py`
- **replay_dlq_message()** (14 connections) — `server/api/metrics.py`
- **_admin_user()** (14 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **asyncio** (14 connections)
- **metrics/metrics.py** (13 connections) — `server/schemas/metrics/metrics.py`
- **delete_dlq_message()** (11 connections) — `server/api/metrics.py`
- **get_metrics()** (11 connections) — `server/api/metrics.py`
- **reset_circuit_breaker()** (11 connections) — `server/api/metrics.py`
- **DLQReplayResponse** (10 connections) — `server/schemas/metrics/metrics.py`
- **get_dlq_messages()** (10 connections) — `server/api/metrics.py`
- **get_metrics_summary()** (10 connections) — `server/api/metrics.py`
- **_load_dlq_message()** (10 connections) — `server/api/metrics.py`
- **StatusMessageResponse** (9 connections) — `server/schemas/metrics/metrics.py`
- **reset_metrics()** (9 connections) — `server/api/metrics.py`
- **verify_admin_access()** (9 connections) — `server/api/metrics.py`
- **Any** (9 connections)
- **metrics/__init__.py** (9 connections) — `server/schemas/metrics/__init__.py`
- **DLQMessagesResponse** (8 connections) — `server/schemas/metrics/metrics.py`
- **MetricsSummaryResponse** (8 connections) — `server/schemas/metrics/metrics.py`
- **_handle_replay_error()** (8 connections) — `server/api/metrics.py`
- **Request** (8 connections)
- **MetricsResponse** (7 connections) — `server/schemas/metrics/metrics.py`
- **_replay_message_safely()** (7 connections) — `server/api/metrics.py`
- **metrics_data.py** (7 connections) — `server/schemas/metrics/metrics_data.py`
- *... and 59 more nodes in this community*

## Relationships

- [Container Exception Handling](Container_Exception_Handling.md) (19 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (15 shared connections)
- [Npc Admin](Npc_Admin.md) (6 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (2 shared connections)
- [Command Aliases](Command_Aliases.md) (2 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (1 shared connections)

## Source Files

- `server/api/metrics.py`
- `server/schemas/metrics/__init__.py`
- `server/schemas/metrics/metrics.py`
- `server/schemas/metrics/metrics_data.py`
- `server/tests/unit/api/test_metrics_endpoints.py`

## Audit Trail

- EXTRACTED: 241 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*