# player persistence repository

> 27 nodes

## Key Concepts

- **game_tick_processing.py** (68 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (10 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (9 connections) — `server/app/game_tick_processing.py`
- **_process_mp_regeneration()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_session_dp_decay_and_death()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_processing.py`
- **UUID** (6 connections)
- **AsyncSession** (6 connections)
- **_process_dead_players()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_players()** (5 connections) — `server/app/game_tick_processing.py`
- **_validate_mp_regeneration_services()** (5 connections) — `server/app/game_tick_processing.py`
- **test_process_single_player_mp_regeneration()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_mp_regeneration_services()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_player_effects_expiration_login_warded()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_mortally_wounded_skips_active_combat()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_mortally_wounded_death_threshold()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_dead_players_moves_to_limbo()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Game tick processing functions.  This module handles all game tick processing lo** (1 connections) — `server/app/game_tick_processing.py`
- **Expire player_effects for this tick; for LOGIN_WARDED clear in-memory state and** (1 connections) — `server/app/game_tick_processing.py`
- **Process a single mortally wounded player's DP decay and death check.      CRITIC** (1 connections) — `server/app/game_tick_processing.py`
- **Process all mortally wounded players.** (1 connections) — `server/app/game_tick_processing.py`
- **Validate that required services exist for MP regeneration.      Args:         co** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for a single player.      Args:         mp_service: MP r** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for online players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process dead players and move them to limbo if needed.** (1 connections) — `server/app/game_tick_processing.py`
- *... and 2 more nodes in this community*

## Relationships

- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (25 shared connections)
- [persistence combat handler](persistence_combat_handler.md) (7 shared connections)
- [tick game processing](tick_game_processing.md) (5 shared connections)
- [command utility models](command_utility_models.md) (5 shared connections)
- [Player Stats](Player_Stats.md) (3 shared connections)
- [realtime message nats](realtime_message_nats.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [task registry app](task_registry_app.md) (3 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (2 shared connections)
- [npc lifecycle config](npc_lifecycle_config.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 161 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*