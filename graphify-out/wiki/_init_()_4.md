# . init ()

> 193 nodes

## Key Concepts

- **magic_service.py** (39 connections) — `server/game/magic/magic_service.py`
- **PlayerSpellRepository** (36 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (35 connections) — `server/game/magic/spell_registry.py`
- **lifespan_magic.py** (34 connections) — `server/app/lifespan_magic.py`
- **SpellLearningService** (30 connections) — `server/game/magic/spell_learning_service.py`
- **MagicService** (29 connections) — `server/game/magic/magic_service.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **SpellTargetingService** (25 connections) — `server/game/magic/spell_targeting.py`
- **MagicServiceCompletionMixin** (21 connections) — `server/game/magic/magic_service_completion.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **magic.py** (19 connections) — `server/container/bundles/magic.py`
- **MagicBundle** (18 connections) — `server/container/bundles/magic.py`
- **CastingStateManager** (18 connections) — `server/game/magic/casting_state_manager.py`
- **MagicServiceOptionalDeps** (17 connections) — `server/game/magic/magic_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **SpellRepository** (14 connections) — `server/persistence/repositories/spell_repository.py`
- **spell_targeting.py** (14 connections) — `server/game/magic/spell_targeting.py`
- **_initialize_magic_service()** (13 connections) — `server/app/lifespan_magic.py`
- **_create_registry_and_targeting()** (13 connections) — `server/container/bundles/magic.py`
- **SpellCommandError** (12 connections) — `server/commands/magic_commands.py`
- **UUID** (12 connections)
- **spell_costs.py** (12 connections) — `server/game/magic/spell_costs.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **Any** (11 connections)
- *... and 168 more nodes in this community*

## Relationships

- [Spell Targeting](Spell_Targeting.md) (39 shared connections)
- [main()](main%28%29.md) (36 shared connections)
- [Connection Manager](Connection_Manager.md) (19 shared connections)
- [Any](Any.md) (19 shared connections)
- [spell registry](spell_registry.md) (16 shared connections)
- [.shutdown()](shutdown%28%29.md) (14 shared connections)
- [. init ()](_init_%28%29.md) (12 shared connections)
- [MagicServiceCore](MagicServiceCore.md) (11 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (11 shared connections)
- [Player Position Service](Player_Position_Service.md) (7 shared connections)
- [UUID](UUID.md) (7 shared connections)
- [MPRegenerationService](MPRegenerationService.md) (5 shared connections)

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
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`

## Audit Trail

- EXTRACTED: 856 (87%)
- INFERRED: 130 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*