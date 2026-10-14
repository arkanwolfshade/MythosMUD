# ground_channel.py

> 55 nodes

## Key Concepts

- **cancel_ground_channel()** (23 connections) — `server/commands/ground_channel.py`
- **ground_channel.py** (23 connections) — `server/commands/ground_channel.py`
- **test_ground_channel.py** (23 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **RescueEventRecorder** (20 connections) — `server/tests/unit/commands/ground_commands_test_support.py`
- **FakeConnectionManager** (19 connections) — `server/tests/unit/commands/ground_commands_test_support.py`
- **start_ground_channel()** (15 connections) — `server/commands/ground_channel.py`
- **_start()** (14 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **GroundChannel** (11 connections) — `server/commands/ground_channel.py`
- **_FinishSpy** (10 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **asyncio** (10 connections)
- **is_player_grounding()** (9 connections) — `server/commands/ground_channel.py`
- **test_cancel_from_either_side_interrupts_both_and_clears_registry()** (9 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_cancel_is_ignored_once_committing()** (9 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_manager_without_registries_is_a_noop()** (8 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **_find_channel()** (7 connections) — `server/commands/ground_channel.py`
- **_registries()** (7 connections) — `server/commands/ground_channel.py`
- **_channel_task()** (7 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_completion_runs_finish_and_clears_registry()** (7 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_finish_interrupted_outcome_notifies_both()** (7 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_start_registers_channel_and_notifies_both_with_eta()** (7 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **UUID** (7 connections)
- **_run_channel()** (6 connections) — `server/commands/ground_channel.py`
- **test_rescuer_cannot_channel_two_rituals()** (6 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_resting_rescuer_cannot_start()** (6 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_second_rescuer_for_same_target_is_rejected()** (6 connections) — `server/tests/unit/commands/test_ground_channel.py`
- *... and 30 more nodes in this community*

## Relationships

- [rescue_commands.py](rescue_commands.py.md) (16 shared connections)
- [go_command.py](go_command.py.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [TaskRegistry](TaskRegistry.md) (2 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (2 shared connections)
- [MagicCommandHandler](MagicCommandHandler.md) (2 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (2 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (1 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (1 shared connections)

## Source Files

- `server/commands/ground_channel.py`
- `server/tests/unit/commands/ground_commands_test_support.py`
- `server/tests/unit/commands/test_ground_channel.py`

## Audit Trail

- EXTRACTED: 168 (91%)
- INFERRED: 16 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*