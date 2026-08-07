# retry rationale transient()

> 48 nodes

## Key Concepts

- **retry.py** (18 connections) — `server/utils/retry.py`
- **test_retry.py** (13 connections) — `server/tests/unit/utils/test_retry.py`
- **is_transient_error()** (13 connections) — `server/utils/retry.py`
- **retry_with_backoff()** (11 connections) — `server/utils/retry.py`
- **Exception** (9 connections)
- **test_is_transient_error_wrapped_connection_closed()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_cause_chain_connection_closed()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_retries_wrapped_connection_closed_then_succeeds()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **_is_psycopg2_transient()** (4 connections) — `server/utils/retry.py`
- **_is_wrapped_transient_message()** (4 connections) — `server/utils/retry.py`
- **_iter_exception_chain()** (4 connections) — `server/utils/retry.py`
- **_should_retry_error()** (4 connections) — `server/utils/retry.py`
- **_create_async_wrapper()** (4 connections) — `server/utils/retry.py`
- **_create_sync_wrapper()** (4 connections) — `server/utils/retry.py`
- **test_is_transient_error_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_non_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_failure_then_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_failure_then_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **_is_asyncpg_transient()** (3 connections) — `server/utils/retry.py`
- **_calculate_retry_delay()** (2 connections) — `server/utils/retry.py`
- **_log_retry_failure()** (2 connections) — `server/utils/retry.py`
- **_log_retry_attempt()** (2 connections) — `server/utils/retry.py`
- **Any** (2 connections)
- *... and 23 more nodes in this community*

## Relationships

- [logging examples fastapi](logging_examples_fastapi.md) (3 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (2 shared connections)
- [level curve game](level_curve_game.md) (2 shared connections)
- [persistence protocols rationale](persistence_protocols_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_retry.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 149 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*