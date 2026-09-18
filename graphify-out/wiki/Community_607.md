# Community 607

> 28 nodes

## Key Concepts

- **test_disconnect_catchup.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **build_catchup_message()** (12 connections) — `server/realtime/disconnect_catchup.py`
- **_manager()** (10 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **_player()** (9 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **_FakePlayer** (7 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_none_without_snapshot()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_reports_damage_taken()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_reports_death_distinctly()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_silent_on_dp_gain()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_silent_on_no_change()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_capture_grace_snapshot_skips_unreadable_stats()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_capture_grace_snapshot_stores_dp()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **.get_stats()** (2 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **.is_dead()** (2 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **UUID** (2 connections)
- **.__init__()** (1 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **Build a reconnect catch-up summary, or None if there is nothing worth telling…** (1 connections) — `server/realtime/disconnect_catchup.py`
- **Unit tests for the disconnect-grace reconnect catch-up summary (`#297`). Covers…** (1 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **No snapshot on record (e.g. capture failed) means no message, not an error.** (1 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **A minimal, fully-typed `CatchupPlayer` double -- avoids MagicMock's inherently…** (1 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **Return the stats dict set at construction.** (1 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **Return the death flag set at construction.** (1 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **capture_grace_snapshot() stores current/max DP keyed by player_id.** (1 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **A player whose get_stats() doesn't return usable DP fields is not snapshotted.** (1 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **A DP drop between snapshot and reconnect produces a damage summary.** (1 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- *... and 3 more nodes in this community*

## Relationships

- [Community 262](Community_262.md) (13 shared connections)

## Source Files

- `server/realtime/disconnect_catchup.py`
- `server/tests/unit/realtime/test_disconnect_catchup.py`

## Audit Trail

- EXTRACTED: 59 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*