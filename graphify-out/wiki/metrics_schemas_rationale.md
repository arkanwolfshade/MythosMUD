# metrics schemas rationale

> 121 nodes

## Key Concepts

- **test_metrics_endpoints.py** (37 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **metrics.py** (29 connections) — `server/api/metrics.py`
- **_admin_user()** (14 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **replay_dlq_message()** (13 connections) — `server/api/metrics.py`
- **StatusMessageResponse** (13 connections) — `server/schemas/metrics/metrics.py`
- **DLQReplayResponse** (13 connections) — `server/schemas/metrics/metrics.py`
- **metrics.py** (12 connections) — `server/schemas/metrics/metrics.py`
- **test_users_current_user_logging.py** (12 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **get_metrics()** (11 connections) — `server/api/metrics.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **MetricsSummaryResponse** (11 connections) — `server/schemas/metrics/metrics.py`
- **DLQMessagesResponse** (11 connections) — `server/schemas/metrics/metrics.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
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
- *... and 96 more nodes in this community*

## Relationships

- [player requests schemas](player_requests_schemas.md) (35 shared connections)
- [Exception Containers](Exception_Containers.md) (16 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (6 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [auth users rationale](auth_users_rationale.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)
- [middleware metrics collector](middleware_metrics_collector.md) (1 shared connections)
- [player service game](player_service_game.md) (1 shared connections)
- [combat validator validators](combat_validator_validators.md) (1 shared connections)
- [fixtures return shape](fixtures_return_shape.md) (1 shared connections)

## Source Files

- `server/api/metrics.py`
- `server/auth/users.py`
- `server/schemas/metrics/__init__.py`
- `server/schemas/metrics/metrics.py`
- `server/schemas/metrics/metrics_data.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/api/test_metrics_endpoints.py`
- `server/tests/unit/auth/test_users_current_user_logging.py`
- `server/tests/unit/models/test_user.py`

## Audit Trail

- EXTRACTED: 500 (89%)
- INFERRED: 59 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*