# disconnect_grace_period.py

> 88 nodes

## Key Concepts

- **disconnect_grace_period.py** (35 connections) — `server/realtime/disconnect_grace_period.py`
- **test_rest_and_grace_period.py** (25 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **is_player_in_grace_period()** (24 connections) — `server/realtime/disconnect_grace_period.py`
- **start_grace_period()** (23 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (18 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **cancel_grace_period()** (15 connections) — `server/realtime/disconnect_grace_period.py`
- **MockPersistenceFull** (14 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **asyncio** (13 connections)
- **asyncio** (9 connections)
- **test_intentional_disconnect_no_grace_period()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_blocks_during_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_command_starts_countdown_not_in_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_countdown_completes_disconnect()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_blocked_during_combat()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_location_instant_disconnect()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_unintentional_disconnect_starts_grace_period()** (5 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_start_grace_period_reconnection_cancels()** (5 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **UUID** (5 connections)
- **_PlayerLookupManager** (4 connections) — `server/realtime/disconnect_grace_period.py`
- **_grace_period_seconds()** (4 connections) — `server/realtime/disconnect_grace_period.py`
- **mock_persistence_full()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_can_auto_attack()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_cannot_use_commands()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_reconnection_cancels_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_interrupts_combat_action()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- *... and 63 more nodes in this community*

## Relationships

- [Test Player Disconnect Handlers](Test_Player_Disconnect_Handlers.md) (9 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (9 shared connections)
- [test_disconnect_catchup.py](test_disconnect_catchup.py.md) (6 shared connections)
- [player_presence_tracker.py](player_presence_tracker.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (3 shared connections)
- [command_guards.py](command_guards.py.md) (3 shared connections)
- [test_look_player.py](test_look_player.py.md) (3 shared connections)
- [CorruptionTier](CorruptionTier.md) (3 shared connections)
- [PlayerOccupantProcessor](PlayerOccupantProcessor.md) (3 shared connections)
- [extract_player_name](extract_player_name.md) (3 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 210 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*