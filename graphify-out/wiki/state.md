# .state

> 67 nodes

## Key Concepts

- **.state()** (37 connections) — `server/realtime/connection_state_machine.py`
- **rescue_commands.py** (33 connections) — `server/commands/rescue_commands.py`
- **handle_ground_command()** (27 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (24 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **asyncio** (17 connections)
- **handle_rescue_command()** (14 connections) — `server/commands/rescue_commands.py`
- **Any** (9 connections)
- **_run_ground_session()** (8 connections) — `server/commands/rescue_commands.py`
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **patch** (7 connections)
- **test_handle_ground_command_apply_lucidity_error()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_player_key()** (6 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **UUID** (6 connections)
- **_complete_ground_command()** (5 connections) — `server/commands/rescue_commands.py`
- **_get_ground_services()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_success_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- **test_handle_ground_command_lucidity_record_not_found()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_target_player_key()** (5 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **_send_grounding_channeling_events()** (4 connections) — `server/commands/rescue_commands.py`
- *... and 42 more nodes in this community*

## Relationships

- [LucidityService](LucidityService.md) (20 shared connections)
- [AliasStorage](AliasStorage.md) (12 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)
- [GameStateProvider](GameStateProvider.md) (3 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [real_time.py](real_time.py.md) (2 shared connections)
- [.on_enter_state](on_enter_state.md) (1 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)
- [test_command_processing.py](test_command_processing.py.md) (1 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (1 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/realtime/connection_state_machine.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 164 (80%)
- INFERRED: 42 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*