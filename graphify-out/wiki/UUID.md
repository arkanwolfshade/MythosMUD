# UUID

> 14 nodes

## Key Concepts

- **UUID** (7 connections)
- **_TickDeathService** (6 connections) — `server/app/game_tick_protocols.py`
- **AsyncSession** (5 connections)
- **_TickCombatService** (4 connections) — `server/app/game_tick_protocols.py`
- **.get_combat_by_participant()** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_dead_players()** (3 connections) — `server/app/game_tick_protocols.py`
- **.get_mortally_wounded_players()** (3 connections) — `server/app/game_tick_protocols.py`
- **.handle_player_death()** (3 connections) — `server/app/game_tick_protocols.py`
- **.process_mortally_wounded_tick()** (3 connections) — `server/app/game_tick_protocols.py`
- **.move_player_to_limbo()** (3 connections) — `server/app/game_tick_protocols.py`
- **.send_personal_message()** (2 connections) — `server/app/game_tick_protocols.py`
- **.process_tick_regeneration()** (2 connections) — `server/app/game_tick_protocols.py`
- **Player** (2 connections)
- **.process_game_tick()** (1 connections) — `server/app/game_tick_protocols.py`

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (8 shared connections)
- [CombatInstance](CombatInstance.md) (1 shared connections)

## Source Files

- `server/app/game_tick_protocols.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*