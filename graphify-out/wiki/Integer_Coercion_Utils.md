# Integer Coercion Utils

> 34 nodes

## Key Concepts

- **test_login_grace_period.py** (24 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_start_login_grace_period()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_start_login_grace_period_already_active()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_start_login_grace_period_expires()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_cancel_login_grace_period_not_active()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_is_player_in_login_grace_period_active()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_is_player_in_login_grace_period_not_active()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_is_player_in_login_grace_period_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_get_login_grace_period_remaining_active()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_get_login_grace_period_remaining_not_active()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_get_login_grace_period_remaining_no_start_time()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_get_login_grace_period_remaining_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_multiple_players_grace_periods()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_grace_period_task_cancellation_cleanup()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_start_login_grace_period_effect_based_adds_effect_and_sets_in_memory()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_cancel_login_grace_period_effect_based_clears_tracking()** (3 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Unit tests for login grace period functionality.  Tests the core login grace per** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Create a mock ConnectionManager for testing.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test starting a login grace period for a player.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test starting grace period when already active (should not duplicate).** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test that grace period expires after duration.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test cancelling grace period when not active (should not error).** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test checking if player is in grace period when active.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test checking if player is in grace period when not active.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- *... and 9 more nodes in this community*

## Relationships

- [Player Respawn Events](Player_Respawn_Events.md) (21 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_login_grace_period.py`

## Audit Trail

- EXTRACTED: 88 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*