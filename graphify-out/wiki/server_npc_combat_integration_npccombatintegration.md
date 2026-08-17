# server npc combat integration npccombatintegration

> 78 nodes

## Key Concepts

- **NPCCombatIntegration** (99 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (47 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_combat_integration_base.py** (25 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **asyncio** (13 connections)
- **asyncio** (11 connections)
- **test_apply_combat_effects_validation_error()** (5 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **integration()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_attribute_error_raises()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_get_combat_stats_for_player()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_npc_only_normalized()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_with_killer_applies_mechanics()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_attack_event_emits_npc_attacked()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_apply_combat_effects_grace_period_blocks_damage()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_invalid_uuid_raises()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_npc_target()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_player()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_mental_effects_occult()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_npc_attack_delegated()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_npc_attack_direct_path()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_is_target_in_login_grace_period_false()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_perform_direct_npc_attack()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_calculate_damage_physical_strength_bonus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_damage_weapon_type_no_strength_bonus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_max_dp_from_constitution_and_size()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_compute_dp_update_fields()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 53 more nodes in this community*

## Relationships

- [server npc combat integration npccombatintegration](server_npc_combat_integration_npccombatintegration.md) (20 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (10 shared connections)
- [server events event bus](server_events_event_bus.md) (7 shared connections)
- [server tests unit npc test](server_tests_unit_npc_test.md) (3 shared connections)
- [server npc combat integration base](server_npc_combat_integration_base.md) (3 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (2 shared connections)
- [server commands combat attack](server_commands_combat_attack.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (1 shared connections)
- [server npc init](server_npc_init.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/tests/unit/npc/test_combat_integration_base.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 146 (68%)
- INFERRED: 69 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*