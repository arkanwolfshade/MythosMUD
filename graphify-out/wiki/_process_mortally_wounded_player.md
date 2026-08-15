# _process_mortally_wounded_player

> 25 nodes

## Key Concepts

- **_process_mortally_wounded_player()** (10 connections) — `server/app/game_tick_processing.py`
- **_process_mp_regeneration()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_session_dp_decay_and_death()** (8 connections) — `server/app/game_tick_processing.py`
- **Any** (8 connections)
- **_handle_player_death_threshold()** (7 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (7 connections)
- **_process_dead_players()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_passive_lucidity_flux()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_single_player_mp_regeneration()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_players()** (5 connections) — `server/app/game_tick_processing.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_player_in_active_combat()** (3 connections) — `server/app/game_tick_processing.py`
- **test_process_dead_players_moves_to_limbo()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_mortally_wounded_death_threshold()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_mortally_wounded_skips_active_combat()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_passive_lucidity_flux()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Return True when the player is in an active combat (skip passive DP decay).** (1 connections) — `server/app/game_tick_processing.py`
- **Move player to limbo and publish authoritative DP when death threshold is…** (1 connections) — `server/app/game_tick_processing.py`
- **Process a single mortally wounded player's DP decay and death check. CRITICAL:…** (1 connections) — `server/app/game_tick_processing.py`
- **Process all mortally wounded players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process passive lucidity flux service if available.** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for a single player. Args: mp_service: MP regeneration…** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for online players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process dead players and move them to limbo if needed.** (1 connections) — `server/app/game_tick_processing.py`
- **Process DP decay and death for a single database session.** (1 connections) — `server/app/game_tick_processing.py`

## Relationships

- [test_game_tick_processing.py](test_game_tick_processing.py.md) (12 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [asyncio](asyncio.md) (7 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [_update_player_status_effects](_update_player_status_effects.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 67 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*