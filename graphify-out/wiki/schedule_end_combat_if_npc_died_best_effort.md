# schedule_end_combat_if_npc_died_best_effort

> 10 nodes · cohesion 0.27

## Key Concepts

- **schedule_end_combat_if_npc_died_best_effort()** (8 connections) — `server/npc/npc_combat_schedule.py`
- **npc_combat_schedule.py** (7 connections) — `server/npc/npc_combat_schedule.py`
- **test_npc_combat_schedule.py** (5 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **test_schedule_end_combat_if_npc_died_no_running_loop()** (3 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **test_schedule_end_combat_if_npc_died_no_service()** (3 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **Best-effort async scheduling for NPC combat cleanup (extracted to limit npc_base** (1 connections) — `server/npc/npc_combat_schedule.py`
- **Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns (be** (1 connections) — `server/npc/npc_combat_schedule.py`
- **Unit tests for best-effort NPC combat cleanup scheduling.** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **When combat service is missing, scheduling is a no-op.** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **Without a running asyncio loop, scheduling fails quietly (RuntimeError path).** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`

## Relationships

- [npc_base.py](npc_base.py.md) (2 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NPCBase](NPCBase.md) (1 shared connections)

## Source Files

- `server/npc/npc_combat_schedule.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*