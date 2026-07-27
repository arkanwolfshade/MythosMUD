# Npc Combat Schedule

> 8 nodes · cohesion 0.32

## Key Concepts

- **schedule_end_combat_if_npc_died_best_effort()** (8 connections) — `server/npc/npc_combat_schedule.py`
- **test_npc_combat_schedule.py** (4 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **test_schedule_end_combat_if_npc_died_no_running_loop()** (3 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **test_schedule_end_combat_if_npc_died_no_service()** (3 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns (be** (1 connections) — `server/npc/npc_combat_schedule.py`
- **Unit tests for best-effort NPC combat cleanup scheduling.** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **When combat service is missing, scheduling is a no-op.** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **Without a running asyncio loop, scheduling fails quietly (RuntimeError path).** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`

## Relationships

- [[Distributed Event Bus]] (1 shared connections)
- [[NPC Death Lifecycle]] (1 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Combat Service Bundle]] (1 shared connections)

## Source Files

- `server/npc/npc_combat_schedule.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
