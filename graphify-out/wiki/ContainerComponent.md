# ContainerComponent

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

- [test behavior engine](test_behavior_engine.md) (21 shared connections)
- [test command factories moderation](test_command_factories_moderation.md) (12 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (5 shared connections)
- [description](description.md) (2 shared connections)
- [lib](lib.md) (2 shared connections)
- [sub zone](sub_zone.md) (2 shared connections)
- [Test check all command blocks](Test_check_all_command_blocks.md) (1 shared connections)
- [Test extract zone from room](Test_extract_zone_from_room.md) (1 shared connections)
- [Test check rate limit function.](Test_check_rate_limit_function.md) (1 shared connections)
- [Test create say command delegates](Test_create_say_command_delegates.md) (1 shared connections)
- [minLength](minLength.md) (1 shared connections)
- [test websocket handler json error](test_websocket_handler_json_error.md) (1 shared connections)

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