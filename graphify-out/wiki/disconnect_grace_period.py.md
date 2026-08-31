# disconnect_grace_period.py

> 40 nodes

## Key Concepts

- **disconnect_grace_period.py** (27 connections) — `server/realtime/disconnect_grace_period.py`
- **is_player_in_grace_period()** (24 connections) — `server/realtime/disconnect_grace_period.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (19 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **player_event_handlers_utils.py** (16 connections) — `server/realtime/player_event_handlers_utils.py`
- **cancel_grace_period()** (14 connections) — `server/realtime/disconnect_grace_period.py`
- **asyncio** (9 connections)
- **test_start_grace_period_reconnection_cancels()** (5 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_cancels_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_errors_gracefully()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_grace_period_handles_player_not_found()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_already_in_grace_period()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_creates_task()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_timer_expires()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **UUID** (4 connections)
- **mock_manager()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_false()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_no_manager_attribute()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Any** (3 connections)
- **fixture** (1 connections)
- **Disconnect grace period management for MythosMUD. This module handles the…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Check if a player is currently in grace period. Args: player_id: The player's…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- *... and 15 more nodes in this community*

## Relationships

- [test_player_disconnect_handlers.py](test_player_disconnect_handlers.py.md) (9 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (7 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [connection_establishment.py](connection_establishment.py.md) (3 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (3 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (3 shared connections)
- [test_look_player.py](test_look_player.py.md) (3 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (3 shared connections)
- [extract_player_name](extract_player_name.md) (3 shared connections)
- [test_player_presence_tracker.py](test_player_presence_tracker.py.md) (3 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (3 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_event_handlers_utils.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 132 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*