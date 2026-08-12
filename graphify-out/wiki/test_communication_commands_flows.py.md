# test_communication_commands_flows.py

> 45 nodes

## Key Concepts

- **test_communication_commands_flows.py** (41 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **SimpleNamespace** (39 connections)
- **asyncio** (18 connections)
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **_message_from_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **flow_reply_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_room_player_bundle()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_global_player_bundle()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_whisper_id_pair_or_error()** (8 connections) — `server/commands/communication_commands_flows.py`
- **test_flow_global_command_blocks_low_level_user()** (5 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_reply_command_no_last_sender_returns_user_message()** (5 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_reply_command_success_uses_container_services()** (5 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_say_command_success_broadcasts_room_message()** (5 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_system_command_blocks_non_admin_user()** (5 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_whisper_command_exception_returns_generic_message()** (5 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_flow_whisper_command_success_sends_private_message()** (5 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_command_request_app_state_from_http_request_like_object()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_command_request_app_state_missing_app_or_state_returns_none()** (4 connections) — `server/tests/unit/command_handler/test_command_execution_request.py`
- **test_global_player_bundle_level_too_low()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_global_player_bundle_non_int_level_coerced()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_global_player_bundle_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_player_id_bundle_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_room_player_bundle_no_primary_id()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_room_player_bundle_success()** (4 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **test_room_player_bundle_no_room()** (3 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- *... and 20 more nodes in this community*

## Relationships

- [communication_commands_flows.py](communication_commands_flows.py.md) (40 shared connections)
- [test_communication_commands_support.py](test_communication_commands_support.py.md) (11 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [NPCCacheService](NPCCacheService.md) (3 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)
- [fixtures/unit/__init__.py](fixtures-unit-__init__.py.md) (1 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_flows.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`

## Audit Trail

- EXTRACTED: 127 (77%)
- INFERRED: 38 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*