# _process_mortally_wounded_player

> 30 nodes

## Key Concepts

- **_process_mortally_wounded_player()** (12 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (12 connections)
- **Player** (11 connections)
- **Protocol** (9 connections)
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_processing.py`
- **UUID** (8 connections)
- **_TickDeathService** (6 connections) — `server/app/game_tick_processing.py`
- **_TickCombatService** (4 connections) — `server/app/game_tick_processing.py`
- **_TickMpRegen** (4 connections) — `server/app/game_tick_processing.py`
- **_TickConnectionManager** (3 connections) — `server/app/game_tick_processing.py`
- **_TickEventBus** (3 connections) — `server/app/game_tick_processing.py`
- **_TickMagicService** (3 connections) — `server/app/game_tick_processing.py`
- **_TickNpcLifecycle** (3 connections) — `server/app/game_tick_processing.py`
- **_TickRespawnService** (3 connections) — `server/app/game_tick_processing.py`
- **.get_combat_by_participant()** (3 connections) — `server/app/game_tick_processing.py`
- **.get_dead_players()** (3 connections) — `server/app/game_tick_processing.py`
- **.get_mortally_wounded_players()** (3 connections) — `server/app/game_tick_processing.py`
- **.handle_player_death()** (3 connections) — `server/app/game_tick_processing.py`
- **.process_mortally_wounded_tick()** (3 connections) — `server/app/game_tick_processing.py`
- **.move_player_to_limbo()** (3 connections) — `server/app/game_tick_processing.py`
- **test_process_mortally_wounded_death_threshold()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_mortally_wounded_skips_active_combat()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **.send_personal_message()** (2 connections) — `server/app/game_tick_processing.py`
- **.process_tick_regeneration()** (2 connections) — `server/app/game_tick_processing.py`
- **.process_game_tick()** (1 connections) — `server/app/game_tick_processing.py`
- *... and 5 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (24 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (7 shared connections)
- [_process_mp_regeneration](_process_mp_regeneration.md) (2 shared connections)
- [coerce_int](coerce_int.md) (2 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 81 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*