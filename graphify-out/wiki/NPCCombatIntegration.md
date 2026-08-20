# NPCCombatIntegration

> 42 nodes

## Key Concepts

- **NPCCombatIntegration** (99 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (47 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **asyncio** (13 connections)
- **test_get_combat_stats_for_player()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_npc_only_normalized()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_with_killer_applies_mechanics()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_attack_event_emits_npc_attacked()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_entity_not_found()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_error_without_npc_stats()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_int_stat_parses_numeric_string()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_reads_active_instance()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_npc_name_from_lifecycle_returns_none_when_missing()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_player_and_stats_for_nats_missing_player()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_player_combat_stats_string_and_invalid_dp()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_invalid_killer_returns_false()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_npc_attack_to_nats_no_publisher()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_npc_attack_to_nats_success()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_npc_attack_to_nats_swallows_errors()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_player_dp_updated_after_npc_damage()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_player_dp_updated_skips_without_player_or_bus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_player_dp_updated_swallows_errors()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_build_player_attacked_event_uses_dp_fallback()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_max_dp_from_max_health()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_compute_dp_update_fields_non_dict_stats()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_event_publisher_from_container()** (2 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 17 more nodes in this community*

## Relationships

- [test_combat_integration_base.py](test_combat_integration_base.py.md) (17 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (9 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (7 shared connections)
- [NATSError](NATSError.md) (4 shared connections)
- [._get_npc_display_name](_get_npc_display_name.md) (4 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [integration](integration.md) (3 shared connections)
- [.get_combat_stats](get_combat_stats.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [combat_attack.py](combat_attack.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (2 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 105 (63%)
- INFERRED: 62 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*