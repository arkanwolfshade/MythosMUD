# test_rest_and_grace_period.py

> 45 nodes

## Key Concepts

- **test_rest_and_grace_period.py** (26 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **is_player_in_grace_period()** (24 connections) — `server/realtime/disconnect_grace_period.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **asyncio** (13 connections)
- **test_intentional_disconnect_no_grace_period()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_blocks_during_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_starts_countdown_not_in_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_countdown_completes_disconnect()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_blocked_during_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_instant_disconnect()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_unintentional_disconnect_starts_grace_period()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **mock_persistence_full()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_can_auto_attack()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_cannot_use_commands()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_reconnection_cancels_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_interrupts_combat_action()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_visual_indicator_in_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **mock_app_with_services()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **mock_connection_manager_full()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **fixture** (3 connections)
- **.get_player_by_name()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.get_room_by_id()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.__setattr__()** (2 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **.__init__()** (1 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **Check if a player is currently in grace period. Args: player_id: The player's…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- *... and 20 more nodes in this community*

## Relationships

- [test_rest_command.py](test_rest_command.py.md) (9 shared connections)
- [start_grace_period](start_grace_period.md) (8 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (3 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (2 shared connections)
- [test_look_player.py](test_look_player.py.md) (2 shared connections)
- [GameStateProvider](GameStateProvider.md) (2 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (2 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (2 shared connections)
- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/integration/test_rest_and_grace_period.py`

## Audit Trail

- EXTRACTED: 104 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*