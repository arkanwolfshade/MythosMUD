# PlayerService

> 635 nodes

## Key Concepts

- **PlayerService** (137 connections) — `server/game/player_service.py`
- **TargetMatch** (121 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (92 connections) — `server/models/spell.py`
- **SpellEffects** (54 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **player_service.py** (44 connections) — `server/game/player_service.py`
- **magic_service.py** (40 connections) — `server/game/magic/magic_service.py`
- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects.py** (38 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **SpellLearningService** (37 connections) — `server/game/magic/spell_learning_service.py`
- **PlayerSpellRepository** (37 connections) — `server/persistence/repositories/player_spell_repository.py`
- **lifespan_magic.py** (35 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (34 connections) — `server/game/magic/spell_registry.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **MagicService** (29 connections) — `server/game/magic/magic_service.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **SpellEffectsDeps** (25 connections) — `server/game/magic/spell_effects.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **asyncio** (23 connections)
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- *... and 610 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (158 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (51 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (47 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (29 shared connections)
- [Player](Player.md) (19 shared connections)
- [PlayerRead](PlayerRead.md) (19 shared connections)
- [MagicServiceCompletionMixin](MagicServiceCompletionMixin.md) (15 shared connections)
- [players.py](players.py.md) (15 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (13 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (13 shared connections)
- [run_flee_effect](run_flee_effect.md) (12 shared connections)
- [DatabaseError](DatabaseError.md) (12 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/app/lifespan_startup.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/container/main.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`

## Audit Trail

- EXTRACTED: 1694 (91%)
- INFERRED: 169 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*