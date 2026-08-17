# f

> 11 nodes

## Key Concepts

- **retry_with_backoff()** (14 connections) — `server/utils/retry.py`
- **test_retry_retries_wrapped_connection_closed_then_succeeds()** (5 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_failure_then_success()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_async_success()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **.get_player_by_id()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **asyncio** (3 connections)
- **F** (1 connections)
- **Test retry_with_backoff() with async function succeeds on first attempt.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Test retry_with_backoff() with async function retries on failure then succeeds.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Retry decorator must not treat wrapped closed-connection as final on attempt 1.** (1 connections) — `server/tests/unit/utils/test_retry.py`
- **Decorator to retry a function with exponential backoff on transient errors.…** (1 connections) — `server/utils/retry.py`

## Relationships

- [server tests unit utils test](server_tests_unit_utils_test.md) (6 shared connections)
- [server models player playerchannelpreferences](server_models_player_playerchannelpreferences.md) (3 shared connections)
- [server tests unit persistence test](server_tests_unit_persistence_test.md) (2 shared connections)
- [server utils retry](server_utils_retry.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_protocols.py`
- `server/tests/unit/utils/test_retry.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 25 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*