# test_login_grace_period.py

> 40 nodes

## Key Concepts

- **test_login_grace_period.py** (26 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (10 connections)
- **test_cancel_login_grace_period()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_cancel_login_grace_period_effect_based_clears_tracking()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_cancel_login_grace_period_not_active()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_grace_period_task_cancellation_cleanup()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_multiple_players_grace_periods()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_start_login_grace_period()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_start_login_grace_period_already_active()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_start_login_grace_period_effect_based_adds_effect_and_sets_in_memory()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_start_login_grace_period_expires()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_get_login_grace_period_remaining_active()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_get_login_grace_period_remaining_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_get_login_grace_period_remaining_no_start_time()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_get_login_grace_period_remaining_not_active()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_is_player_in_login_grace_period_active()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_is_player_in_login_grace_period_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_is_player_in_login_grace_period_not_active()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **fixture** (1 connections)
- **Cancel login grace period for a player (if needed). For effect-based grace…** (1 connections) — `server/realtime/login_grace_period.py`
- **Unit tests for login grace period functionality. Tests the core login grace…** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test cancelling grace period when not active (should not error).** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test checking if player is in grace period when active.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- *... and 15 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (24 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*