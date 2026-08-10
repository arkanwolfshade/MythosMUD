# NPC Service Tests

> 294 nodes

## Key Concepts

- **Spell** (93 connections) — `server/models/spell.py`
- **SpellEffects** (56 connections) — `server/game/magic/spell_effects.py`
- **magic_service.py** (40 connections) — `server/game/magic/magic_service.py`
- **SpellLearningService** (38 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell_effects.py** (38 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **PlayerSpellRepository** (37 connections) — `server/persistence/repositories/player_spell_repository.py`
- **lifespan_magic.py** (35 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (35 connections) — `server/game/magic/spell_registry.py`
- **MagicService** (30 connections) — `server/game/magic/magic_service.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **SpellTargetingService** (29 connections) — `server/game/magic/spell_targeting.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **SpellEffectsDeps** (25 connections) — `server/game/magic/spell_effects.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- **spell_targeting.py** (20 connections) — `server/game/magic/spell_targeting.py`
- **MagicBundle** (19 connections) — `server/container/bundles/magic.py`
- **CastingStateManager** (18 connections) — `server/game/magic/casting_state_manager.py`
- **MagicServiceOptionalDeps** (18 connections) — `server/game/magic/magic_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **spell_registry.py** (15 connections) — `server/game/magic/spell_registry.py`
- **test_spell_targeting.py** (15 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **_create_registry_and_targeting()** (14 connections) — `server/container/bundles/magic.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- *... and 269 more nodes in this community*

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (89 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (30 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (22 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (21 shared connections)
- [Security Headers Middleware](Security_Headers_Middleware.md) (20 shared connections)
- [Client Event Store](Client_Event_Store.md) (17 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (14 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (14 shared connections)
- [Async Persistence Migration](Async_Persistence_Migration.md) (13 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (10 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (10 shared connections)
- [Quality Audit Report](Quality_Audit_Report.md) (9 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 1300 (88%)
- INFERRED: 173 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*