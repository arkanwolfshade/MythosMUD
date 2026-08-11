# Player Respawn Events

> 109 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (52 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (32 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period.py** (24 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_flow.py** (18 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **npc_combat_grace.py** (13 connections) — `server/services/npc_combat_grace.py`
- **_grace_period_expiration_handler()** (11 connections) — `server/realtime/login_grace_period.py`
- **test_combat_grace_period.py** (11 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **UUID** (9 connections)
- **Any** (8 connections)
- **_connection_manager_from_config_app()** (8 connections) — `server/services/npc_combat_grace.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **is_player_attack_blocked_by_login_grace_period()** (7 connections) — `server/services/npc_combat_grace.py`
- **is_npc_attack_on_player_blocked_by_login_grace_period()** (7 connections) — `server/services/npc_combat_grace.py`
- **_trigger_room_occupants_update()** (5 connections) — `server/realtime/login_grace_period.py`
- **test_grace_period_expires_after_duration()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_warded_indicator_in_game_state_provider()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_start_grace_period_removes_from_combat()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 84 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (20 shared connections)
- [API Type Guards](API_Type_Guards.md) (15 shared connections)
- [Game State Provider](Game_State_Provider.md) (8 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (8 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (7 shared connections)
- [Command Alias Handling](Command_Alias_Handling.md) (7 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (7 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (4 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (3 shared connections)
- [Look Player Command](Look_Player_Command.md) (3 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (3 shared connections)
- [Chat Rate Limiter](Chat_Rate_Limiter.md) (3 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/services/npc_combat_grace.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 483 (99%)
- INFERRED: 7 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*