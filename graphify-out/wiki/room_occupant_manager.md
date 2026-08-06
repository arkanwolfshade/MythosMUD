# room occupant manager

> 22 nodes

## Key Concepts

- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **test_add_rule_replaces_existing()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_add_rule_handles_exception()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_get_rules()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_equality_true()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_non_numeric()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_get_applicable_rules_matching()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_get_applicable_rules_priority_order()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.__init__()** (2 connections) — `server/npc/behavior_engine.py`
- **.remove_rule()** (2 connections) — `server/npc/behavior_engine.py`
- **Deterministic behavior engine for NPCs.      This engine evaluates rules based o** (1 connections) — `server/npc/behavior_engine.py`
- **Initialize the behavior engine.** (1 connections) — `server/npc/behavior_engine.py`
- **Remove a behavior rule from the engine.          Args:             rule_name: Na** (1 connections) — `server/npc/behavior_engine.py`
- **Get the behavior engine for this NPC.** (1 connections) — `server/npc/npc_base.py`
- **Test add_rule() replaces existing rule with same name.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test add_rule() handles exceptions gracefully.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test get_rules() returns copy of rules.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test _evaluate_equality() returns True for matching condition.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test _evaluate_numeric_comparison() raises ValueError for non-numeric values.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test get_applicable_rules() returns matching rules.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test get_applicable_rules() returns rules in priority order.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`

## Relationships

- [behavior engine npc](behavior_engine_npc.md) (21 shared connections)
- [monitoring dashboard rationale](monitoring_dashboard_rationale.md) (12 shared connections)
- [room infrastructure persistence](room_infrastructure_persistence.md) (7 shared connections)
- [skill game service](skill_game_service.md) (6 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [room game service](room_game_service.md) (4 shared connections)
- [lucidity event services](lucidity_event_services.md) (2 shared connections)
- [game skill service](game_skill_service.md) (2 shared connections)
- [test_validate_combat_command_invalid_command_type](test_validate_combat_command_invalid_command_type.md) (1 shared connections)
- [chat game service](chat_game_service.md) (1 shared connections)
- [test_get_combat_status_message_in_combat](test_get_combat_status_message_in_combat.md) (1 shared connections)

## Source Files

- `server/npc/behavior_engine.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_behavior_engine.py`

## Audit Trail

- EXTRACTED: 111 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*