# RoomService

> 160 nodes · cohesion 0.03

## Key Concepts

- **TargetMatch** (173 connections) — `server/schemas/shared/target_resolution.py`
- **spell_effects.py** (58 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **SpellEffectsEngineHealPort** (12 connections) — `server/game/magic/spell_effect_types.py`
- **asyncio** (12 connections)
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (10 connections)
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_resolve_target_dp()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_add_healing_threat_if_in_combat()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **coerce_effect_int_times_mastery()** (9 connections) — `server/game/magic/spell_effects_internal.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **_steal_life_publish_npc_events()** (8 connections) — `server/game/magic/spell_effects_heal.py`
- **combat_room_id_for_npc_spell()** (8 connections) — `server/game/magic/spell_effects_internal.py`
- **UUID** (8 connections)
- *... and 135 more nodes in this community*

## Relationships

- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (45 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (38 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (30 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (24 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (14 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (13 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (12 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (12 shared connections)
- [AsciiMapRenderer](AsciiMapRenderer.md) (10 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (8 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (7 shared connections)
- [test_item.py](test_item.py.md) (6 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 527 (89%)
- INFERRED: 62 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*