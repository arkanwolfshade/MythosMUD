# BehaviorEngine

> 22 nodes

## Key Concepts

- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **test_add_rule_handles_exception()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_add_rule_replaces_existing()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_equality_true()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_non_numeric()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_get_applicable_rules_matching()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_get_applicable_rules_priority_order()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_get_rules()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.__init__()** (2 connections) — `server/npc/behavior_engine.py`
- **.remove_rule()** (2 connections) — `server/npc/behavior_engine.py`
- **Deterministic behavior engine for NPCs. This engine evaluates rules based on…** (1 connections) — `server/npc/behavior_engine.py`
- **Initialize the behavior engine.** (1 connections) — `server/npc/behavior_engine.py`
- **Remove a behavior rule from the engine. Args: rule_name: Name of the rule to…** (1 connections) — `server/npc/behavior_engine.py`
- **Get the behavior engine for this NPC.** (1 connections) — `server/npc/npc_base.py`
- **Test _evaluate_equality() returns True for matching condition.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test _evaluate_numeric_comparison() raises ValueError for non-numeric values.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test get_applicable_rules() returns matching rules.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test get_applicable_rules() returns rules in priority order.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test add_rule() replaces existing rule with same name.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test add_rule() handles exceptions gracefully.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test get_rules() returns copy of rules.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`

## Relationships

- [test_behavior_engine.py](test_behavior_engine.py.md) (21 shared connections)
- [Any](Any.md) (12 shared connections)
- [EventBus](EventBus.md) (5 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [test_add_rule_missing_fields](test_add_rule_missing_fields.md) (1 shared connections)
- [test_add_rule_success](test_add_rule_success.md) (1 shared connections)
- [test_behavior_engine_init](test_behavior_engine_init.md) (1 shared connections)
- [test_evaluate_boolean_condition_false](test_evaluate_boolean_condition_false.md) (1 shared connections)
- [test_evaluate_boolean_condition_variable_false](test_evaluate_boolean_condition_variable_false.md) (1 shared connections)
- [test_evaluate_condition_equality](test_evaluate_condition_equality.md) (1 shared connections)
- [test_evaluate_condition_greater_than](test_evaluate_condition_greater_than.md) (1 shared connections)
- [test_evaluate_condition_inequality](test_evaluate_condition_inequality.md) (1 shared connections)

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