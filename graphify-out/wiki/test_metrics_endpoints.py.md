# test_metrics_endpoints.py

> 32 nodes · cohesion 0.12

## Key Concepts

- **test_metrics_endpoints.py** (37 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **_admin_user()** (14 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **delete_dlq_message()** (10 connections) — `server/api/metrics.py`
- **_load_dlq_message()** (10 connections) — `server/api/metrics.py`
- **verify_admin_access()** (9 connections) — `server/api/metrics.py`
- **reset_metrics()** (8 connections) — `server/api/metrics.py`
- **Path** (8 connections)
- **test_delete_dlq_message_404_when_missing_file()** (5 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_delete_dlq_message_success()** (4 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_get_metrics_wraps_unexpected_errors()** (4 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_replay_dlq_message_success_removes_from_dlq()** (4 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_reset_circuit_breaker_503_without_handler()** (4 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_verify_admin_access_rejects_non_admin()** (4 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **Path** (3 connections)
- **_plain_user()** (3 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_get_dlq_messages_empty_when_no_handler()** (3 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_get_metrics_merges_nats_and_handler()** (3 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_get_metrics_summary_adds_dlq_and_circuit()** (3 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_handle_replay_error_returns_failed_payload()** (3 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_load_dlq_message_accepts_legacy_message_key()** (3 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_load_dlq_message_missing_file()** (3 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_load_dlq_message_reads_data_key()** (3 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_load_dlq_message_rejects_bad_payload()** (3 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_reset_circuit_breaker_calls_reset()** (3 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- **test_reset_metrics_success()** (3 connections) — `server/tests/unit/api/test_metrics_endpoints.py`
- *... and 7 more nodes in this community*

## Relationships

- [metrics.py](metrics.py.md) (31 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (10 shared connections)
- [User](User.md) (7 shared connections)
- [exceptions.py](exceptions.py.md) (1 shared connections)

## Source Files

- `server/api/metrics.py`
- `server/tests/unit/api/test_metrics_endpoints.py`

## Audit Trail

- EXTRACTED: 160 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*