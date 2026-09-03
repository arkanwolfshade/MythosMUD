# Game State Provider

> 90 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (51 connections) — `server/realtime/login_grace_period.py`
- **.state()** (32 connections) — `server/realtime/connection_state_machine.py`
- **GameStateProvider** (24 connections) — `server/realtime/integration/game_state_provider.py`
- **get_login_grace_period_remaining()** (22 connections) — `server/realtime/login_grace_period.py`
- **game_state_provider.py** (22 connections) — `server/realtime/integration/game_state_provider.py`
- **test_login_grace_period_flow.py** (22 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **UUID** (14 connections)
- **FakeGraceManager** (13 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **.connection_manager()** (9 connections) — `server/realtime/nats_message_handler.py`
- **asyncio** (9 connections)
- **._apply_player_combat_effects()** (8 connections) — `server/npc/combat_integration_base.py`
- **._get_player_data_for_client()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._is_target_in_login_grace_period()** (7 connections) — `server/npc/combat_integration_base.py`
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._process_occupants_with_grace_periods()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_expires_after_duration()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **._convert_player_uuids_to_names()** (6 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 65 more nodes in this community*

## Relationships

- [Test Login Grace Period](Test_Login_Grace_Period.md) (36 shared connections)
- [Combat Integration Base](Combat_Integration_Base.md) (9 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (7 shared connections)
- [Npc Combat Grace](Npc_Combat_Grace.md) (4 shared connections)
- [Test Rest And Grace Period](Test_Rest_And_Grace_Period.md) (4 shared connections)
- [Players](Players.md) (4 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (4 shared connections)
- [Test Game State Provider](Test_Game_State_Provider.md) (3 shared connections)
- [Websocket Handler Commands](Websocket_Handler_Commands.md) (3 shared connections)
- [Test Envelope](Test_Envelope.md) (3 shared connections)
- [Test Combat Service Modules](Test_Combat_Service_Modules.md) (3 shared connections)
- [Test Config Init](Test_Config_Init.md) (2 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/realtime/connection_state_machine.py`
- `server/realtime/integration/__init__.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/integration/test_login_grace_period_flow.py`

## Audit Trail

- EXTRACTED: 267 (88%)
- INFERRED: 37 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*