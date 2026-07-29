# BehaviorEngine

> 20 nodes

## Key Concepts

- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **Test _evaluate_numeric_comparison() handles > operator.** (4 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **test_evaluate_equality_boolean_true()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_equality_boolean_false()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_greater_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_less_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_greater_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_less_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_execute_applicable_rules_no_matching()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_execute_applicable_rules_executes_highest_priority()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.__init__()** (2 connections) — `server/npc/behavior_engine.py`
- **.remove_rule()** (2 connections) — `server/npc/behavior_engine.py`
- **Test _evaluate_equality() handles boolean true.** (2 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Deterministic behavior engine for NPCs.      This engine evaluates rules based o** (1 connections) — `server/npc/behavior_engine.py`
- **Initialize the behavior engine.** (1 connections) — `server/npc/behavior_engine.py`
- **Remove a behavior rule from the engine.          Args:             rule_name: Na** (1 connections) — `server/npc/behavior_engine.py`
- **Get the behavior engine for this NPC.** (1 connections) — `server/npc/npc_base.py`
- **Test execute_applicable_rules() returns True when no rules match.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test execute_applicable_rules() executes highest priority rule.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`

## Relationships

- [test behavior engine](test_behavior_engine.md) (22 shared connections)
- [.add rule()](add_rule%28%29.md) (12 shared connections)
- [.initialize()](initialize%28%29.md) (4 shared connections)
- [Test get applicable rules() returns](Test_get_applicable_rules%28%29_returns.md) (3 shared connections)
- [Test evaluate boolean condition() handles](Test_evaluate_boolean_condition%28%29_handles.md) (2 shared connections)
- [behavior engine](behavior_engine.md) (1 shared connections)
- [Return stats\[key\] as int, or](Return_stats%5Bkey%5D_as_int%2C_or.md) (1 shared connections)
- [Test add rule() handles exceptions](Test_add_rule%28%29_handles_exceptions.md) (1 shared connections)
- [Test add rule() returns False](Test_add_rule%28%29_returns_False.md) (1 shared connections)
- [Test add rule() replaces existing](Test_add_rule%28%29_replaces_existing.md) (1 shared connections)
- [Test add rule() successfully adds](Test_add_rule%28%29_successfully_adds.md) (1 shared connections)
- [Test BehaviorEngine initialization.](Test_BehaviorEngine_initialization.md) (1 shared connections)

## Source Files

- `server/npc/behavior_engine.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_behavior_engine.py`

## Audit Trail

- EXTRACTED: 115 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*