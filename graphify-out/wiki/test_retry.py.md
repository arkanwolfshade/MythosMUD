# test_retry.py

> 19 nodes

## Key Concepts

- **test_retry.py** (14 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_cause_chain_connection_closed()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_wrapped_connection_closed()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_failure_then_success()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_success()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_non_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_failure_then_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **asyncio** (3 connections)
- **Unit tests for retry utilities. Tests the retry decorator and retry logic.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() with async function succeeds on first attempt.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test is_transient_error() identifies transient errors.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() with async function retries on failure then succeeds.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test is_transient_error() returns False for non-transient errors.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **DatabaseError wrapping asyncpg closed-connection must still retry (e2e…** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **__cause__ ConnectionDoesNotExistError makes the outer wrapper transient.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() succeeds on first attempt.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() retries on failure then succeeds.** (1 connections) — `server/tests/unit/utils/test_retry.py`

## Relationships

- [DatabaseError](DatabaseError.md) (8 shared connections)
- [is_transient_error](is_transient_error.md) (5 shared connections)
- [_StubPlayerRepo](_StubPlayerRepo.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_retry.py`

## Audit Trail

- EXTRACTED: 33 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*