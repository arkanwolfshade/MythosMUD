# LoggedHTTPException

> 89 nodes

## Key Concepts

- **LoggedHTTPException** (358 connections) — `server/exceptions.py`
- **test_metrics_endpoints.py** (37 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **api/metrics.py** (30 connections) — `server/api/metrics.py`
- **replay_dlq_message()** (14 connections) — `server/api/metrics.py`
- **_admin_user()** (14 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **asyncio** (14 connections)
- **get_metrics()** (12 connections) — `server/api/metrics.py`
- **metrics/metrics.py** (12 connections) — `server/schemas/metrics/metrics.py`
- **delete_dlq_message()** (11 connections) — `server/api/metrics.py`
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
- *... and 64 more nodes in this community*

## Relationships

- [User](User.md) (39 shared connections)
- [PlayerService](PlayerService.md) (30 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (24 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (23 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (21 shared connections)
- [LootAllRequest](LootAllRequest.md) (19 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (19 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (19 shared connections)
- [models/user.py](models-user.py.md) (19 shared connections)
- [maps.py](maps.py.md) (16 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (14 shared connections)
- [real_time.py](real_time.py.md) (14 shared connections)

## Source Files

- `server/api/metrics.py`
- `server/exceptions.py`
- `server/schemas/metrics/__init__.py`
- `server/schemas/metrics/metrics.py`
- `server/schemas/metrics/metrics_data.py`
- `server/tests/unit/api/test_metrics_endpoints.py`
- `server/tests/unit/test_exceptions.py`

## Audit Trail

- EXTRACTED: 449 (76%)
- INFERRED: 144 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*