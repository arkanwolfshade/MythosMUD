# behavior engine npc

> 139 nodes

## Key Concepts

- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **test_behavior_engine.py** (54 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Any** (12 connections)
- **behavior_engine.py** (7 connections) — `server/npc/behavior_engine.py`
- **._try_evaluators()** (7 connections) — `server/npc/behavior_engine.py`
- **.evaluate_condition()** (6 connections) — `server/npc/behavior_engine.py`
- **.get_applicable_rules()** (5 connections) — `server/npc/behavior_engine.py`
- **.execute_applicable_rules()** (5 connections) — `server/npc/behavior_engine.py`
- **._evaluate_equality()** (4 connections) — `server/npc/behavior_engine.py`
- **._evaluate_inequality()** (4 connections) — `server/npc/behavior_engine.py`
- **._evaluate_numeric_comparison()** (4 connections) — `server/npc/behavior_engine.py`
- **._evaluate_boolean_condition()** (4 connections) — `server/npc/behavior_engine.py`
- **.execute_action()** (4 connections) — `server/npc/behavior_engine.py`
- **.add_rule()** (3 connections) — `server/npc/behavior_engine.py`
- **.get_rules()** (3 connections) — `server/npc/behavior_engine.py`
- **.register_action_handler()** (3 connections) — `server/npc/behavior_engine.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **test_behavior_engine_init()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_add_rule_success()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_add_rule_missing_fields()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_add_rule_replaces_existing()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_add_rule_handles_exception()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_remove_rule_success()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_remove_rule_not_found()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_remove_rule_handles_exception()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- *... and 114 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (1 shared connections)

## Source Files

- `server/npc/behavior_engine.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_behavior_engine.py`

## Audit Trail

- EXTRACTED: 426 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*