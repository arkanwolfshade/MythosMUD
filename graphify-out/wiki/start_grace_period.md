# start_grace_period

> 34 nodes

## Key Concepts

- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (19 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **cancel_grace_period()** (14 connections) — `server/realtime/disconnect_grace_period.py`
- **asyncio** (9 connections)
- **test_start_grace_period_reconnection_cancels()** (5 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_cancels_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_errors_gracefully()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_already_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_creates_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_timer_expires()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **UUID** (4 connections)
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_false()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Any** (3 connections)
- **fixture** (1 connections)
- **Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Start a grace period for a disconnected player. During the grace period, the…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Unit tests for disconnect grace period management. Tests the grace period…** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Test grace period is cancelled when player reconnects.** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Test cancel_grace_period() does nothing if player not in grace period.** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Test cancel_grace_period() cancels the grace period task.** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- *... and 9 more nodes in this community*

## Relationships

- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (8 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (3 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (3 shared connections)
- [establish_websocket_connection](establish_websocket_connection.md) (1 shared connections)
- [handle_new_connection_setup](handle_new_connection_setup.md) (1 shared connections)
- [models/player.py](models-player.py.md) (1 shared connections)
- [extract_player_name](extract_player_name.md) (1 shared connections)
- [PlayerOccupantProcessor](PlayerOccupantProcessor.md) (1 shared connections)
- [test_look_player.py](test_look_player.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*