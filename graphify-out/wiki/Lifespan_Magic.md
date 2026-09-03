# Lifespan Magic

> 151 nodes

## Key Concepts

- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **spell_learning_service.py** (22 connections) — `server/game/magic/spell_learning_service.py`
- **player_spell_repository.py** (22 connections) — `server/persistence/repositories/player_spell_repository.py`
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **test_player_spell_repository.py** (20 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **MPRegenerationService** (18 connections) — `server/game/magic/mp_regeneration_service.py`
- **PlayerSpell** (17 connections) — `server/models/player_spells.py`
- **_create_registry_and_targeting()** (16 connections) — `server/container/bundles/magic.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **_row_to_player_spell()** (11 connections) — `server/persistence/repositories/player_spell_repository.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **_mock_session_with_rows()** (9 connections) — `server/tests/unit/persistence/test_player_spell_repository.py`
- **FastAPI** (9 connections)
- **asyncio** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **UUID** (8 connections)
- *... and 126 more nodes in this community*

## Relationships

- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (27 shared connections)
- [Test Magic Service](Test_Magic_Service.md) (17 shared connections)
- [Test Spell](Test_Spell.md) (16 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (13 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (13 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (12 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (12 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (10 shared connections)
- [Test Target Resolution Service](Test_Target_Resolution_Service.md) (10 shared connections)
- [Spell Learning Service](Spell_Learning_Service.md) (9 shared connections)
- [Test Spell Effects](Test_Spell_Effects.md) (9 shared connections)
- [Test Magic Commands](Test_Magic_Commands.md) (8 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/container/bundles/magic.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/models/player_spells.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/models/test_player_spells.py`
- `server/tests/unit/persistence/test_player_spell_repository.py`

## Audit Trail

- EXTRACTED: 425 (91%)
- INFERRED: 44 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*