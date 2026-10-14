# SpellEffects

> 150 nodes

## Key Concepts

- **SpellEffects** (63 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (58 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (50 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **asyncio** (30 connections)
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **SpellEffectsDeps** (22 connections) — `server/game/magic/spell_effects.py`
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **test_process_teleport_into_instance_template_fails_cleanly()** (7 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_negative_status_effect_blocked_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_positive_status_effect_allowed_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Protocol** (7 connections)
- **NpcIntegrationStringIdPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **NpcLifecycleManagerPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **test_process_effect_flee_not_in_combat()** (6 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_publish_npc_spell_damage_syncs_participant_when_npc_room_missing()** (6 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **PlayerServiceHealPort** (5 connections) — `server/game/magic/spell_effect_types.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_effects.py`
- **spell_effects()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **test_process_damage_to_npc_success()** (5 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- *... and 125 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (70 shared connections)
- [get_logger](get_logger.md) (27 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (20 shared connections)
- [SpellEffectType](SpellEffectType.md) (16 shared connections)
- [CombatService](CombatService.md) (11 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (11 shared connections)
- [test_utility_threat.py](test_utility_threat.py.md) (7 shared connections)
- [magic_service.py](magic_service.py.md) (6 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [TargetType](TargetType.md) (5 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [SpellLearningService](SpellLearningService.md) (4 shared connections)

## Source Files

- `server/container/bundles/magic.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 409 (88%)
- INFERRED: 58 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*