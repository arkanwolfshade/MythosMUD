# Game Tick Death

> 30 nodes

## Key Concepts

- **game_tick_death.py** (35 connections) — `server/app/game_tick_death.py`
- **_TickContainer** (23 connections) — `server/app/game_tick_protocols.py`
- **_process_mortally_wounded_player()** (14 connections) — `server/app/game_tick_death.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (9 connections) — `server/app/game_tick_death.py`
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_death.py`
- **_online_player_ids()** (8 connections) — `server/app/game_tick_protocols.py`
- **_process_dead_players()** (7 connections) — `server/app/game_tick_death.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_death.py`
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_death.py`
- **AsyncSession** (7 connections)
- **_process_mortally_wounded_players()** (6 connections) — `server/app/game_tick_death.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_death.py`
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_death.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Player** (3 connections)
- **test_validate_mp_regeneration_services()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **FastAPI** (2 connections)
- **DP decay, death, and MP regeneration for the game tick loop.** (1 connections) — `server/app/game_tick_death.py`
- **Process all mortally wounded players.** (1 connections) — `server/app/game_tick_death.py`
- **Process passive lucidity flux service if available.** (1 connections) — `server/app/game_tick_death.py`
- **Validate that required services exist for MP regeneration. Args: container:…** (1 connections) — `server/app/game_tick_death.py`
- **Process MP regeneration for a single player. Args: mp_service: MP regeneration…** (1 connections) — `server/app/game_tick_death.py`
- **Process MP regeneration for online players.** (1 connections) — `server/app/game_tick_death.py`
- **Process dead players and move them to limbo if needed.** (1 connections) — `server/app/game_tick_death.py`
- *... and 5 more nodes in this community*

## Relationships

- [Game Tick Processing](Game_Tick_Processing.md) (12 shared connections)
- [Game Tick Protocols](Game_Tick_Protocols.md) (7 shared connections)
- [Test Game Tick Death](Test_Game_Tick_Death.md) (7 shared connections)
- [Game Tick Status Effects](Game_Tick_Status_Effects.md) (6 shared connections)
- [Test Inventory Command Coercion](Test_Inventory_Command_Coercion.md) (5 shared connections)
- [Test Game Tick Processing](Test_Game_Tick_Processing.md) (4 shared connections)
- [Test Game Tick Processing Async](Test_Game_Tick_Processing_Async.md) (4 shared connections)
- [Test Player Event Handlers State](Test_Player_Event_Handlers_State.md) (2 shared connections)
- [Combat Events](Combat_Events.md) (2 shared connections)
- [Test Combat Cleanup Handler](Test_Combat_Cleanup_Handler.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (2 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_protocols.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 110 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*