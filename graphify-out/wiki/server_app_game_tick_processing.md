# server app game tick processing

> 30 nodes

## Key Concepts

- **game_tick_processing.py** (50 connections) — `server/app/game_tick_processing.py`
- **game_tick_status_effects.py** (26 connections) — `server/app/game_tick_status_effects.py`
- **_process_single_effect()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_damage_over_time_effect()** (12 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (11 connections) — `server/app/game_tick_status_effects.py`
- **_process_heal_over_time_effect()** (10 connections) — `server/app/game_tick_status_effects.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_status_effects.py`
- **FastAPI** (9 connections)
- **process_player_effects_expiration()** (8 connections) — `server/app/game_tick_status_effects.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_status_effects.py`
- **_process_status_effects_for_players()** (7 connections) — `server/app/game_tick_status_effects.py`
- **Player** (6 connections)
- **_TickConnectionManager** (5 connections) — `server/app/game_tick_protocols.py`
- **_handle_login_warded_expirations()** (5 connections) — `server/app/game_tick_status_effects.py`
- **UUID** (3 connections)
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- **Status-effect processing for the game tick loop.** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process a single status effect. Returns: Tuple of (updated_effect_dict or None…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Update and save player status effects if changes occurred. Returns: True if…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Validate container and retrieve player by ID. Args: container: Application…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process all status effects for a player. Args: app: FastAPI application…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process status effects for a single player. Returns: True if player was…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Clear in-memory grace state for each expired LOGIN_WARDED effect.** (1 connections) — `server/app/game_tick_status_effects.py`
- *... and 5 more nodes in this community*

## Relationships

- [playerdpupdated](playerdpupdated.md) (22 shared connections)
- [server app game tick status](server_app_game_tick_status.md) (16 shared connections)
- [server app game tick processing](server_app_game_tick_processing.md) (15 shared connections)
- [corpselifecycleservice](corpselifecycleservice.md) (10 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (8 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (4 shared connections)
- [server app game tick protocols](server_app_game_tick_protocols.md) (2 shared connections)
- [server api players](server_api_players.md) (2 shared connections)
- [server config npc config](server_config_npc_config.md) (1 shared connections)
- [server realtime connection manager api](server_realtime_connection_manager_api.md) (1 shared connections)
- [holidayresolver](holidayresolver.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`

## Audit Trail

- EXTRACTED: 129 (85%)
- INFERRED: 23 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*