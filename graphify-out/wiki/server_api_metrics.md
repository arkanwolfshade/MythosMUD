# server api metrics

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

- [claude rules fastapi](claude_rules_fastapi.md) (21 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (15 shared connections)
- [server api players get player](server_api_players_get_player.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [leveluphook](leveluphook.md) (1 shared connections)
- [scripts generate openapi spec](scripts_generate_openapi_spec.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

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