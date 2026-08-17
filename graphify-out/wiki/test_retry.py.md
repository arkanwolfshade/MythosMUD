# test_retry.py

> 24 nodes

## Key Concepts

- **retry_with_backoff()** (14 connections) — `server/utils/retry.py`
- **test_retry.py** (14 connections) — `server/tests/unit/utils/test_retry.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **test_is_transient_error_cause_chain_connection_closed()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_wrapped_connection_closed()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_failure_then_success()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_success()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_non_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_failure_then_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **asyncio** (3 connections)
- **F** (1 connections)
- **Get a player by ID. Args: player_id: Player UUID Returns: Player | None: Player…** (1 connections) — `server/persistence/repositories/player_repository.py`
- **Unit tests for retry utilities. Tests the retry decorator and retry logic.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() with async function succeeds on first attempt.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test is_transient_error() identifies transient errors.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() with async function retries on failure then succeeds.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test is_transient_error() returns False for non-transient errors.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **DatabaseError wrapping asyncpg closed-connection must still retry (e2e…** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **__cause__ ConnectionDoesNotExistError makes the outer wrapper transient.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() succeeds on first attempt.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() retries on failure then succeeds.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Decorator to retry a function with exponential backoff on transient errors.…** (1 connections) — `server/utils/retry.py`

## Relationships

- [retry.py](retry.py.md) (8 shared connections)
- [row_to_player](row_to_player.md) (5 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [_StubPlayerRepo](_StubPlayerRepo.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [get_session_maker](get_session_maker.md) (1 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_repository.py`
- `server/tests/unit/utils/test_retry.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 50 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*