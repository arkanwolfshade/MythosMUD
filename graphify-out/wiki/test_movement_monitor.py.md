# test_movement_monitor.py

> 58 nodes

## Key Concepts

- **NPCCombatIntegration** (92 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (47 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **asyncio** (13 connections)
- **test_get_combat_stats_for_player()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_npc_only_normalized()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_with_killer_applies_mechanics()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_attack_event_emits_npc_attacked()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_damage_physical_strength_bonus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_damage_weapon_type_no_strength_bonus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_max_dp_from_constitution_and_size()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_compute_dp_update_fields()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_derive_npc_name_from_id()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_entity_not_found()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_error_without_npc_stats()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_int_stat_parses_numeric_string()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_reads_active_instance()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_returns_none_when_missing()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_stats_defaults()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_stats_preserves_values()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_player_and_stats_for_nats_missing_player()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_player_combat_stats_string_and_invalid_dp()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_invalid_killer_returns_false()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_normalize_npc_stats_adds_hp_from_determination_points()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_npc_attack_to_nats_no_publisher()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_npc_attack_to_nats_success()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 33 more nodes in this community*

## Relationships

- [PostgresCursor](PostgresCursor.md) (17 shared connections)
- [TestGracefulDegradation](TestGracefulDegradation.md) (10 shared connections)
- [NPCDefinition](NPCDefinition.md) (8 shared connections)
- [Invite](Invite.md) (6 shared connections)
- [Combat Client Crash](Combat_Client_Crash.md) (4 shared connections)
- [duration_hours](duration_hours.md) (3 shared connections)
- [A Cold Fire Within (source summary)](A_Cold_Fire_Within_source_summary.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [GameConfig](GameConfig.md) (1 shared connections)
- [id](id.md) (1 shared connections)
- [short_description](short_description.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 107 (64%)
- INFERRED: 61 (36%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*