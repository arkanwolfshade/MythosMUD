# test_lifecycle_respawn.py

> 38 nodes

## Key Concepts

- **test_lifecycle_respawn.py** (22 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **_make_manager()** (14 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **process_respawn_queue_impl()** (13 connections) — `server/npc/lifecycle_respawn.py`
- **_respawn_data()** (13 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **lifecycle_respawn.py** (12 connections) — `server/npc/lifecycle_respawn.py`
- **_attempt_respawn_impl()** (11 connections) — `server/npc/lifecycle_respawn.py`
- **spawn_npc_via_population_controller()** (11 connections) — `server/npc/npc_utils.py`
- **_process_respawn_queue_entry()** (8 connections) — `server/npc/lifecycle_respawn.py`
- **_cleanup_respawn_queue()** (6 connections) — `server/npc/lifecycle_respawn.py`
- **test_attempt_respawn_routes_through_population_controller()** (5 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_attempt_respawn_can_spawn_false()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_attempt_respawn_exception_returns_false()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_attempt_respawn_migrates_lifecycle_record()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_attempt_respawn_same_npc_id_no_migration()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_process_entry_not_ready()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_process_entry_success_removes_entry()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_process_respawn_queue_failed_retry()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_process_respawn_queue_max_attempts_removes_entry()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_process_respawn_queue_multiple_entries()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_process_respawn_queue_not_ready()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_process_respawn_queue_success()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **Any** (4 connections)
- **.process_respawn_queue()** (3 connections) — `server/npc/lifecycle_manager.py`
- **test_spawn_npc_via_population_controller_falls_back_without_controller()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- **test_spawn_npc_via_population_controller_routes_through_controller()** (3 connections) — `server/tests/unit/npc/test_npc_utils.py`
- *... and 13 more nodes in this community*

## Relationships

- [test_npc_utils.py](test_npc_utils.py.md) (6 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [test_population_control.py](test_population_control.py.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_respawn.py`
- `server/npc/npc_utils.py`
- `server/tests/unit/npc/test_lifecycle_respawn.py`
- `server/tests/unit/npc/test_npc_utils.py`

## Audit Trail

- EXTRACTED: 100 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*