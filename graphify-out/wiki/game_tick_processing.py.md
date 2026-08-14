# game_tick_processing.py

> 34 nodes

## Key Concepts

- **game_tick_processing.py** (79 connections) — `server/app/game_tick_processing.py`
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
- **_validate_mp_regeneration_services()** (5 connections) — `server/app/game_tick_processing.py`
- **passive_lucidity_flux_service.py** (5 connections) — `server/services/passive_lucidity_flux_service.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_player_in_active_combat()** (3 connections) — `server/app/game_tick_processing.py`
- **test_process_dead_players_moves_to_limbo()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_mortally_wounded_death_threshold()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_mortally_wounded_skips_active_combat()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_passive_lucidity_flux()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_mp_regeneration_services()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **UUID** (2 connections)
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- **Return True when the player is in an active combat (skip passive DP decay).** (1 connections) — `server/app/game_tick_processing.py`
- **Move player to limbo and publish authoritative DP when death threshold is…** (1 connections) — `server/app/game_tick_processing.py`
- **Process a single mortally wounded player's DP decay and death check. CRITICAL:…** (1 connections) — `server/app/game_tick_processing.py`
- *... and 9 more nodes in this community*

## Relationships

- [test_game_tick_processing.py](test_game_tick_processing.py.md) (38 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (9 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (4 shared connections)
- [coerce_int](coerce_int.md) (3 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (2 shared connections)
- [container_events.py](container_events.py.md) (2 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/services/passive_lucidity_flux_service.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 146 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*