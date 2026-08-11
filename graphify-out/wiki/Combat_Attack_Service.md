# Combat Attack Service

> 166 nodes

## Key Concepts

- **Spell** (93 connections) — `server/models/spell.py`
- **SpellLearningService** (38 connections) — `server/game/magic/spell_learning_service.py`
- **SpellRegistry** (35 connections) — `server/game/magic/spell_registry.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **SpellTargetingService** (29 connections) — `server/game/magic/spell_targeting.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- **spell_targeting.py** (20 connections) — `server/game/magic/spell_targeting.py`
- **MagicBundle** (19 connections) — `server/container/bundles/magic.py`
- **spell_registry.py** (15 connections) — `server/game/magic/spell_registry.py`
- **test_spell_targeting.py** (15 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **_create_registry_and_targeting()** (14 connections) — `server/container/bundles/magic.py`
- **SpellRepository** (14 connections) — `server/persistence/repositories/spell_repository.py`
- **SpellMaterial** (13 connections) — `server/models/spell.py`
- **Any** (12 connections)
- **.learn_spell()** (12 connections) — `server/game/magic/spell_learning_service.py`
- **UUID** (10 connections)
- **spell_materials.py** (10 connections) — `server/game/magic/spell_materials.py`
- **_create_learning_mp_regen_and_magic()** (9 connections) — `server/container/bundles/magic.py`
- **._validate_prerequisites()** (9 connections) — `server/game/magic/spell_learning_service.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **SpellSchool** (8 connections) — `server/models/spell.py`
- **SpellTargetType** (8 connections) — `server/models/spell.py`
- *... and 141 more nodes in this community*

## Relationships

- [Player Respawn Service](Player_Respawn_Service.md) (55 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (25 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (14 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (11 shared connections)
- [Container Open Events](Container_Open_Events.md) (10 shared connections)
- [Security Headers Middleware](Security_Headers_Middleware.md) (10 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (9 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (9 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (7 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (6 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (6 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 730 (92%)
- INFERRED: 67 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*