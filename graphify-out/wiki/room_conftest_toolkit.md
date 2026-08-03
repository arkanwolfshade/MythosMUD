# room conftest toolkit

> 21 nodes

## Key Concepts

- **test_combat_integration_base.py** (24 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **integration()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_validation_error()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_attribute_error_raises()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_resolve_npc_combat_service_from_container()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_calculate_damage_minimum_on_bad_stats()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_npc_target()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_invalid_uuid_raises()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_player()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_convert_target_id_to_uuid()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_unexpected_error_logs()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_is_target_in_login_grace_period_false()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_grace_period_blocks_damage()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_mental_effects_occult()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_npc_attack_direct_path()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_calculate_damage_with_stats()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_perform_direct_npc_attack()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_npc_attack_delegated()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **Return the live NPC combat integration service for delegation.      Prefer ``C** (1 connections) — `server/npc/combat_integration_base.py`
- **Unit tests for NPCCombatIntegrationBase helpers.** (1 connections) — `server/tests/unit/npc/test_combat_integration_base.py`

## Relationships

- [services nats service](services_nats_service.md) (17 shared connections)
- [npc combat base](npc_combat_base.md) (3 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (3 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)
- [command commands aliases](command_commands_aliases.md) (1 shared connections)
- [command inventory models](command_inventory_models.md) (1 shared connections)
- [health service services](health_service_services.md) (1 shared connections)
- [look helpers commands](look_helpers_commands.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration_base.py`
- `server/tests/unit/npc/test_combat_integration_base.py`

## Audit Trail

- EXTRACTED: 66 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*