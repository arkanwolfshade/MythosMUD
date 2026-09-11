# game_tick_death.py

> 27 nodes

## Key Concepts

- **game_tick_death.py** (35 connections) — `server/app/game_tick_death.py`
- **_process_mortally_wounded_player()** (14 connections) — `server/app/game_tick_death.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (9 connections) — `server/app/game_tick_death.py`
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_death.py`
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
- **Process DP decay and death for a single database session.** (1 connections) — `server/app/game_tick_death.py`
- **Return True when the player is in an active combat (skip passive DP decay).** (1 connections) — `server/app/game_tick_death.py`
- *... and 2 more nodes in this community*

## Relationships

- [game_tick_status_effects.py](game_tick_status_effects.py.md) (12 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (11 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (7 shared connections)
- [coerce_int](coerce_int.md) (5 shared connections)
- [event_types.py](event_types.py.md) (3 shared connections)
- [game_tick_protocols.py](game_tick_protocols.py.md) (3 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (2 shared connections)
- [combat_service.py](combat_service.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [get_async_session](get_async_session.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 92 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*