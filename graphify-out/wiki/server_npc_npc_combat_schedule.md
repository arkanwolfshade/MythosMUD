# server npc npc combat schedule

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

- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (1 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (1 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)

## Source Files

- `server/npc/npc_combat_schedule.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*