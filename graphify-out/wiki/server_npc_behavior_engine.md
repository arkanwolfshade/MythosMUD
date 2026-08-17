# server npc behavior engine

> 15 nodes

## Key Concepts

- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **behavior_engine.py** (7 connections) — `server/npc/behavior_engine.py`
- **Test evaluate_condition() handles > operator.** (4 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **test_evaluate_condition_greater_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_greater_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_less_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_less_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.__init__()** (2 connections) — `server/npc/behavior_engine.py`
- **.remove_rule()** (2 connections) — `server/npc/behavior_engine.py`
- **Behavior engine for NPCs. This module provides the deterministic behavior…** (1 connections) — `server/npc/behavior_engine.py`
- **Deterministic behavior engine for NPCs. This engine evaluates rules based on…** (1 connections) — `server/npc/behavior_engine.py`
- **Initialize the behavior engine.** (1 connections) — `server/npc/behavior_engine.py`
- **Remove a behavior rule from the engine. Args: rule_name: Name of the rule to…** (1 connections) — `server/npc/behavior_engine.py`
- **Get the behavior engine for this NPC.** (1 connections) — `server/npc/npc_base.py`

## Relationships

- [server tests unit npc test](server_tests_unit_npc_test.md) (53 shared connections)
- [server npc behavior engine behaviorengine](server_npc_behavior_engine_behaviorengine.md) (12 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (4 shared connections)
- [server events event bus](server_events_event_bus.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server npc npc base npcbase](server_npc_npc_base_npcbase.md) (1 shared connections)

## Source Files

- `server/npc/behavior_engine.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_behavior_engine.py`

## Audit Trail

- EXTRACTED: 39 (43%)
- INFERRED: 52 (57%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*