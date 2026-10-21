# TestValidatorIntegration

> 19 nodes · cohesion 0.12

## Key Concepts

- **BehaviorEngine** (73 connections) — `server/npc/behavior_engine.py`
- **.get_behavior_engine()** (3 connections) — `server/npc/npc_base.py`
- **test_evaluate_condition_greater_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_greater_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_less_equal()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_condition_less_than()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_equality_true()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_evaluate_numeric_comparison_false()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **test_register_action_handler()** (3 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **.__init__()** (2 connections) — `server/npc/behavior_engine.py`
- **.remove_rule()** (2 connections) — `server/npc/behavior_engine.py`
- **Deterministic behavior engine for NPCs. This engine evaluates rules based on…** (1 connections) — `server/npc/behavior_engine.py`
- **Initialize the behavior engine.** (1 connections) — `server/npc/behavior_engine.py`
- **Remove a behavior rule from the engine. Args: rule_name: Name of the rule to…** (1 connections) — `server/npc/behavior_engine.py`
- **Get the behavior engine for this NPC.** (1 connections) — `server/npc/npc_base.py`
- **Test _evaluate_equality() returns True for matching condition.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test _evaluate_numeric_comparison() returns False when condition not met.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test evaluate_condition() handles > operator.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`
- **Test register_action_handler() registers handler.** (1 connections) — `server/tests/unit/npc/test_behavior_engine.py`

## Relationships

- [.cursor/hooks/record_edited_file.py](cursor-hooks-record_edited_file.py.md) (21 shared connections)
- [attach_compatibility_properties](attach_compatibility_properties.md) (12 shared connections)
- [BaseEvent](BaseEvent.md) (5 shared connections)
- [Critical File Coverage Improvement](Critical_File_Coverage_Improvement.md) (1 shared connections)
- [Issue Template Config](Issue_Template_Config.md) (1 shared connections)
- [authoritative_schema.sql](authoritative_schema.sql.md) (1 shared connections)
- [Deprecated get_async_persistence Global](Deprecated_get_async_persistence_Global.md) (1 shared connections)
- [Convert E2E Scenarios to Playwright CLI](Convert_E2E_Scenarios_to_Playwright_CLI.md) (1 shared connections)
- [Temporal System 4:1 Calendar Conversion](Temporal_System_4-1_Calendar_Conversion.md) (1 shared connections)
- [passive_lucidity_flux_tick Performance Alert](passive_lucidity_flux_tick_Performance_Alert.md) (1 shared connections)
- [Playwright MCP core-tabs Capability](Playwright_MCP_core-tabs_Capability.md) (1 shared connections)
- [Mute Command Server Error (Bug #1)](Mute_Command_Server_Error_Bug__1.md) (1 shared connections)

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