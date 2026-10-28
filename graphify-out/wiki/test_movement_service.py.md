# test_movement_service.py

> 72 nodes · cohesion 0.04

## Key Concepts

- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **asyncio** (21 connections)
- **_process_alias_expansion()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (15 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **TestHandleSpecialCommandRouting** (7 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **TestValidateCommandBasics** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_handle_special_command_routing_alias_command()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_handle_special_command_routing_alias_storage_none()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_handle_special_command_routing_emote_conversion()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_handle_special_command_routing_returns_none()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_all_command_blocks_casting()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_all_command_blocks_catatonia()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_all_command_blocks_grace_period()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_process_alias_expansion_invalid_expanded()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_process_alias_expansion_no_alias()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_process_alias_expansion_no_storage()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_process_alias_expansion_unsafe_alias()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_allowed_commands()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_error_handling()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_is_casting()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_no_magic_service()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_casting_state_not_casting()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_in_grace_period()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_grace_period_block_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- *... and 47 more nodes in this community*

## Relationships

- [QuestService](QuestService.md) (18 shared connections)
- [DialogueService](DialogueService.md) (9 shared connections)
- [go_command.py](go_command.py.md) (6 shared connections)
- [look_container.py](look_container.py.md) (5 shared connections)
- [command_parser.py](command_parser.py.md) (3 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (2 shared connections)
- [test_passive_corruption_flux_rate_overrides.py](test_passive_corruption_flux_rate_overrides.py.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 144 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*