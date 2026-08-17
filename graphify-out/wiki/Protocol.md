# Protocol

> 28 nodes

## Key Concepts

- **Protocol** (9 connections)
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_death.py`
- **UUID** (7 connections)
- **_TickDeathService** (6 connections) — `server/app/game_tick_protocols.py`
- **_TickMpRegen** (6 connections) — `server/app/game_tick_protocols.py`
- **_regenerate_mp_for_players()** (6 connections) — `server/app/game_tick_death.py`
- **AsyncSession** (5 connections)
- **_TickCombatService** (4 connections) — `server/app/game_tick_protocols.py`
- **_TickEventBus** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickMagicService** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickNpcLifecycle** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickRespawnService** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_combat_by_participant()** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_dead_players()** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_mortally_wounded_players()** (3 connections) — `server/app/game_tick_protocols.py`
- **.handle_player_death()** (3 connections) — `server/app/game_tick_protocols.py`
- **.process_mortally_wounded_tick()** (3 connections) — `server/app/game_tick_protocols.py`
- **.move_player_to_limbo()** (3 connections) — `server/app/game_tick_protocols.py`
- **.send_personal_message()** (2 connections) — `server/app/game_tick_protocols.py`
- **.process_tick_regeneration()** (2 connections) — `server/app/game_tick_protocols.py`
- **UUID** (2 connections)
- **Player** (2 connections)
- **.process_game_tick()** (1 connections) — `server/app/game_tick_protocols.py`
- **.publish()** (1 connections) — `server/app/game_tick_protocols.py`
- **.check_casting_progress()** (1 connections) — `server/app/game_tick_protocols.py`
- *... and 3 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (13 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [coerce_int](coerce_int.md) (1 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (1 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_protocols.py`

## Audit Trail

- EXTRACTED: 56 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*