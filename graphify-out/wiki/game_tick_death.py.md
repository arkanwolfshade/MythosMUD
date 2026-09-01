# game_tick_death.py

> 39 nodes

## Key Concepts

- **game_tick_death.py** (35 connections) — `server/app/game_tick_death.py`
- **game_tick_protocols.py** (30 connections) — `server/app/game_tick_protocols.py`
- **_TickContainer** (23 connections) — `server/app/game_tick_protocols.py`
- **_process_mortally_wounded_player()** (14 connections) — `server/app/game_tick_death.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (9 connections) — `server/app/game_tick_death.py`
- **Protocol** (9 connections)
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_death.py`
- **_online_player_ids()** (8 connections) — `server/app/game_tick_protocols.py`
- **_process_dead_players()** (7 connections) — `server/app/game_tick_death.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_death.py`
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_death.py`
- **AsyncSession** (7 connections)
- **_process_mortally_wounded_players()** (6 connections) — `server/app/game_tick_death.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_death.py`
- **_TickMpRegen** (5 connections) — `server/app/game_tick_protocols.py`
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_death.py`
- **_TickEventBus** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickMagicService** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickNpcLifecycle** (3 connections) — `server/app/game_tick_protocols.py`
- **_TickRespawnService** (3 connections) — `server/app/game_tick_protocols.py`
- **Player** (3 connections)
- **FastAPI** (2 connections)
- **.publish()** (1 connections) — `server/app/game_tick_protocols.py`
- **.check_casting_progress()** (1 connections) — `server/app/game_tick_protocols.py`
- *... and 14 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (15 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (13 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (9 shared connections)
- [UUID](UUID.md) (8 shared connections)
- [event_types.py](event_types.py.md) (7 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [coerce_int](coerce_int.md) (5 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (4 shared connections)
- [Player](Player.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_protocols.py`

## Audit Trail

- EXTRACTED: 147 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*