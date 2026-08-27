# chatPanelRuntimeUtils.ts

> 92 nodes

## Key Concepts

- **test_player_presence_tracker.py** (39 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **player_presence_tracker.py** (35 connections) — `server/realtime/player_presence_tracker.py`
- **track_player_disconnected_impl()** (28 connections) — `server/realtime/player_presence_tracker.py`
- **asyncio** (17 connections)
- **track_player_connected_impl()** (13 connections) — `server/realtime/player_presence_tracker.py`
- **Any** (11 connections)
- **_build_player_info()** (10 connections) — `server/realtime/player_presence_tracker.py`
- **_acquire_disconnect_lock()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_room_id()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **_should_skip_disconnect()** (9 connections) — `server/realtime/player_presence_tracker.py`
- **test_player_presence_tracker_grace_period.py** (8 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **broadcast_connection_message_impl()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_disconnect_during_rest_is_intentional()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_get_instance_manager_from_manager()** (7 connections) — `server/realtime/player_presence_tracker.py`
- **_resolve_intentional_disconnect()** (6 connections) — `server/realtime/player_presence_tracker.py`
- **UUID** (6 connections)
- **_resolve_room_id_for_tutorial_reconnect()** (5 connections) — `server/realtime/player_presence_tracker.py`
- **test_broadcast_connection_message_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_error()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_impl_finally_cleanup()** (5 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- **test_track_player_disconnected_intentional_no_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_mid_rest_skips_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_removes_from_intentional_set()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_track_player_disconnected_unintentional_starts_grace_period()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`
- **test_acquire_disconnect_lock_already_disconnecting()** (4 connections) — `server/tests/unit/realtime/test_player_presence_tracker.py`
- *... and 67 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (9 shared connections)
- [ContainerComponent](ContainerComponent.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (7 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (5 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (4 shared connections)
- [utils/layout.ts](utils-layout.ts.md) (3 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (3 shared connections)
- [character-cleanup.ts](character-cleanup.ts.md) (3 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (1 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)
- [applies_to](applies_to.md) (1 shared connections)

## Source Files

- `server/realtime/player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker.py`
- `server/tests/unit/realtime/test_player_presence_tracker_grace_period.py`

## Audit Trail

- EXTRACTED: 212 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*