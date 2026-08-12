# is_player_in_grace_period

> 79 nodes

## Key Concepts

- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **test_rest_and_grace_period.py** (25 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (18 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **asyncio** (13 connections)
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **asyncio** (9 connections)
- **test_intentional_disconnect_no_grace_period()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_blocks_during_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_starts_countdown_not_in_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_countdown_completes_disconnect()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_blocked_during_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_instant_disconnect()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_unintentional_disconnect_starts_grace_period()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_start_grace_period_reconnection_cancels()** (5 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **mock_persistence_full()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_can_auto_attack()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_cannot_use_commands()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_reconnection_cancels_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_interrupts_combat_action()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_visual_indicator_in_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_cancel_grace_period_cancels_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_errors_gracefully()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- *... and 54 more nodes in this community*

## Relationships

- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (16 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (9 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (2 shared connections)
- [test_look_player.py](test_look_player.py.md) (2 shared connections)
- [test_look_room.py](test_look_room.py.md) (2 shared connections)
- [GameStateProvider](GameStateProvider.md) (2 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (2 shared connections)
- [_check_grace_period_block](_check_grace_period_block.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 301 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*