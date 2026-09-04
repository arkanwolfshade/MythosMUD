# Test Disconnect Catchup

> 40 nodes

## Key Concepts

- **test_disconnect_catchup.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **build_catchup_message()** (14 connections) — `server/realtime/disconnect_catchup.py`
- **CatchupManager** (11 connections) — `server/realtime/disconnect_catchup.py`
- **CatchupPlayer** (11 connections) — `server/realtime/disconnect_catchup.py`
- **capture_grace_snapshot()** (11 connections) — `server/realtime/disconnect_catchup.py`
- **_manager()** (10 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **disconnect_catchup.py** (10 connections) — `server/realtime/disconnect_catchup.py`
- **_player()** (9 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **_FakePlayer** (7 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **_dp_snapshot()** (5 connections) — `server/realtime/disconnect_catchup.py`
- **test_build_catchup_message_none_without_snapshot()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_reports_damage_taken()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_reports_death_distinctly()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_silent_on_dp_gain()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_silent_on_no_change()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_capture_grace_snapshot_skips_unreadable_stats()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_capture_grace_snapshot_stores_dp()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **UUID** (3 connections)
- **.get_stats()** (2 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **.is_dead()** (2 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **Protocol** (2 connections)
- **UUID** (2 connections)
- **.get_stats()** (1 connections) — `server/realtime/disconnect_catchup.py`
- **.is_dead()** (1 connections) — `server/realtime/disconnect_catchup.py`
- **.__init__()** (1 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- *... and 15 more nodes in this community*

## Relationships

- [Test Player Presence Tracker](Test_Player_Presence_Tracker.md) (7 shared connections)
- [Test Rest And Grace Period](Test_Rest_And_Grace_Period.md) (6 shared connections)

## Source Files

- `server/realtime/disconnect_catchup.py`
- `server/tests/unit/realtime/test_disconnect_catchup.py`

## Audit Trail

- EXTRACTED: 86 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*