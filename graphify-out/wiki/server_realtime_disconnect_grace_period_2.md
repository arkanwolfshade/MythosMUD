# server realtime disconnect grace period

> 36 nodes

## Key Concepts

- **disconnect_grace_period.py** (27 connections) — `server/realtime/disconnect_grace_period.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (19 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
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
- **Start a grace period for a disconnected player. During the grace period, the…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Unit tests for disconnect grace period management. Tests the grace period…** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Test grace period is cancelled when player reconnects.** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- *... and 11 more nodes in this community*

## Relationships

- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (10 shared connections)
- [server realtime player disconnect handlers](server_realtime_player_disconnect_handlers.md) (9 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (5 shared connections)
- [server realtime connection establishment](server_realtime_connection_establishment.md) (3 shared connections)
- [server realtime player connection setup](server_realtime_player_connection_setup.md) (3 shared connections)
- [server realtime player presence tracker](server_realtime_player_presence_tracker.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [server realtime player presence utils](server_realtime_player_presence_utils.md) (2 shared connections)
- [server command handler command execution](server_command_handler_command_execution.md) (1 shared connections)
- [server commands look player](server_commands_look_player.md) (1 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (1 shared connections)
- [server realtime integration game state](server_realtime_integration_game_state.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 101 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*