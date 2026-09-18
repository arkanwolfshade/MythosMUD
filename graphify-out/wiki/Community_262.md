# Community 262

> 59 nodes

## Key Concepts

- **disconnect_grace_period.py** (35 connections) — `server/realtime/disconnect_grace_period.py`
- **start_grace_period()** (21 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (18 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **is_player_in_grace_period()** (17 connections) — `server/realtime/disconnect_grace_period.py`
- **cancel_grace_period()** (15 connections) — `server/realtime/disconnect_grace_period.py`
- **capture_grace_snapshot()** (11 connections) — `server/realtime/disconnect_catchup.py`
- **disconnect_catchup.py** (10 connections) — `server/realtime/disconnect_catchup.py`
- **CatchupManager** (9 connections) — `server/realtime/disconnect_catchup.py`
- **CatchupPlayer** (9 connections) — `server/realtime/disconnect_catchup.py`
- **_cleanup_player_references()** (9 connections) — `server/realtime/player_disconnect_handlers.py`
- **asyncio** (9 connections)
- **_dp_snapshot()** (5 connections) — `server/realtime/disconnect_catchup.py`
- **test_start_grace_period_reconnection_cancels()** (5 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **UUID** (5 connections)
- **_PlayerLookupManager** (4 connections) — `server/realtime/disconnect_grace_period.py`
- **_grace_period_seconds()** (4 connections) — `server/realtime/disconnect_grace_period.py`
- **test_cancel_grace_period_cancels_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_errors_gracefully()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_already_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_creates_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_timer_expires()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **._get_player()** (3 connections) — `server/realtime/disconnect_grace_period.py`
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- *... and 34 more nodes in this community*

## Relationships

- [Community 607](Community_607.md) (13 shared connections)
- [Community 187](Community_187.md) (13 shared connections)
- [Community 389](Community_389.md) (7 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (7 shared connections)
- [Community 326](Community_326.md) (6 shared connections)
- [Community 78](Community_78.md) (3 shared connections)
- [Community 435](Community_435.md) (3 shared connections)
- [Community 229](Community_229.md) (3 shared connections)
- [Community 139](Community_139.md) (2 shared connections)
- [Community 673](Community_673.md) (2 shared connections)
- [Community 58](Community_58.md) (2 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_catchup.py`
- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 160 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*