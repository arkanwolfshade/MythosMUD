# game_tick_death.py

> 35 nodes

## Key Concepts

- **game_tick_death.py** (38 connections) — `server/app/game_tick_death.py`
- **_TickContainer** (24 connections) — `server/app/game_tick_protocols.py`
- **_process_mortally_wounded_player()** (14 connections) — `server/app/game_tick_death.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **_process_passive_corruption_flux()** (11 connections) — `server/app/game_tick_death.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **_online_player_ids()** (9 connections) — `server/app/game_tick_protocols.py`
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_death.py`
- **AsyncSession** (8 connections)
- **_process_dead_players()** (7 connections) — `server/app/game_tick_death.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_death.py`
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_death.py`
- **_process_mortally_wounded_players()** (6 connections) — `server/app/game_tick_death.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_death.py`
- **_TickMpRegen** (5 connections) — `server/app/game_tick_protocols.py`
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_death.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Player** (3 connections)
- **test_validate_mp_regeneration_services()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **FastAPI** (2 connections)
- **DP decay, death, and MP regeneration for the game tick loop.** (1 connections) — `server/app/game_tick_death.py`
- **Process a single mortally wounded player's DP decay and death check. CRITICAL:…** (1 connections) — `server/app/game_tick_death.py`
- **Process all mortally wounded players.** (1 connections) — `server/app/game_tick_death.py`
- **Process passive lucidity flux service if available.** (1 connections) — `server/app/game_tick_death.py`
- *... and 10 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (20 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (14 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (7 shared connections)
- [Player](Player.md) (6 shared connections)
- [Protocol](Protocol.md) (5 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (2 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [event_types.py](event_types.py.md) (1 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_protocols.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 129 (91%)
- INFERRED: 12 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*