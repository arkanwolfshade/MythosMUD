# BehaviorEngine

> 28 nodes

## Key Concepts

- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **test_add_rule_handles_exception()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_equality_false()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_equality_string()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_inequality_true()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_less_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_execute_applicable_rules_handles_exception()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_execute_applicable_rules_no_matching()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_register_action_handler_overwrites()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_remove_rule_handles_exception()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_remove_rule_not_found()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.__init__()** (2 connections) — `server/npc/behavior_engine.py`
- **.remove_rule()** (2 connections) — `server/npc/behavior_engine.py`
- **Deterministic behavior engine for NPCs. This engine evaluates rules based on…** (1 connections) — `server/npc/behavior_engine.py`
- **Initialize the behavior engine.** (1 connections) — `server/npc/behavior_engine.py`
- **Remove a behavior rule from the engine. Args: rule_name: Name of the rule to…** (1 connections) — `server/npc/behavior_engine.py`
- **Get the behavior engine for this NPC.** (1 connections) — `server/npc/npc_base.py`
- **Test _evaluate_equality() returns False for non-matching condition.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test _evaluate_equality() handles string values.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test _evaluate_inequality() returns True for non-matching condition.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test _evaluate_numeric_comparison() handles <= operator.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test execute_applicable_rules() returns True when no rules match.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test execute_applicable_rules() handles exceptions.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test register_action_handler() overwrites existing handler.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- *... and 3 more nodes in this community*

## Relationships

- [test_behavior_engine.py](test_behavior_engine.py.md) (27 shared connections)
- [Any](Any.md) (12 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [test_add_rule_missing_fields](test_add_rule_missing_fields.md) (1 shared connections)
- [test_add_rule_success](test_add_rule_success.md) (1 shared connections)
- [test_behavior_engine_init](test_behavior_engine_init.md) (1 shared connections)
- [test_evaluate_boolean_condition_true](test_evaluate_boolean_condition_true.md) (1 shared connections)
- [test_evaluate_boolean_condition_variable](test_evaluate_boolean_condition_variable.md) (1 shared connections)
- [test_evaluate_boolean_condition_variable_false](test_evaluate_boolean_condition_variable_false.md) (1 shared connections)
- [test_evaluate_condition_equality](test_evaluate_condition_equality.md) (1 shared connections)
- [test_evaluate_condition_greater_equal](test_evaluate_condition_greater_equal.md) (1 shared connections)

## Source Files

- `server/npc/behavior_engine.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_behavior_engine.py`

## Audit Trail

- EXTRACTED: 96 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*