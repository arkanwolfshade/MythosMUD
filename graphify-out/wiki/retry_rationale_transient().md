# retry rationale transient()

> 65 nodes

## Key Concepts

- **_StubPlayerRepo** (18 connections) — `server/tests/unit/persistence/test_protocols.py`
- **retry.py** (18 connections) — `server/utils/retry.py`
- **test_player_repository_protocol_stub()** (17 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_retry.py** (13 connections) — `server/tests/unit/utils/test_retry.py`
- **is_transient_error()** (13 connections) — `server/utils/retry.py`
- **retry_with_backoff()** (11 connections) — `server/utils/retry.py`
- **Exception** (9 connections)
- **UUID** (6 connections)
- **.get_player_by_id()** (4 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_is_transient_error_wrapped_connection_closed()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_cause_chain_connection_closed()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_retries_wrapped_connection_closed_then_succeeds()** (4 connections) — `server/tests/unit/utils/test_retry.py`
- **_is_psycopg2_transient()** (4 connections) — `server/utils/retry.py`
- **_is_wrapped_transient_message()** (4 connections) — `server/utils/retry.py`
- **_iter_exception_chain()** (4 connections) — `server/utils/retry.py`
- **_should_retry_error()** (4 connections) — `server/utils/retry.py`
- **_create_async_wrapper()** (4 connections) — `server/utils/retry.py`
- **_create_sync_wrapper()** (4 connections) — `server/utils/retry.py`
- **.get_players_batch()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.soft_delete_player()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.delete_player()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.update_player_last_active()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_is_transient_error_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_is_transient_error_non_transient()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- **test_retry_with_backoff_success()** (3 connections) — `server/tests/unit/utils/test_retry.py`
- *... and 40 more nodes in this community*

## Relationships

- [persistence protocols rationale](persistence_protocols_rationale.md) (6 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)

## Source Files

- `server/tests/unit/persistence/test_protocols.py`
- `server/tests/unit/utils/test_retry.py`
- `server/utils/retry.py`

## Audit Trail

- EXTRACTED: 220 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*