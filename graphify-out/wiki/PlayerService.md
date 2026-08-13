# PlayerService

> 593 nodes

## Key Concepts

- **PlayerService** (137 connections) — `server/game/player_service.py`
- **Spell** (92 connections) — `server/models/spell.py`
- **SpellEffects** (54 connections) — `server/game/magic/spell_effects.py`
- **GameBundle** (45 connections) — `server/container/bundles/game.py`
- **player_service.py** (44 connections) — `server/game/player_service.py`
- **_MagicServiceCore** (43 connections) — `server/game/magic/magic_service.py`
- **bundles/game.py** (42 connections) — `server/container/bundles/game.py`
- **magic_service.py** (40 connections) — `server/game/magic/magic_service.py`
- **SpellLearningService** (37 connections) — `server/game/magic/spell_learning_service.py`
- **PlayerSpellRepository** (37 connections) — `server/persistence/repositories/player_spell_repository.py`
- **lifespan_magic.py** (35 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (34 connections) — `server/game/magic/spell_registry.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **MagicService** (29 connections) — `server/game/magic/magic_service.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **ScheduleService** (27 connections) — `server/services/schedule_service.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **MagicServiceCompletionMixin** (21 connections) — `server/game/magic/magic_service_completion.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- **UUID** (20 connections)
- **spell_targeting.py** (20 connections) — `server/game/magic/spell_targeting.py`
- **MagicBundle** (19 connections) — `server/container/bundles/magic.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- *... and 568 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (101 shared connections)
- [get_logger](get_logger.md) (76 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (60 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (42 shared connections)
- [log_and_raise](log_and_raise.md) (25 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (20 shared connections)
- [AliasStorage](AliasStorage.md) (19 shared connections)
- [PlayerRead](PlayerRead.md) (19 shared connections)
- [CombatService](CombatService.md) (18 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (17 shared connections)
- [ScheduleEntry](ScheduleEntry.md) (15 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (13 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/game.py`
- `server/container/bundles/magic.py`
- `server/dependencies.py`
- `server/game/instance_manager.py`
- `server/game/level_service.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_search_service.py`

## Audit Trail

- EXTRACTED: 1510 (88%)
- INFERRED: 198 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*