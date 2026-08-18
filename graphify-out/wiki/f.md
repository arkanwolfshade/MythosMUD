# f

> 73 nodes

## Key Concepts

- **retry.py** (19 connections) — `server/utils/retry.py`
- **_StubPlayerRepo** (16 connections) — `server/tests/unit/persistence/test_protocols.py`
- **retry_with_backoff()** (14 connections) — `server/utils/retry.py`
- **test_retry.py** (14 connections) — `server/tests/unit/utils/test_retry.py`
- **is_transient_error()** (13 connections) — `server/utils/retry.py`
- **test_protocols.py** (11 connections) — `server/tests/unit/persistence/test_protocols.py`
- **Exception** (9 connections)
- **UUID** (6 connections)
- **test_player_repository_protocol_stub()** (5 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_retry_retries_wrapped_connection_closed_then_succeeds()** (5 connections) — `server/tests/unit/utils/test_retry.py`
- **_StubRoomRepo** (4 connections) — `server/tests/unit/persistence/test_protocols.py`
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
- **.get_player_by_id()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_room_repository_protocol_stub()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_is_transient_error_non_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- *... and 48 more nodes in this community*

## Relationships

- [server async persistence](server_async_persistence.md) (7 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [object](object.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_protocols.py`
- `server/tests/unit/utils/test_retry.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 121 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*