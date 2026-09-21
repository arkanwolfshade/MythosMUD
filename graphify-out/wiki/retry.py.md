# retry.py

> 49 nodes

## Key Concepts

- **retry.py** (18 connections) — `server/utils/retry.py`
- **retry_with_backoff()** (14 connections) — `server/utils/retry.py`
- **is_transient_error()** (13 connections) — `server/utils/retry.py`
- **test_retry.py** (13 connections) — `server/tests/unit/utils/test_retry.py`
- **Exception** (9 connections)
- **test_retry_retries_wrapped_connection_closed_then_succeeds()** (5 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_cause_chain_connection_closed()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_wrapped_connection_closed()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_failure_then_success()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_success()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **_create_async_wrapper()** (4 connections) — `server/utils/retry.py`
- **_create_sync_wrapper()** (4 connections) — `server/utils/retry.py`
- **_is_psycopg2_transient()** (4 connections) — `server/utils/retry.py`
- **_is_wrapped_transient_message()** (4 connections) — `server/utils/retry.py`
- **_iter_exception_chain()** (4 connections) — `server/utils/retry.py`
- **_should_retry_error()** (4 connections) — `server/utils/retry.py`
- **test_is_transient_error_non_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_failure_then_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **_is_asyncpg_transient()** (3 connections) — `server/utils/retry.py`
- **asyncio** (3 connections)
- **_calculate_retry_delay()** (2 connections) — `server/utils/retry.py`
- **_log_retry_attempt()** (2 connections) — `server/utils/retry.py`
- **_log_retry_failure()** (2 connections) — `server/utils/retry.py`
- *... and 24 more nodes in this community*

## Relationships

- [get_session_maker](get_session_maker.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [_StubPlayerRepo](_StubPlayerRepo.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_retry.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 83 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*