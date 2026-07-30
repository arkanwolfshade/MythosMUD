# Test get mortally wounded players()

> 8 nodes

## Key Concepts

- **test_player_presence_tracker_grace_period.py** (6 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_intentional_no_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_unintentional_starts_grace_period()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_removes_from_intentional_set()** (3 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **Unit tests for player presence tracker grace period integration.  Tests the inte** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **Test intentional disconnect does NOT start grace period.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **Test unintentional disconnect starts grace period.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **Test intentional disconnect is removed from intentional_disconnects set.** (1 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Relationships

- [player presence tracker](player_presence_tracker.md) (4 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*