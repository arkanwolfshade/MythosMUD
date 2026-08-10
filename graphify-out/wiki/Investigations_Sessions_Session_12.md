# Investigations Sessions Session

> 74 nodes

## Key Concepts

- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **test_command_validation.py** (22 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (18 connections) — `server/command_handler_unified.py`
- **check_catatonia_block()** (17 connections) — `server/command_handler/catatonia_check.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **Any** (14 connections)
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **CommandExecutionRequest** (11 connections)
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **process_command()** (9 connections) — `server/command_handler_unified.py`
- **_get_grace_check_context()** (8 connections) — `server/command_handler_unified.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler_unified.py`
- **TestHandleSpecialCommandRouting** (7 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **TestCheckCastingState** (6 connections) — `server/tests/unit/commands/test_command_validation.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **TestCheckRateLimit** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_handle_special_command_routing_alias_command()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_handle_special_command_routing_alias_storage_none()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- *... and 49 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (34 shared connections)
- [Admin Teleport Commands](Admin_Teleport_Commands.md) (24 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (16 shared connections)
- [Health Check Service](Health_Check_Service.md) (9 shared connections)
- [Test Refactoring Summary](Test_Refactoring_Summary.md) (6 shared connections)
- [NATS Connection State Machine](NATS_Connection_State_Machine.md) (6 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (6 shared connections)
- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (5 shared connections)
- [Npc Behavior Engine](Npc_Behavior_Engine.md) (5 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (5 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (3 shared connections)
- [Mythosmud Obsidian Raw](Mythosmud_Obsidian_Raw.md) (3 shared connections)

## Source Files

- `server/command_handler/catatonia_check.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler_unified.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 361 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*