# MemoryThresholdMonitor

> 35 nodes

## Key Concepts

- **test_login_grace_period.py** (26 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **asyncio** (10 connections)
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
- **Test checking if player is in grace period when active.** (2 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **fixture** (1 connections)
- **Unit tests for login grace period functionality. Tests the core login grace…** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test cancelling grace period when not active (should not error).** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test checking grace period when manager lacks attribute.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test getting remaining time for active grace period.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **Test getting remaining time when not in grace period.** (1 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- *... and 10 more nodes in this community*

## Relationships

- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (22 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_login_grace_period.py`

## Audit Trail

- EXTRACTED: 67 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*