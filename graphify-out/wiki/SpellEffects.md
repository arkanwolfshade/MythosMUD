# SpellEffects

> 179 nodes

## Key Concepts

- **SpellEffects** (55 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (47 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **asyncio** (29 connections)
- **test_damage_grace_period.py** (28 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **SpellEffectsDeps** (20 connections) — `server/game/magic/spell_effects.py`
- **MPRegenerationService** (18 connections) — `server/game/magic/mp_regeneration_service.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **test_negative_status_effect_blocked_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_positive_status_effect_allowed_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- *... and 154 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (59 shared connections)
- [SpellEffectType](SpellEffectType.md) (24 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [magic_service.py](magic_service.py.md) (17 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (14 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (12 shared connections)
- [SpellLearningService](SpellLearningService.md) (10 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (5 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 460 (87%)
- INFERRED: 71 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*