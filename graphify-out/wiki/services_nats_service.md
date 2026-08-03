# services nats service

> 59 nodes

## Key Concepts

- **NPCCombatIntegration** (103 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (46 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **integration()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_attack_event_emits_npc_attacked()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_stats_defaults()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_stats_preserves_values()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_derive_npc_name_from_id()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_damage_physical_strength_bonus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_damage_weapon_type_no_strength_bonus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_int_stat_parses_numeric_string()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_max_dp_from_constitution_and_size()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_normalize_npc_stats_adds_hp_from_determination_points()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_for_player()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_npc_only_normalized()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_with_killer_applies_mechanics()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_compute_dp_update_fields()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_reads_active_instance()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_returns_none_when_missing()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_display_name_prefers_lifecycle()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_display_name_falls_back_to_id()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_lifecycle_manager_from_config()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_lifecycle_manager_missing_app()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_swallows_errors()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_player_dp_updated_after_npc_damage()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_player_dp_updated_skips_without_player_or_bus()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 34 more nodes in this community*

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (21 shared connections)
- [room conftest toolkit](room_conftest_toolkit.md) (17 shared connections)
- [message queue realtime](message_queue_realtime.md) (14 shared connections)
- [schemas items item](schemas_items_item.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [attack combat commands](attack_combat_commands.md) (2 shared connections)
- [npc combat base](npc_combat_base.md) (2 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [lucidity event services](lucidity_event_services.md) (1 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)
- [combat commands handler](combat_commands_handler.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 254 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*