# player disconnect handlers

> 115 nodes

## Key Concepts

- **test_player_disconnect_handlers.py** (34 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **disconnect_grace_period.py** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **is_player_in_grace_period()** (26 connections) — `server/realtime/disconnect_grace_period.py`
- **test_rest_and_grace_period.py** (24 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **start_grace_period()** (20 connections) — `server/realtime/disconnect_grace_period.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **test_disconnect_grace_period.py** (17 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **cancel_grace_period()** (12 connections) — `server/realtime/disconnect_grace_period.py`
- **_cleanup_player_references()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **_remove_player_from_online_tracking()** (10 connections) — `server/realtime/player_disconnect_handlers.py`
- **UUID** (7 connections)
- **UUID** (4 connections)
- **test_start_grace_period_reconnection_cancels()** (4 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **Any** (3 connections)
- **test_reconnection_cancels_grace_period()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_can_auto_attack()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_cannot_use_commands()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_visual_indicator_in_grace_period()** (3 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_start_grace_period_creates_task()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_already_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_start_grace_period_timer_expires()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_not_in_grace_period()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_cancel_grace_period_cancels_task()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **test_is_player_in_grace_period_true()** (3 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- *... and 90 more nodes in this community*

## Relationships

- [Player](Player.md) (14 shared connections)
- [player presence tracker](player_presence_tracker.md) (12 shared connections)
- [command admin](command_admin.md) (9 shared connections)
- [Any](Any.md) (7 shared connections)
- [login grace period](login_grace_period.md) (6 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (4 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (3 shared connections)
- [look player](look_player.md) (3 shared connections)
- [look room](look_room.md) (3 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (2 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/realtime/player_disconnect_handlers.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`

## Audit Trail

- EXTRACTED: 413 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*