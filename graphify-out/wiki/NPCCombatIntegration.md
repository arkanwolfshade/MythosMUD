# NPCCombatIntegration

> 106 nodes

## Key Concepts

- **NPCCombatIntegration** (99 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (46 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_combat_integration_base.py** (24 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **asyncio** (13 connections)
- **asyncio** (11 connections)
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **._get_npc_display_name()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/npc/combat_integration.py`
- **test_apply_combat_effects_validation_error()** (5 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **integration()** (5 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **.get_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_npc_name_from_lifecycle()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **integration()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_attribute_error_raises()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_get_combat_stats_for_player()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_get_combat_stats_npc_only_normalized()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_handle_npc_death_with_killer_applies_mechanics()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_publish_attack_event_emits_npc_attacked()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **._derive_npc_name_from_id()** (3 connections) — `server/npc/combat_integration.py`
- **._normalize_npc_stats()** (3 connections) — `server/npc/combat_integration.py`
- **._publish_attack_event()** (3 connections) — `server/npc/combat_integration.py`
- **test_apply_combat_effects_grace_period_blocks_damage()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_invalid_uuid_raises()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_npc_target()** (3 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- *... and 81 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (14 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (13 shared connections)
- [EventBus](EventBus.md) (4 shared connections)
- [NPCDefinition](NPCDefinition.md) (3 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (2 shared connections)
- [.state](state.md) (2 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/combat_integration_base.py`
- `server/tests/unit/npc/test_combat_integration_base.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 176 (72%)
- INFERRED: 68 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*