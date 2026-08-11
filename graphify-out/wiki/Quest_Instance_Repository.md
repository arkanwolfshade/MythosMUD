# Quest Instance Repository

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

- [WebSocket Message Handlers](WebSocket_Message_Handlers.md) (21 shared connections)
- [Real-Time Architecture Docs](Real-Time_Architecture_Docs.md) (12 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (5 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (1 shared connections)
- [test_apply_encounter_lucidity_loss_acclimated](test_apply_encounter_lucidity_loss_acclimated.md) (1 shared connections)
- [test_is_player_disconnecting_no_connection_manager](test_is_player_disconnecting_no_connection_manager.md) (1 shared connections)
- [test_process_dict_occupant_with_name](test_process_dict_occupant_with_name.md) (1 shared connections)
- [test_apply_encounter_lucidity_loss_with_location](test_apply_encounter_lucidity_loss_with_location.md) (1 shared connections)
- [test_perform_recovery_action_success](test_perform_recovery_action_success.md) (1 shared connections)
- [test_is_player_disconnecting_no_disconnecting_players_attr](test_is_player_disconnecting_no_disconnecting_players_attr.md) (1 shared connections)
- [test_normalize_player_id_uuid](test_normalize_player_id_uuid.md) (1 shared connections)
- [test_player_event_handler_utils_init](test_player_event_handler_utils_init.md) (1 shared connections)

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