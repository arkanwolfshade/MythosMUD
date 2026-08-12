# test_npc_combat_integration_class.py

> 54 nodes

## Key Concepts

- **test_npc_combat_integration_class.py** (23 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **NPCAttacked** (11 connections) — `server/events/event_types.py`
- **integration()** (7 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **._attack_target_impl()** (6 connections) — `server/npc/aggressive_mob_npc.py`
- **.attack_target()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **._attack_via_combat_integration()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **test_get_combat_stats_for_player()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_npc_only_normalized()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_with_killer_applies_mechanics()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **.__post_init__()** (3 connections) — `server/events/event_types.py`
- **._get_attack_damage()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_attack_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_damage_physical_strength_bonus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_damage_weapon_type_no_strength_bonus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_max_dp_from_constitution_and_size()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_compute_dp_update_fields()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_derive_npc_name_from_id()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_int_stat_parses_numeric_string()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_reads_active_instance()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_returns_none_when_missing()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_stats_defaults()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_stats_preserves_values()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_normalize_npc_stats_adds_hp_from_determination_points()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 29 more nodes in this community*

## Relationships

- [get_npc_instance_service](get_npc_instance_service.md) (22 shared connections)
- [EventBus](EventBus.md) (9 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (2 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)
- [.__post_init__](__post_init__.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/npc/aggressive_mob_npc.py`
- `server/npc/combat_integration.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 149 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*