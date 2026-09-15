# start_grace_period

> 39 nodes

## Key Concepts

- **start_grace_period()** (23 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (18 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **cancel_grace_period()** (15 connections) — `server/realtime/disconnect_grace_period.py`
- **asyncio** (9 connections)
- **test_start_grace_period_reconnection_cancels()** (5 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **UUID** (5 connections)
- **_PlayerLookupManager** (4 connections) — `server/realtime/disconnect_grace_period.py`
- **test_cancel_grace_period_cancels_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_errors_gracefully()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_already_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_creates_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_timer_expires()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **._get_player()** (3 connections) — `server/realtime/disconnect_grace_period.py`
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_false()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Any** (3 connections)
- **Player** (1 connections)
- **Protocol** (1 connections)
- **fixture** (1 connections)
- **Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **The one typed slice of ConnectionManager needed to snapshot DP at grace start.** (1 connections) — `server/realtime/disconnect_grace_period.py`
- *... and 14 more nodes in this community*

## Relationships

- [player_presence_tracker.py](player_presence_tracker.py.md) (14 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (8 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (2 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (2 shared connections)
- [extract_player_name](extract_player_name.md) (1 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 85 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*