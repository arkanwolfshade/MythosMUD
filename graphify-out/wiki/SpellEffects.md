# SpellEffects

> 147 nodes

## Key Concepts

- **SpellEffects** (55 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (47 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **asyncio** (29 connections)
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **SpellEffectsDeps** (20 connections) — `server/game/magic/spell_effects.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **test_negative_status_effect_blocked_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_positive_status_effect_allowed_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- *... and 122 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (50 shared connections)
- [get_logger](get_logger.md) (22 shared connections)
- [SpellEffectType](SpellEffectType.md) (20 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (11 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (10 shared connections)
- [SpellLearningService](SpellLearningService.md) (8 shared connections)
- [test_player_spell_repository.py](test_player_spell_repository.py.md) (7 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (7 shared connections)
- [spell_repository.py](spell_repository.py.md) (6 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (6 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (5 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 384 (84%)
- INFERRED: 73 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*