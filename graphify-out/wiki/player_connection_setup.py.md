# player_connection_setup.py

> 84 nodes · cohesion 0.04

## Key Concepts

- **disconnect_grace_period.py** (37 connections) — `server/realtime/disconnect_grace_period.py`
- **start_grace_period()** (25 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (18 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_disconnect_catchup.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **cancel_grace_period()** (15 connections) — `server/realtime/disconnect_grace_period.py`
- **build_catchup_message()** (14 connections) — `server/realtime/disconnect_catchup.py`
- **_cleanup_player_references()** (14 connections) — `server/realtime/player_disconnect_handlers.py`
- **capture_grace_snapshot()** (11 connections) — `server/realtime/disconnect_catchup.py`
- **CatchupManager** (11 connections) — `server/realtime/disconnect_catchup.py`
- **CatchupPlayer** (11 connections) — `server/realtime/disconnect_catchup.py`
- **disconnect_catchup.py** (10 connections) — `server/realtime/disconnect_catchup.py`
- **_manager()** (10 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **InstanceFlushOwner** (9 connections) — `server/realtime/player_disconnect_handlers.py`
- **_player()** (9 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **asyncio** (9 connections)
- **_FakePlayer** (7 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **_dp_snapshot()** (5 connections) — `server/realtime/disconnect_catchup.py`
- **UUID** (5 connections)
- **test_build_catchup_message_none_without_snapshot()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_reports_damage_taken()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_reports_death_distinctly()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_silent_on_dp_gain()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_build_catchup_message_silent_on_no_change()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_capture_grace_snapshot_skips_unreadable_stats()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- **test_capture_grace_snapshot_stores_dp()** (5 connections) — `server/tests/unit/realtime/test_disconnect_catchup.py`
- *... and 59 more nodes in this community*

## Relationships

- [test_npc_event_handlers.py](test_npc_event_handlers.py.md) (21 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (16 shared connections)
- [test_look_npc_helpers.py](test_look_npc_helpers.py.md) (10 shared connections)
- [ChatLogger](ChatLogger.md) (4 shared connections)
- [test_npc_utils.py](test_npc_utils.py.md) (3 shared connections)
- [test_disconnect_catchup.py](test_disconnect_catchup.py.md) (3 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (1 shared connections)
- [mapUtils.ts](mapUtils.ts.md) (1 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (1 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_catchup.py`
- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_disconnect_catchup.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 214 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*