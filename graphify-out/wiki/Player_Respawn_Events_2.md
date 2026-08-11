# Player Respawn Events

> 50 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (52 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (32 connections) — `server/realtime/login_grace_period.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_flow.py** (18 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_expiration_handler()** (11 connections) — `server/realtime/login_grace_period.py`
- **UUID** (9 connections)
- **Any** (8 connections)
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **_trigger_room_occupants_update()** (5 connections) — `server/realtime/login_grace_period.py`
- **test_grace_period_expires_after_duration()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_warded_indicator_in_game_state_provider()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_start_grace_period_removes_from_combat()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_blocks_combat_initiation()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_remaining_time_decreases()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_start_time_tracking()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_cancel_login_grace_period()** (4 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_apply_damage_blocked_during_grace_period()** (4 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **mock_connection_manager()** (2 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **mock_async_persistence()** (2 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 25 more nodes in this community*

## Relationships

- [Integer Coercion Utils](Integer_Coercion_Utils.md) (21 shared connections)
- [API Type Guards](API_Type_Guards.md) (15 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (7 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (7 shared connections)
- [Status Effect Model](Status_Effect_Model.md) (5 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (5 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (4 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (4 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (4 shared connections)
- [Archive Planning E 2 E](Archive_Planning_E_2_E.md) (4 shared connections)
- [Game State Provider](Game_State_Provider.md) (4 shared connections)
- [Look Player Command](Look_Player_Command.md) (3 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 303 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*