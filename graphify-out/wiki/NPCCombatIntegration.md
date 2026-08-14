# NPCCombatIntegration

> 31 nodes

## Key Concepts

- **NPCCombatIntegration** (103 connections) — `server/npc/combat_integration.py`
- **test_combat_integration_base.py** (24 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **asyncio** (11 connections)
- **_resolve_npc_combat_service_raw()** (7 connections) — `server/npc/combat_integration_base.py`
- **integration()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_attribute_error_raises()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_validation_error()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
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
- **._get_npc_stats()** (2 connections) — `server/npc/combat_integration.py`
- **.handle_npc_death()** (2 connections) — `server/npc/combat_integration.py`
- **test_calculate_damage_minimum_on_bad_stats()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_calculate_damage_with_stats()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_convert_target_id_to_uuid()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_unexpected_error_logs()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_resolve_npc_combat_service_from_container()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **fixture** (1 connections)
- *... and 6 more nodes in this community*

## Relationships

- [test_npc_combat_integration_class.py](test_npc_combat_integration_class.py.md) (38 shared connections)
- [EventBus](EventBus.md) (10 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (10 shared connections)
- [event_types.py](event_types.py.md) (4 shared connections)
- [._get_npc_display_name](_get_npc_display_name.md) (4 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [AggressiveMobNPC](AggressiveMobNPC.md) (3 shared connections)
- [.get_combat_stats](get_combat_stats.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [combat_attack.py](combat_attack.py.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/npc/combat_integration_base.py`
- `server/tests/unit/npc/test_combat_integration_base.py`

## Audit Trail

- EXTRACTED: 139 (92%)
- INFERRED: 12 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*