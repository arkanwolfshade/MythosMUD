# Test Npc Combat Schedule

> 9 nodes

## Key Concepts

- **schedule_end_combat_if_npc_died_best_effort()** (8 connections) — `server/npc/npc_combat_schedule.py`
- **test_npc_combat_schedule.py** (5 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **test_schedule_end_combat_if_npc_died_no_running_loop()** (4 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **test_schedule_end_combat_if_npc_died_no_service()** (4 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **patch** (2 connections)
- **Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns…** (1 connections) — `server/npc/npc_combat_schedule.py`
- **Unit tests for best-effort NPC combat cleanup scheduling.** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **When combat service is missing, scheduling is a no-op.** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **Without a running asyncio loop, scheduling fails quietly (RuntimeError path).** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`

## Relationships

- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Npc Base](Npc_Base.md) (1 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (1 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (1 shared connections)

## Source Files

- `server/npc/npc_combat_schedule.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*