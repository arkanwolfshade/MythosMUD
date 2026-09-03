# Test Login Grace Period

> 92 nodes

## Key Concepts

- **login_grace_period.py** (44 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (43 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (29 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_login_grace_period.py** (26 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **UUID** (13 connections)
- **handle_login_grace_period_expiration()** (10 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (10 connections)
- **_as_grace()** (9 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_task()** (8 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (8 connections)
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **test_both_linkdead_and_warded_indicators()** (7 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_removed_after_expiration()** (7 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Protocol** (7 connections)
- **_login_grace_period_seconds()** (6 connections) — `server/realtime/login_grace_period.py`
- **_trigger_room_occupants_update()** (6 connections) — `server/realtime/login_grace_period.py`
- **_try_start_effect_based_grace()** (6 connections) — `server/realtime/login_grace_period.py`
- **test_warded_indicator_in_game_state_provider()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_player_occupant_processor()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **_GraceManager** (5 connections) — `server/realtime/login_grace_period.py`
- **test_cancel_login_grace_period()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_warded_indicator_in_look_player()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_look_room()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_websocket_room_updates()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- *... and 67 more nodes in this community*

## Relationships

- [Game State Provider](Game_State_Provider.md) (36 shared connections)
- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (7 shared connections)
- [Player Occupant Processor](Player_Occupant_Processor.md) (7 shared connections)
- [Test Player Name Utils](Test_Player_Name_Utils.md) (5 shared connections)
- [Test Look Player](Test_Look_Player.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (4 shared connections)
- [Game Tick Status Effects](Game_Tick_Status_Effects.md) (3 shared connections)
- [Players](Players.md) (3 shared connections)
- [Player Connection Setup](Player_Connection_Setup.md) (3 shared connections)
- [Test Combat Grace Period](Test_Combat_Grace_Period.md) (3 shared connections)
- [Test Rest And Grace Period](Test_Rest_And_Grace_Period.md) (3 shared connections)
- [Test Look Room](Test_Look_Room.md) (3 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 251 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*