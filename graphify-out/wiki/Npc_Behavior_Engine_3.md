# Npc Behavior Engine

> 16 nodes · cohesion 0.17

## Key Concepts

- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **Test evaluate_condition() handles equality.** (7 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_add_rule_missing_fields()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_equality()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_greater_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_greater_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_handles_exception()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_inequality()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_less_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_less_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.__init__()** (2 connections) — `server/npc/behavior_engine.py`
- **.remove_rule()** (2 connections) — `server/npc/behavior_engine.py`
- **Deterministic behavior engine for NPCs.      This engine evaluates rules based o** (1 connections) — `server/npc/behavior_engine.py`
- **Initialize the behavior engine.** (1 connections) — `server/npc/behavior_engine.py`
- **Remove a behavior rule from the engine.          Args:             rule_name: Na** (1 connections) — `server/npc/behavior_engine.py`
- **Test add_rule() returns False when fields missing.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`

## Relationships

- [[Npc Behavior Engine]] (64 shared connections)
- [[NPC Movement Integration]] (2 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Aggressive Mob NPC]] (1 shared connections)
- [[Distributed Event Bus]] (1 shared connections)
- [[NPC Death Lifecycle]] (1 shared connections)

## Source Files

- `server/npc/behavior_engine.py`
- `server/tests/unit/npc/test_behavior_engine.py`

## Audit Trail

- EXTRACTED: 109 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
