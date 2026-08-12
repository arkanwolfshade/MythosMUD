# _process_session_dp_decay_and_death

> 19 nodes

## Key Concepts

- **_process_session_dp_decay_and_death()** (8 connections) — `server/app/game_tick_processing.py`
- **_handle_player_death_threshold()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (7 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (7 connections)
- **_process_mp_regeneration()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_players()** (5 connections) — `server/app/game_tick_processing.py`
- **_process_dead_players()** (4 connections) — `server/app/game_tick_processing.py`
- **_process_passive_lucidity_flux()** (4 connections) — `server/app/game_tick_processing.py`
- **_player_in_active_combat()** (3 connections) — `server/app/game_tick_processing.py`
- **_validate_mp_regeneration_services()** (3 connections) — `server/app/game_tick_processing.py`
- **Return True when the player is in an active combat (skip passive DP decay).** (1 connections) — `server/app/game_tick_processing.py`
- **Move player to limbo and publish authoritative DP when death threshold is…** (1 connections) — `server/app/game_tick_processing.py`
- **Process a single mortally wounded player's DP decay and death check. CRITICAL:…** (1 connections) — `server/app/game_tick_processing.py`
- **Process all mortally wounded players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process passive lucidity flux service if available.** (1 connections) — `server/app/game_tick_processing.py`
- **Validate that required services exist for MP regeneration. Args: container:…** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for online players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process dead players and move them to limbo if needed.** (1 connections) — `server/app/game_tick_processing.py`
- **Process DP decay and death for a single database session.** (1 connections) — `server/app/game_tick_processing.py`

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (10 shared connections)
- [coerce_int](coerce_int.md) (2 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (2 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*