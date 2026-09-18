# Community 530

> 32 nodes

## Key Concepts

- **test_lifecycle_respawn.py** (22 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **_make_manager()** (14 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **process_respawn_queue_impl()** (13 connections) — `server/npc/lifecycle_respawn.py`
- **_respawn_data()** (13 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **lifecycle_respawn.py** (12 connections) — `server/npc/lifecycle_respawn.py`
- **_attempt_respawn_impl()** (11 connections) — `server/npc/lifecycle_respawn.py`
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
- **test_cleanup_respawn_queue()** (2 connections) — `server/tests/unit/npc/test_lifecycle_respawn.py`
- **Process the respawn queue and spawn NPCs that are ready (delegates to…** (1 connections) — `server/npc/lifecycle_manager.py`
- **Respawn queue processing for NPC lifecycle. Extracted from lifecycle_manager to…** (1 connections) — `server/npc/lifecycle_respawn.py`
- *... and 7 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (4 shared connections)
- [Community 35](Community_35.md) (3 shared connections)
- [Community 91](Community_91.md) (3 shared connections)

## Source Files

- `server/npc/lifecycle_manager.py`
- `server/npc/lifecycle_respawn.py`
- `server/tests/unit/npc/test_lifecycle_respawn.py`

## Audit Trail

- EXTRACTED: 88 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*