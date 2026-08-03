# npc spawn validator

> 94 nodes

## Key Concepts

- **PopulationStats** (42 connections) — `server/npc/population_stats.py`
- **test_population_stats.py** (23 connections) — `server/tests/unit/npc/test_population_stats.py`
- **_PopulationLifecycleManager** (13 connections) — `server/npc/population_control.py`
- **._should_spawn_npc()** (8 connections) — `server/npc/population_control.py`
- **.__init__()** (7 connections) — `server/npc/population_control.py`
- **._check_spawn_requirements_for_room()** (7 connections) — `server/npc/population_control.py`
- **._spawn_npc()** (7 connections) — `server/npc/population_control.py`
- **._register_spawned_npc_in_population_stats()** (6 connections) — `server/npc/population_control.py`
- **._handle_player_entered_room()** (5 connections) — `server/npc/population_control.py`
- **._get_zone_key_from_room_id()** (5 connections) — `server/npc/population_control.py`
- **test_should_spawn_npc()** (5 connections) — `server/tests/unit/npc/test_population_control.py`
- **.spawn_npc()** (4 connections) — `server/npc/population_control.py`
- **._load_zone_configurations()** (4 connections) — `server/npc/population_control.py`
- **._handle_player_left_room()** (4 connections) — `server/npc/population_control.py`
- **._update_player_count()** (4 connections) — `server/npc/population_control.py`
- **.get_zone_configuration()** (4 connections) — `server/npc/population_control.py`
- **.get_population_stats()** (4 connections) — `server/npc/population_control.py`
- **.clear_population_stats()** (3 connections) — `server/npc/population_control.py`
- **.to_dict()** (3 connections) — `server/npc/population_stats.py`
- **test_get_population_stats_existing()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_clear_population_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_population_summary_with_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_despawn_npc_success()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_population_stats_init()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- **test_add_npc_required()** (3 connections) — `server/tests/unit/npc/test_population_stats.py`
- *... and 69 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (30 shared connections)
- [item models rationale](item_models_rationale.md) (7 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (6 shared connections)
- [spell game magic](spell_game_magic.md) (5 shared connections)
- [combat services rationale](combat_services_rationale.md) (3 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)

## Source Files

- `server/npc/population_control.py`
- `server/npc/population_stats.py`
- `server/tests/unit/npc/test_population_control.py`
- `server/tests/unit/npc/test_population_stats.py`

## Audit Trail

- EXTRACTED: 269 (95%)
- INFERRED: 13 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*