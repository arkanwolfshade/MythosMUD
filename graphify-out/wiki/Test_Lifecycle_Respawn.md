# Test Lifecycle Respawn

> 32 nodes

## Key Concepts

- **test_lifecycle_respawn.py** (22 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **_make_manager()** (14 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **process_respawn_queue_impl()** (13 connections) — `server/npc/lifecycle_respawn.py`
- **_respawn_data()** (13 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **_attempt_respawn_impl()** (11 connections) — `server/npc/lifecycle_respawn.py`
- **lifecycle_respawn.py** (11 connections) — `server/npc/lifecycle_respawn.py`
- **_process_respawn_queue_entry()** (8 connections) — `server/npc/lifecycle_respawn.py`
- **_cleanup_respawn_queue()** (6 connections) — `server/npc/lifecycle_respawn.py`
- **test_attempt_respawn_exception_returns_false()** (5 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_attempt_respawn_routes_through_population_controller()** (5 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **test_attempt_respawn_can_spawn_false()** (4 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
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
- *... and 7 more nodes in this community*

## Relationships

- [Test Npc Utils](Test_Npc_Utils.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (2 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (1 shared connections)
- [Test Websocket Handler Validation Errors](Test_Websocket_Handler_Validation_Errors.md) (1 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_respawn.py`
- `server/tests/unit/npc/test_lifecycle_respawn.py`

## Audit Trail

- EXTRACTED: 87 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*