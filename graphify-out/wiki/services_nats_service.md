# services nats service

> 63 nodes

## Key Concepts

- **NPCCombatIntegration** (103 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (46 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **integration()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_attack_event_emits_npc_attacked()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **._normalize_npc_stats()** (3 connections) — `server/npc/combat_integration.py`
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
- **._get_npc_stats()** (2 connections) — `server/npc/combat_integration.py`
- **test_get_npc_display_name_prefers_lifecycle()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_display_name_falls_back_to_id()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_lifecycle_manager_from_config()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_lifecycle_manager_missing_app()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_swallows_errors()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 38 more nodes in this community*

## Relationships

- [command parser rationale](command_parser_rationale.md) (16 shared connections)
- [Error Conversion](Error_Conversion.md) (14 shared connections)
- [game weapon player](game_weapon_player.md) (12 shared connections)
- [lucidity event services](lucidity_event_services.md) (6 shared connections)
- [combat models rationale](combat_models_rationale.md) (4 shared connections)
- [catatonia registry services](catatonia_registry_services.md) (2 shared connections)
- [attack combat commands](attack_combat_commands.md) (2 shared connections)
- [add used user](add_used_user.md) (2 shared connections)
- [command utility models](command_utility_models.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [error logging rationale](error_logging_rationale.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 261 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*