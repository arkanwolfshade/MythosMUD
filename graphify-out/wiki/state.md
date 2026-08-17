# .state

> 80 nodes

## Key Concepts

- **.state()** (37 connections) — `server/realtime/connection_state_machine.py`
- **.app()** (34 connections) — `server/commands/look_helpers.py`
- **rescue_commands.py** (33 connections) — `server/commands/rescue_commands.py`
- **handle_ground_command()** (27 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (24 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **resolve_state()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **asyncio** (17 connections)
- **handle_rescue_command()** (15 connections) — `server/commands/rescue_commands.py`
- **Any** (9 connections)
- **_run_ground_session()** (8 connections) — `server/commands/rescue_commands.py`
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **patch** (7 connections)
- **_get_ground_services()** (6 connections) — `server/commands/rescue_commands.py`
- **test_handle_ground_command_apply_lucidity_error()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_player_key()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **UUID** (6 connections)
- **test_inventory_commands_state_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- **_app_state_container_service()** (5 connections) — `server/commands/container_helpers_inventory_ops.py`
- **_complete_ground_command()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_success_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- *... and 55 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (12 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [websocket_initial_state.py](websocket_initial_state.py.md) (5 shared connections)
- [test_lucidity_event_dispatcher.py](test_lucidity_event_dispatcher.py.md) (5 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (4 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (4 shared connections)
- [asyncio](asyncio.md) (4 shared connections)
- [position_commands.py](position_commands.py.md) (4 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (3 shared connections)
- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (3 shared connections)

## Source Files

- `server/commands/container_helpers_inventory_ops.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/look_helpers.py`
- `server/commands/rescue_commands.py`
- `server/realtime/connection_state_machine.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 194 (72%)
- INFERRED: 74 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*