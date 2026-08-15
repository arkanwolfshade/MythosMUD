# Spell

> 48 nodes

## Key Concepts

- **Spell** (128 connections) — `server/models/spell.py`
- **SpellLearningService** (44 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell_learning_service.py** (15 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **.learn_spell()** (12 connections) — `server/game/magic/spell_learning_service.py`
- **Any** (12 connections)
- **asyncio** (11 connections)
- **UUID** (10 connections)
- **._validate_prerequisites()** (9 connections) — `server/game/magic/spell_learning_service.py`
- **._load_spell_learn_context()** (6 connections) — `server/game/magic/spell_learning_service.py`
- **._check_required_spell_prerequisites()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_book()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_npc()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_quest()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **._persist_spell_learning()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **._apply_mythos_corruption_on_learn()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **._check_intelligence_requirement()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **._check_power_requirement()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **._spell_learn_success_response()** (4 connections) — `server/game/magic/spell_learning_service.py`
- **.increase_mastery_on_cast()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **._resolve_spell()** (3 connections) — `server/game/magic/spell_learning_service.py`
- **.search_spells()** (3 connections) — `server/game/magic/spell_registry.py`
- **learning_service()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_increase_mastery_on_cast()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_already_known()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_from_book_no_spell_id()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- *... and 23 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (32 shared connections)
- [SpellEffectType](SpellEffectType.md) (22 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (18 shared connections)
- [magic_service.py](magic_service.py.md) (15 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (12 shared connections)
- [server/models/game.py](server-models-game.py.md) (7 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (7 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (6 shared connections)
- [test_magic_healing_events.py](test_magic_healing_events.py.md) (4 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_learning_service.py`

## Audit Trail

- EXTRACTED: 156 (65%)
- INFERRED: 85 (35%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*