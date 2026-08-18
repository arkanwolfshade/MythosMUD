# server npc combat integration npccombatintegration

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

- [server tests unit npc test](server_tests_unit_npc_test.md) (19 shared connections)
- [server npc combat integration npccombatintegration](server_npc_combat_integration_npccombatintegration.md) (19 shared connections)
- [server npc combat integration base](server_npc_combat_integration_base.md) (17 shared connections)
- [server npc npc base npcbase](server_npc_npc_base_npcbase.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server config init](server_config_init.md) (5 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (4 shared connections)
- [server commands combat attack](server_commands_combat_attack.md) (2 shared connections)
- [server models combat](server_models_combat.md) (1 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)
- [server realtime integration game state](server_realtime_integration_game_state.md) (1 shared connections)
- [object](object.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 105 (63%)
- INFERRED: 62 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*