# NPCCombatIntegration

> 26 nodes

## Key Concepts

- **NPCCombatIntegration** (99 connections) — `server/npc/combat_integration.py`
- **test_combat_integration_base.py** (24 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **asyncio** (11 connections)
- **test_apply_combat_effects_validation_error()** (5 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **integration()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_apply_combat_effects_attribute_error_raises()** (4 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
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
- **.handle_npc_death()** (2 connections) — `server/npc/combat_integration.py`
- **test_calculate_damage_minimum_on_bad_stats()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_calculate_damage_with_stats()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_convert_target_id_to_uuid()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **test_handle_unexpected_error_logs()** (2 connections) — `server/tests/unit/npc/test_combat_integration_base.py`
- **fixture** (1 connections)
- **Publish NPC attack event to event bus.** (1 connections) — `server/npc/combat_integration.py`
- **Integrates NPCs with the existing combat and game mechanics systems. Extends…** (1 connections) — `server/npc/combat_integration.py`
- **Handle NPC death and related effects. Args: npc_id: ID of the dead NPC room_id:…** (1 connections) — `server/npc/combat_integration.py`
- *... and 1 more nodes in this community*

## Relationships

- [test_npc_combat_integration_class.py](test_npc_combat_integration_class.py.md) (31 shared connections)
- [get_logger](get_logger.md) (19 shared connections)
- [._build_player_attacked_event](_build_player_attacked_event.md) (10 shared connections)
- [test_publish_attack_event_emits_npc_attacked](test_publish_attack_event_emits_npc_attacked.md) (6 shared connections)
- [._get_npc_display_name](_get_npc_display_name.md) (4 shared connections)
- [.get_combat_stats](get_combat_stats.md) (3 shared connections)
- [combat_attack.py](combat_attack.py.md) (2 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [_resolve_npc_combat_service_raw](_resolve_npc_combat_service_raw.md) (2 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (1 shared connections)
- [._get_npc_stats](_get_npc_stats.md) (1 shared connections)
- [test_calculate_damage_physical_strength_bonus](test_calculate_damage_physical_strength_bonus.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`
- `server/tests/unit/npc/test_combat_integration_base.py`

## Audit Trail

- EXTRACTED: 74 (52%)
- INFERRED: 67 (48%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*