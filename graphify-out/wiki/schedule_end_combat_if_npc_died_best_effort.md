# schedule_end_combat_if_npc_died_best_effort

> 21 nodes

## Key Concepts

- **schedule_end_combat_if_npc_died_best_effort()** (8 connections) — `server/npc/npc_combat_schedule.py`
- **npc_combat_schedule.py** (7 connections) — `server/npc/npc_combat_schedule.py`
- **._handle_npc_death()** (5 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **test_npc_combat_schedule.py** (5 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **._publish_damage_event()** (4 connections) — `server/npc/npc_base.py`
- **._schedule_end_combat_if_npc_died()** (4 connections) — `server/npc/npc_base.py`
- **test_schedule_end_combat_if_npc_died_no_running_loop()** (4 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **test_schedule_end_combat_if_npc_died_no_service()** (4 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **._update_determination_points()** (3 connections) — `server/npc/npc_base.py`
- **patch** (2 connections)
- **Update determination points after taking damage; return new DP.** (1 connections) — `server/npc/npc_base.py`
- **Publish damage event to event bus.** (1 connections) — `server/npc/npc_base.py`
- **Handle NPC death after taking fatal damage.** (1 connections) — `server/npc/npc_base.py`
- **Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns…** (1 connections) — `server/npc/npc_base.py`
- **Take damage and update determination points (DP).** (1 connections) — `server/npc/npc_base.py`
- **Best-effort async scheduling for NPC combat cleanup (extracted to limit…** (1 connections) — `server/npc/npc_combat_schedule.py`
- **Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns…** (1 connections) — `server/npc/npc_combat_schedule.py`
- **Unit tests for best-effort NPC combat cleanup scheduling.** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **When combat service is missing, scheduling is a no-op.** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`
- **Without a running asyncio loop, scheduling fails quietly (RuntimeError path).** (1 connections) — `server/tests/unit/npc/test_npc_combat_schedule.py`

## Relationships

- [EventBus](EventBus.md) (7 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_combat_schedule.py`
- `server/tests/unit/npc/test_npc_combat_schedule.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*