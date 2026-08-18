# server npc behavior engine behaviorengine

> 19 nodes

## Key Concepts

- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **Test _evaluate_numeric_comparison() handles >= operator.** (4 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **test_evaluate_inequality_not_inequality()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_inequality_true()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_greater_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_greater_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_less_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_less_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_execute_action_success()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.__init__()** (2 connections) — `server/npc/behavior_engine.py`
- **.remove_rule()** (2 connections) — `server/npc/behavior_engine.py`
- **Deterministic behavior engine for NPCs. This engine evaluates rules based on…** (1 connections) — `server/npc/behavior_engine.py`
- **Initialize the behavior engine.** (1 connections) — `server/npc/behavior_engine.py`
- **Remove a behavior rule from the engine. Args: rule_name: Name of the rule to…** (1 connections) — `server/npc/behavior_engine.py`
- **Get the behavior engine for this NPC.** (1 connections) — `server/npc/npc_base.py`
- **Test _evaluate_inequality() returns True for non-matching condition.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test _evaluate_inequality() returns None for non-inequality condition.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test execute_action() successfully executes action.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`

## Relationships

- [server tests unit npc test](server_tests_unit_npc_test.md) (52 shared connections)
- [server npc behavior engine behaviorengine](server_npc_behavior_engine_behaviorengine.md) (12 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server npc npc base npcbase](server_npc_npc_base_npcbase.md) (2 shared connections)

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