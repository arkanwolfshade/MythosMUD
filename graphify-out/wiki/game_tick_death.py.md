# game_tick_death.py

> 67 nodes

## Key Concepts

- **game_tick_death.py** (48 connections) — `server/app/game_tick_death.py`
- **test_game_tick_death.py** (40 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **asyncio** (21 connections)
- **_process_mortally_wounded_player()** (16 connections) — `server/app/game_tick_death.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **_process_passive_corruption_flux()** (11 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **_tick_online_players()** (10 connections) — `server/app/game_tick_protocols.py`
- **_handle_player_death_threshold()** (9 connections) — `server/app/game_tick_death.py`
- **_process_mortally_wounded_players()** (9 connections) — `server/app/game_tick_death.py`
- **_process_single_player_room_flux()** (9 connections) — `server/app/game_tick_death.py`
- **AsyncSession** (8 connections)
- **_process_dead_players()** (7 connections) — `server/app/game_tick_death.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_death.py`
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_death.py`
- **_create_bleed_out_corpse()** (6 connections) — `server/app/game_tick_death.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_death.py`
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_death.py`
- **_bleed_out_setup()** (5 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_bleed_out_corpse_failure_does_not_abort_the_death_sequence()** (5 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_mortally_wounded_decay_runs_once_per_second()** (5 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **_dp_decay_due()** (4 connections) — `server/app/game_tick_death.py`
- **test_bleed_out_without_persistence_skips_corpse_but_still_moves_to_limbo()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_game_tick_loop_survives_unanticipated_exception()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_death_threshold()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- *... and 42 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (30 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (25 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [CombatService](CombatService.md) (8 shared connections)
- [coerce_int](coerce_int.md) (6 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (2 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (2 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_protocols.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 217 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*