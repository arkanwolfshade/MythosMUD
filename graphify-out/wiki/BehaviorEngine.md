# BehaviorEngine

> 16 nodes

## Key Concepts

- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **test_evaluate_equality_boolean_false()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_invalid()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_less_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_remove_rule_handles_exception()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.__init__()** (2 connections) — `server/npc/behavior_engine.py`
- **.remove_rule()** (2 connections) — `server/npc/behavior_engine.py`
- **Deterministic behavior engine for NPCs. This engine evaluates rules based on…** (1 connections) — `server/npc/behavior_engine.py`
- **Initialize the behavior engine.** (1 connections) — `server/npc/behavior_engine.py`
- **Remove a behavior rule from the engine. Args: rule_name: Name of the rule to…** (1 connections) — `server/npc/behavior_engine.py`
- **Get the behavior engine for this NPC.** (1 connections) — `server/npc/npc_base.py`
- **Test _evaluate_equality() handles boolean false.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test _evaluate_numeric_comparison() handles < operator.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test _evaluate_numeric_comparison() returns None for invalid format.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test remove_rule() handles exceptions gracefully.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`

## Relationships

- [test_behavior_engine.py](test_behavior_engine.py.md) (19 shared connections)
- [Any](Any.md) (12 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [register_default_reactions_for_npc](register_default_reactions_for_npc.md) (1 shared connections)
- [test_add_rule_missing_fields](test_add_rule_missing_fields.md) (1 shared connections)
- [test_add_rule_success](test_add_rule_success.md) (1 shared connections)
- [test_behavior_engine_init](test_behavior_engine_init.md) (1 shared connections)
- [test_evaluate_boolean_condition_false](test_evaluate_boolean_condition_false.md) (1 shared connections)
- [test_evaluate_boolean_condition_variable_false](test_evaluate_boolean_condition_variable_false.md) (1 shared connections)
- [test_evaluate_condition_equality](test_evaluate_condition_equality.md) (1 shared connections)
- [test_evaluate_condition_greater_than](test_evaluate_condition_greater_than.md) (1 shared connections)
- [test_evaluate_condition_handles_exception](test_evaluate_condition_handles_exception.md) (1 shared connections)

## Source Files

- `server/npc/behavior_engine.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_behavior_engine.py`

## Audit Trail

- EXTRACTED: 33 (39%)
- INFERRED: 52 (61%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*