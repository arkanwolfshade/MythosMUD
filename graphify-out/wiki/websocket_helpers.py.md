# websocket_helpers.py

> 58 nodes · cohesion 0.09

## Key Concepts

- **ground_channel.py** (23 connections) — `server/commands/ground_channel.py`
- **cancel_ground_channel()** (23 connections) — `server/commands/ground_channel.py`
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
- **UUID** (7 connections)
- **_registries()** (7 connections) — `server/commands/ground_channel.py`
- **_channel_task()** (7 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_completion_runs_finish_and_clears_registry()** (7 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_finish_interrupted_outcome_notifies_both()** (7 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_start_registers_channel_and_notifies_both_with_eta()** (7 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **_run_channel()** (6 connections) — `server/commands/ground_channel.py`
- **test_rescuer_cannot_channel_two_rituals()** (6 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_resting_rescuer_cannot_start()** (6 connections) — `server/tests/unit/commands/test_ground_channel.py`
- **test_second_rescuer_for_same_target_is_rejected()** (6 connections) — `server/tests/unit/commands/test_ground_channel.py`
- *... and 33 more nodes in this community*

## Relationships

- [test_connection_establishment.py](test_connection_establishment.py.md) (16 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (4 shared connections)
- [CORSConfig](CORSConfig.md) (3 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (2 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (2 shared connections)
- [inventory_item_matching.py](inventory_item_matching.py.md) (2 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [Semgrep Configuration](Semgrep_Configuration.md) (1 shared connections)

## Source Files

- `server/commands/ground_channel.py`
- `server/tests/unit/commands/ground_commands_test_support.py`
- `server/tests/unit/commands/test_ground_channel.py`

## Audit Trail

- EXTRACTED: 171 (91%)
- INFERRED: 16 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*