# game_tick_processing.py

> 54 nodes

## Key Concepts

- **game_tick_processing.py** (83 connections) — `server/app/game_tick_processing.py`
- **_TickContainer** (20 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (12 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (12 connections)
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **Player** (11 connections)
- **_process_mp_regeneration()** (9 connections) — `server/app/game_tick_processing.py`
- **_process_session_dp_decay_and_death()** (9 connections) — `server/app/game_tick_processing.py`
- **Protocol** (9 connections)
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_processing.py`
- **UUID** (8 connections)
- **_process_dead_players()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_processing.py`
- **_TickDeathService** (6 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_players()** (6 connections) — `server/app/game_tick_processing.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_processing.py`
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_processing.py`
- **combat_messaging_integration.py** (5 connections) — `server/services/combat_messaging_integration.py`
- **_TickCombatService** (4 connections) — `server/app/game_tick_processing.py`
- **_TickMpRegen** (4 connections) — `server/app/game_tick_processing.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_TickConnectionManager** (3 connections) — `server/app/game_tick_processing.py`
- **_TickEventBus** (3 connections) — `server/app/game_tick_processing.py`
- **_TickMagicService** (3 connections) — `server/app/game_tick_processing.py`
- *... and 29 more nodes in this community*

## Relationships

- [test_game_tick_processing.py](test_game_tick_processing.py.md) (42 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (13 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [coerce_int](coerce_int.md) (5 shared connections)
- [get_current_tick](get_current_tick.md) (4 shared connections)
- [test_connection_manager_api.py](test_connection_manager_api.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [HolidayService](HolidayService.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (2 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/realtime/connection_manager_api.py`
- `server/services/combat_messaging_integration.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 210 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*