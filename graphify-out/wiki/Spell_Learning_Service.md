# Spell Learning Service

> 40 nodes

## Key Concepts

- **SpellLearningService** (46 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell_learning_service.py** (16 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
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
- **learning_service()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_increase_mastery_on_cast()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_already_known()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_from_book_no_spell_id()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_from_book_with_spell()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **test_learn_spell_from_npc()** (3 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- *... and 15 more nodes in this community*

## Relationships

- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (10 shared connections)
- [Lifespan Magic](Lifespan_Magic.md) (9 shared connections)
- [Test Magic Commands](Test_Magic_Commands.md) (3 shared connections)
- [Test Magic Service](Test_Magic_Service.md) (3 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (2 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (1 shared connections)
- [Magic Service](Magic_Service.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_learning_service.py`
- `server/tests/unit/game/magic/test_spell_learning_service.py`

## Audit Trail

- EXTRACTED: 104 (85%)
- INFERRED: 18 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*