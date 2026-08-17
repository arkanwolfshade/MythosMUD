# NPCCombatIntegration

> 89 nodes

## Key Concepts

- **NPCCombatIntegration** (99 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (47 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_combat_integration_base.py** (25 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **asyncio** (13 connections)
- **asyncio** (11 connections)
- **test_apply_combat_effects_validation_error()** (5 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **integration()** (5 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **integration()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_attribute_error_raises()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_get_combat_stats_for_player()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_npc_only_normalized()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_with_killer_applies_mechanics()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_attack_event_emits_npc_attacked()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration.py`
- **test_apply_combat_effects_grace_period_blocks_damage()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_invalid_uuid_raises()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_npc_target()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_player()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_mental_effects_occult()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_npc_attack_delegated()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_npc_attack_direct_path()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_is_target_in_login_grace_period_false()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_perform_direct_npc_attack()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_calculate_damage_physical_strength_bonus()** (3 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 64 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (24 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (13 shared connections)
- [._get_npc_display_name](_get_npc_display_name.md) (4 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)
- [combat_attack.py](combat_attack.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [test_damage_grace_period.py](test_damage_grace_period.py.md) (2 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [AttributeError](AttributeError.md) (1 shared connections)
- [test_command_service.py](test_command_service.py.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/tests/unit/npc/test_combat_integration_base.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 155 (69%)
- INFERRED: 69 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*