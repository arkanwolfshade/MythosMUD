# Retry Transient Errors

> 37 nodes

## Key Concepts

- **retry.py** (16 connections) — `server/utils/retry.py`
- **test_retry.py** (10 connections) — `server/tests/unit/utils/test_retry.py`
- **retry_with_backoff()** (10 connections) — `server/utils/retry.py`
- **is_transient_error()** (9 connections) — `server/utils/retry.py`
- **Exception** (8 connections)
- **_is_psycopg2_transient()** (4 connections) — `server/utils/retry.py`
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
- **Unit tests for retry utilities.  Tests the retry decorator and retry logic.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test is_transient_error() identifies transient errors.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test is_transient_error() returns False for non-transient errors.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() succeeds on first attempt.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() retries on failure then succeeds.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- *... and 12 more nodes in this community*

## Relationships

- [Schemas Maps Map](Schemas_Maps_Map.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_retry.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 115 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*