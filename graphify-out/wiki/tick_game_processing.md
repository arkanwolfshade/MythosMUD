# tick game processing

> 127 nodes

## Key Concepts

- **game_tick_processing.py** (68 connections) — `server/app/game_tick_processing.py`
- **test_game_tick_processing_async.py** (26 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (16 connections)
- **test_game_tick_processing.py** (15 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **_process_damage_over_time_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_heal_over_time_effect()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_session_dp_decay_and_death()** (8 connections) — `server/app/game_tick_processing.py`
- **Any** (7 connections)
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (7 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_processing.py`
- **UUID** (6 connections)
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (6 connections)
- *... and 102 more nodes in this community*

## Relationships

- [command utility models](command_utility_models.md) (9 shared connections)
- [time service rationale](time_service_rationale.md) (8 shared connections)
- [command inventory factories](command_inventory_factories.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (6 shared connections)
- [Item Instances](Item_Instances.md) (4 shared connections)
- [container events rationale](container_events_rationale.md) (4 shared connections)
- [npc combat services](npc_combat_services.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (3 shared connections)
- [game models player](game_models_player.md) (3 shared connections)
- [item models rationale](item_models_rationale.md) (2 shared connections)
- [models player rationale](models_player_rationale.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 504 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*