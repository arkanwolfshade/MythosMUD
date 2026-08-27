# properties

> 18 nodes

## Key Concepts

- **_StubPlayerRepo** (16 connections) — `server/tests/unit/persistence/test_protocols.py`
- **UUID** (6 connections)
- **test_retry_retries_wrapped_connection_closed_then_succeeds()** (5 connections) — `server/tests/unit/utils/test_retry.py`
- **.get_player_by_id()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.delete_player()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_players_batch()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.soft_delete_player()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.update_player_last_active()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_active_players_by_user_id()** (1 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_player_by_name()** (1 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_player_by_user_id()** (1 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_players_by_user_id()** (1 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_players_in_room()** (1 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.list_players()** (1 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.save_player()** (1 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.save_players()** (1 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.validate_and_fix_player_room()** (1 connections) — `server/tests/unit/persistence/test_protocols.py`
- **Retry decorator must not treat wrapped closed-connection as final on attempt 1.** (1 connections) — `server/tests/unit/utils/test_retry.py`

## Relationships

- [test_realtime_bundle_nats.py](test_realtime_bundle_nats.py.md) (3 shared connections)
- [Execution Steps](Execution_Steps.md) (3 shared connections)

## Source Files

- `server/tests/unit/persistence/test_protocols.py`
- `server/tests/unit/utils/test_retry.py`

## Audit Trail

- EXTRACTED: 26 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*