# Magic Lifespan Initialization

> 140 nodes · cohesion 0.02

## Key Concepts

- **SpellRegistry** (35 connections) — `server/game/magic/spell_registry.py`
- **lifespan_magic.py** (34 connections) — `server/app/lifespan_magic.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **MagicService** (29 connections) — `server/game/magic/magic_service.py`
- **SpellTargetingService** (29 connections) — `server/game/magic/spell_targeting.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **spell_registry.py** (15 connections) — `server/game/magic/spell_registry.py`
- **test_spell_targeting.py** (15 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **SpellRepository** (14 connections) — `server/persistence/repositories/spell_repository.py`
- **_initialize_magic_service()** (13 connections) — `server/app/lifespan_magic.py`
- **_create_registry_and_targeting()** (13 connections) — `server/container/bundles/magic.py`
- **SpellMaterial** (13 connections) — `server/models/spell.py`
- **_initialize_spell_effects()** (9 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections)
- **SpellEffectType** (9 connections) — `server/models/spell.py`
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **SpellSchool** (8 connections) — `server/models/spell.py`
- **SpellTargetType** (8 connections) — `server/models/spell.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- *... and 115 more nodes in this community*

## Relationships

- [Game Magic Spell](Game_Magic_Spell.md) (41 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (25 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (22 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (16 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (10 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (8 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (8 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (7 shared connections)
- [Commands Go Command](Commands_Go_Command.md) (6 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (6 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (5 shared connections)
- [MP Regeneration Service](MP_Regeneration_Service.md) (3 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 527 (88%)
- INFERRED: 69 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*