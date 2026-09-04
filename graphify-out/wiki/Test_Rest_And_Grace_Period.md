# Test Rest And Grace Period

> 88 nodes

## Key Concepts

- **disconnect_grace_period.py** (29 connections) — `server/realtime/disconnect_grace_period.py`
- **test_rest_and_grace_period.py** (26 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **is_player_in_grace_period()** (24 connections) — `server/realtime/disconnect_grace_period.py`
- **test_disconnect_grace_period.py** (19 connections) — `server/tests/unit/realtime/test_disconnect_grace_period.py`
- **start_grace_period()** (18 connections) — `server/realtime/disconnect_grace_period.py`
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
- **mock_persistence_full()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_can_auto_attack()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_grace_period_player_cannot_use_commands()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_reconnection_cancels_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_rest_interrupts_combat_action()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- **test_visual_indicator_in_grace_period()** (4 connections) — `server/tests/integration/test_rest_and_grace_period.py`
- *... and 63 more nodes in this community*

## Relationships

- [Test Rest Command](Test_Rest_Command.md) (9 shared connections)
- [Test Disconnect Catchup](Test_Disconnect_Catchup.md) (6 shared connections)
- [Test Player Presence Tracker](Test_Player_Presence_Tracker.md) (6 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (4 shared connections)
- [Game State Provider](Game_State_Provider.md) (4 shared connections)
- [Player Connection Setup](Player_Connection_Setup.md) (3 shared connections)
- [Command Guards](Command_Guards.md) (3 shared connections)
- [Test Look Player](Test_Look_Player.md) (3 shared connections)
- [Occupant Display](Occupant_Display.md) (3 shared connections)
- [Player Occupant Processor](Player_Occupant_Processor.md) (3 shared connections)
- [Test Login Grace Period](Test_Login_Grace_Period.md) (3 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (2 shared connections)

## Source Files

- `server/realtime/disconnect_grace_period.py`
- `server/tests/integration/test_rest_and_grace_period.py`
- `server/tests/unit/realtime/test_disconnect_grace_period.py`

## Audit Trail

- EXTRACTED: 200 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*