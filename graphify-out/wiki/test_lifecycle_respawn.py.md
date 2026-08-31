# test_lifecycle_respawn.py

> 29 nodes

## Key Concepts

- **test_lifecycle_respawn.py** (21 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **process_respawn_queue_impl()** (13 connections) — `server/npc/lifecycle_respawn.py`
- **_make_manager()** (12 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **_respawn_data()** (12 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **lifecycle_respawn.py** (10 connections) — `server/npc/lifecycle_respawn.py`
- **_attempt_respawn_impl()** (9 connections) — `server/npc/lifecycle_respawn.py`
- **_process_respawn_queue_entry()** (8 connections) — `server/npc/lifecycle_respawn.py`
- **_cleanup_respawn_queue()** (6 connections) — `server/npc/lifecycle_respawn.py`
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
- **test_cleanup_respawn_queue()** (2 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **Process the respawn queue and spawn NPCs that are ready (delegates to…** (1 connections) — `server/npc/lifecycle_manager.py`
- **Respawn queue processing for NPC lifecycle. Extracted from lifecycle_manager to…** (1 connections) — `server/npc/lifecycle_respawn.py`
- **Process the respawn queue and spawn NPCs that are ready. Args: manager:…** (1 connections) — `server/npc/lifecycle_respawn.py`
- *... and 4 more nodes in this community*

## Relationships

- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_respawn.py`
- `server/tests/unit/npc/test_lifecycle_respawn.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*