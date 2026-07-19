# Magic Service Bundle

> 129 nodes · cohesion 0.04

## Key Concepts

- **PlayerSpellRepository** (66 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (52 connections) — `server/game/magic/spell_registry.py`
- **MagicService** (48 connections) — `server/game/magic/magic_service.py`
- **SpellLearningService** (48 connections) — `server/game/magic/spell_learning_service.py`
- **_MagicServiceCore** (42 connections) — `server/game/magic/magic_service.py`
- **SpellTargetingService** (36 connections) — `server/game/magic/spell_targeting.py`
- **UUID** (33 connections) — `server/game/magic/magic_service.py`
- **Any** (31 connections) — `server/game/magic/magic_service.py`
- **CastingStateManager** (28 connections) — `server/game/magic/casting_state_manager.py`
- **MagicServiceCompletionMixin** (28 connections) — `server/game/magic/magic_service_completion.py`
- **SpellCostsService** (24 connections) — `server/game/magic/spell_costs.py`
- **magic_service.py** (23 connections) — `server/game/magic/magic_service.py`
- **MagicServiceHealingMixin** (22 connections) — `server/game/magic/magic_healing_events.py`
- **SpellMaterialsService** (22 connections) — `server/game/magic/spell_materials.py`
- **SpellRepository** (19 connections) — `server/persistence/repositories/spell_repository.py`
- **Spell** (19 connections) — `server/game/magic/magic_service.py`
- **magic.py** (17 connections) — `server/container/bundles/magic.py`
- **MagicServiceOptionalDeps** (17 connections) — `server/game/magic/magic_service.py`
- **MagicBundle** (16 connections) — `server/container/bundles/magic.py`
- **ApplicationContainer** (14 connections) — `server/container/bundles/magic.py`
- **PlayerService** (14 connections) — `server/game/magic/magic_service.py`
- **SpellRegistry** (14 connections) — `server/game/magic/magic_service.py`
- **SpellEffects** (14 connections) — `server/game/magic/magic_service.py`
- **SpellTargetingService** (14 connections) — `server/game/magic/magic_service.py`
- **_create_registry_and_targeting()** (13 connections) — `server/container/bundles/magic.py`
- *... and 104 more nodes in this community*

## Relationships

- [[Spell Registry Costs]] (47 shared connections)
- [[Spell Effect Protocols]] (29 shared connections)
- [[Combat Service Bundle]] (28 shared connections)
- [[Combat Command Handler]] (27 shared connections)
- [[Magic Game Service]] (25 shared connections)
- [[Game Magic Spell]] (21 shared connections)
- [[NPC Admin API]] (20 shared connections)
- [[Magic Command Handlers]] (20 shared connections)
- [[Magic Lifespan Initialization]] (14 shared connections)
- [[Application DI Bundles]] (8 shared connections)
- [[Game Magic Casting]] (8 shared connections)
- [[MP Regeneration Service]] (6 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`

## Audit Trail

- EXTRACTED: 555 (55%)
- INFERRED: 457 (45%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
