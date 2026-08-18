# lifespan_magic.py

> 85 nodes

## Key Concepts

- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **MagicBundle** (13 connections) — `server/container/bundles/magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_create_learning_mp_regen_and_magic()** (11 connections) — `server/container/bundles/magic.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **UUID** (8 connections)
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **._get_player()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._match_combat_opponent()** (7 connections) — `server/game/magic/spell_targeting.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- **.initialize()** (6 connections) — `server/container/bundles/magic.py`
- *... and 60 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (25 shared connections)
- [Spell](Spell.md) (18 shared connections)
- [DatabaseError](DatabaseError.md) (16 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (15 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (14 shared connections)
- [magic_service.py](magic_service.py.md) (11 shared connections)
- [SpellLearningService](SpellLearningService.md) (11 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (6 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (6 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (6 shared connections)
- [CombatParticipant](CombatParticipant.md) (4 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/container/test_container_bundles.py`

## Audit Trail

- EXTRACTED: 262 (86%)
- INFERRED: 41 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*