# server app game tick protocols

> 22 nodes

## Key Concepts

- **Protocol** (9 connections)
- **UUID** (7 connections)
- **_TickDeathService** (6 connections) — `server/app/game_tick_protocols.py`
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
- **Player** (2 connections)
- **.process_game_tick()** (1 connections) — `server/app/game_tick_protocols.py`
- **.publish()** (1 connections) — `server/app/game_tick_protocols.py`
- **.check_casting_progress()** (1 connections) — `server/app/game_tick_protocols.py`
- **.periodic_maintenance()** (1 connections) — `server/app/game_tick_protocols.py`
- **CombatInstance** (1 connections)

## Relationships

- [playerdpupdated](playerdpupdated.md) (10 shared connections)
- [server app game tick processing](server_app_game_tick_processing.md) (2 shared connections)

## Source Files

- `server/app/game_tick_protocols.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*