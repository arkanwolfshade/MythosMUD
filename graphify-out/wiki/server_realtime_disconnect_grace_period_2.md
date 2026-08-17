# server realtime disconnect grace period

> 34 nodes

## Key Concepts

- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (19 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
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
- **Cancel grace period for a player (e.g., on reconnection). Args: player_id: The…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Start a grace period for a disconnected player. During the grace period, the…** (1 connections) — `server/realtime/disconnect_grace_period.py`
- **Unit tests for disconnect grace period management. Tests the grace period…** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Test grace period is cancelled when player reconnects.** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Test cancel_grace_period() does nothing if player not in grace period.** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Test cancel_grace_period() cancels the grace period task.** (1 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- *... and 9 more nodes in this community*

## Relationships

- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (8 shared connections)
- [server realtime player disconnect handlers](server_realtime_player_disconnect_handlers.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (2 shared connections)
- [server realtime player connection setup](server_realtime_player_connection_setup.md) (1 shared connections)
- [server realtime player presence utils](server_realtime_player_presence_utils.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 76 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*