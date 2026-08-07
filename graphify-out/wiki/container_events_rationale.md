# container events rationale

> 98 nodes

## Key Concepts

- **test_population_control.py** (65 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_should_spawn_npc()** (5 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_check_spawn_requirements_for_room_with_definitions()** (4 connections) — `server/tests/unit/npc/test_population_control.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **population_controller()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_population_controller_init()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_population_controller_init_requires_async_persistence()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_load_npc_definitions()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_load_npc_definitions_overwrites()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_load_spawn_rules()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_exact_match()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_zone_fallback()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_configuration_no_slash()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_population_stats_existing()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_clear_population_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_get_zone_population_summary_with_stats()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_player_entered_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_player_left_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_npc_entered_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_handle_npc_left_room()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_spawn_npc_no_lifecycle_manager()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_spawn_npc_success()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_spawn_npc_spawn_fails()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_spawn_npc_handles_exception()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- **test_spawn_npc_public_api()** (3 connections) — `server/tests/unit/npc/test_population_control.py`
- *... and 73 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (22 shared connections)
- [room look commands](room_look_commands.md) (13 shared connections)
- [spell game magic](spell_game_magic.md) (7 shared connections)
- [inventory mutation guard](inventory_mutation_guard.md) (2 shared connections)

## Source Files

- `server/tests/unit/npc/test_population_control.py`

## Audit Trail

- EXTRACTED: 227 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*