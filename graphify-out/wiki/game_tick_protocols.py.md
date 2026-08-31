# game_tick_protocols.py

> 29 nodes

## Key Concepts

- **game_tick_protocols.py** (30 connections) — `server/app/game_tick_protocols.py`
- **_app_container()** (13 connections) — `server/app/game_tick_protocols.py`
- **Protocol** (9 connections)
- **UUID** (9 connections)
- **_TickDeathService** (6 connections) — `server/app/game_tick_protocols.py`
- **_TickCombatService** (5 connections) — `server/app/game_tick_protocols.py`
- **_TickMpRegen** (5 connections) — `server/app/game_tick_protocols.py`
- **AsyncSession** (5 connections)
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
- **.publish_player_dp_decay_event_to_nats()** (2 connections) — `server/app/game_tick_protocols.py`
- **.send_personal_message()** (2 connections) — `server/app/game_tick_protocols.py`
- **.process_tick_regeneration()** (2 connections) — `server/app/game_tick_protocols.py`
- **FastAPI** (2 connections)
- **Player** (2 connections)
- **.process_game_tick()** (1 connections) — `server/app/game_tick_protocols.py`
- **.publish()** (1 connections) — `server/app/game_tick_protocols.py`
- *... and 4 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (10 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (8 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (5 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (2 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [event_types.py](event_types.py.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (1 shared connections)
- [service.py](service.py.md) (1 shared connections)

## Source Files

- `server/app/game_tick_protocols.py`

## Audit Trail

- EXTRACTED: 83 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*