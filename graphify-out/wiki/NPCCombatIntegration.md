# NPCCombatIntegration

> 125 nodes

## Key Concepts

- **NPCCombatIntegration** (99 connections) — `server/npc/combat_integration.py`
- **test_npc_combat_integration_class.py** (47 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **test_combat_integration_base.py** (25 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **asyncio** (13 connections)
- **asyncio** (11 connections)
- **._build_player_attacked_event()** (8 connections) — `server/npc/combat_integration.py`
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **._calculate_max_dp()** (6 connections) — `server/npc/combat_integration.py`
- **._compute_dp_update_fields()** (6 connections) — `server/npc/combat_integration.py`
- **._get_int_stat()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_display_name()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_npc_attack_to_nats()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_after_npc_damage()** (5 connections) — `server/npc/combat_integration.py`
- **._publish_player_dp_updated_event()** (5 connections) — `server/npc/combat_integration.py`
- **test_apply_combat_effects_validation_error()** (5 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **integration()** (5 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- **UUID** (5 connections)
- **.get_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_npc_name_from_lifecycle()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_and_stats_for_nats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_combat_stats()** (4 connections) — `server/npc/combat_integration.py`
- **._get_player_for_dp_update()** (4 connections) — `server/npc/combat_integration.py`
- **integration()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_attribute_error_raises()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_get_combat_stats_for_player()** (4 connections) — `server/tests/unit/npc/test_npc_combat_integration_class.py`
- *... and 100 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [EventBus](EventBus.md) (6 shared connections)
- [npc_base.py](npc_base.py.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [ConnectionManager](ConnectionManager.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [combat_attack.py](combat_attack.py.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/combat_integration_base.py`
- `server/npc/npc_base.py`
- `server/tests/unit/npc/test_combat_integration_base.py`
- `server/tests/unit/npc/test_npc_combat_integration_class.py`

## Audit Trail

- EXTRACTED: 201 (74%)
- INFERRED: 72 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*