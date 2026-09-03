# Test Behavior Engine

> 19 nodes

## Key Concepts

- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **Test evaluate_condition() handles > operator.** (4 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **test_evaluate_condition_greater_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_greater_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_less_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_less_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_equality_invalid_format()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_equality_true()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_execute_action_no_handler()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.__init__()** (2 connections) — `server/npc/behavior_engine.py`
- **.remove_rule()** (2 connections) — `server/npc/behavior_engine.py`
- **Deterministic behavior engine for NPCs. This engine evaluates rules based on…** (1 connections) — `server/npc/behavior_engine.py`
- **Initialize the behavior engine.** (1 connections) — `server/npc/behavior_engine.py`
- **Remove a behavior rule from the engine. Args: rule_name: Name of the rule to…** (1 connections) — `server/npc/behavior_engine.py`
- **Get the behavior engine for this NPC.** (1 connections) — `server/npc/npc_base.py`
- **Test _evaluate_equality() returns True for matching condition.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test _evaluate_equality() returns None for invalid format.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test execute_action() returns False when no handler.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`

## Relationships

- [Test Behavior Engine](Test_Behavior_Engine.md) (52 shared connections)
- [Behavior Engine](Behavior_Engine.md) (13 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (2 shared connections)
- [Npc Base](Npc_Base.md) (2 shared connections)
- [NPC Behavior & Spawning](NPC_Behavior_&_Spawning.md) (1 shared connections)

## Source Files

- `server/npc/behavior_engine.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_behavior_engine.py`

## Audit Trail

- EXTRACTED: 90 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*