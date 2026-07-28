# Server Npc (14)

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

- [Server Npc (13)](Server_Npc_%2813%29.md) (22 shared connections)
- [Server Npc (11)](Server_Npc_%2811%29.md) (12 shared connections)
- [Server Npc (3)](Server_Npc_%283%29.md) (3 shared connections)
- [Server Npc (19)](Server_Npc_%2819%29.md) (1 shared connections)
- [Server Npc](Server_Npc.md) (1 shared connections)
- [Server Events](Server_Events.md) (1 shared connections)
- [Server Npc (47)](Server_Npc_%2847%29.md) (1 shared connections)
- [Server Npc (35)](Server_Npc_%2835%29.md) (1 shared connections)
- [Server Npc (45)](Server_Npc_%2845%29.md) (1 shared connections)
- [Server Npc (28)](Server_Npc_%2828%29.md) (1 shared connections)
- [Server Npc (23)](Server_Npc_%2823%29.md) (1 shared connections)
- [Server Npc (43)](Server_Npc_%2843%29.md) (1 shared connections)

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