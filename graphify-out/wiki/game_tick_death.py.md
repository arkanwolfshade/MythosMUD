# game_tick_death.py

> 31 nodes

## Key Concepts

- **game_tick_death.py** (35 connections) — `server/app/game_tick_death.py`
- **_process_mortally_wounded_player()** (14 connections) — `server/app/game_tick_death.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (9 connections) — `server/app/game_tick_death.py`
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_death.py`
- **_process_dead_players()** (7 connections) — `server/app/game_tick_death.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_death.py`
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_death.py`
- **AsyncSession** (7 connections)
- **_process_mortally_wounded_players()** (6 connections) — `server/app/game_tick_death.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_death.py`
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_death.py`
- **combat_messaging_integration.py** (5 connections) — `server/services/combat_messaging_integration.py`
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
- *... and 6 more nodes in this community*

## Relationships

- [game_tick_status_effects.py](game_tick_status_effects.py.md) (12 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (11 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (8 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [coerce_int](coerce_int.md) (5 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (4 shared connections)
- [game_tick_protocols.py](game_tick_protocols.py.md) (3 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (2 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (2 shared connections)
- [models/combat.py](models-combat.py.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [seed_e2e_users.py](seed_e2e_users.py.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/services/combat_messaging_integration.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 101 (91%)
- INFERRED: 10 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*