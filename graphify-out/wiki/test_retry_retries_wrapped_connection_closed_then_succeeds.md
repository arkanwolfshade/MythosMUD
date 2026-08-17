# test_retry_retries_wrapped_connection_closed_then_succeeds

> 8 nodes

## Key Concepts

- **test_retry_retries_wrapped_connection_closed_then_succeeds()** (5 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_failure_then_success()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_success()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **.get_player_by_id()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **asyncio** (3 connections)
- **Test retry_with_backoff() with async function succeeds on first attempt.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() with async function retries on failure then succeeds.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Retry decorator must not treat wrapped closed-connection as final on attempt 1.** (1 connections) — `server/tests/unit/utils/test_retry.py`

## Relationships

- [get_session_maker](get_session_maker.md) (3 shared connections)
- [test_retry.py](test_retry.py.md) (3 shared connections)
- [_StubPlayerRepo](_StubPlayerRepo.md) (2 shared connections)

## Source Files

- `server/tests/unit/persistence/test_protocols.py`
- `server/tests/unit/utils/test_retry.py`

## Audit Trail

- EXTRACTED: 14 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*