# process dead players()

> 17 nodes

## Key Concepts

- **_process_session_dp_decay_and_death()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (7 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (6 connections)
- **_process_mp_regeneration()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_players()** (5 connections) — `server/app/game_tick_processing.py`
- **_process_single_player_mp_regeneration()** (5 connections) — `server/app/game_tick_processing.py`
- **_process_passive_lucidity_flux()** (4 connections) — `server/app/game_tick_processing.py`
- **_process_dead_players()** (4 connections) — `server/app/game_tick_processing.py`
- **_validate_mp_regeneration_services()** (3 connections) — `server/app/game_tick_processing.py`
- **Process a single mortally wounded player's DP decay and death check.      CRITIC** (1 connections) — `server/app/game_tick_processing.py`
- **Process all mortally wounded players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process passive lucidity flux service if available.** (1 connections) — `server/app/game_tick_processing.py`
- **Validate that required services exist for MP regeneration.      Args:         co** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for a single player.      Args:         mp_service: MP r** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for online players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process dead players and move them to limbo if needed.** (1 connections) — `server/app/game_tick_processing.py`
- **Process DP decay and death for a single database session.** (1 connections) — `server/app/game_tick_processing.py`

## Relationships

- [game tick processing](game_tick_processing.md) (11 shared connections)
- [Any](Any.md) (1 shared connections)
- [.apply dp change()](apply_dp_change%28%29.md) (1 shared connections)
- [process all status effects()](process_all_status_effects%28%29.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`

## Audit Trail

- EXTRACTED: 56 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*