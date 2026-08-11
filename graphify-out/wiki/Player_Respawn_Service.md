# Player Respawn Service

> 172 nodes

## Key Concepts

- **SpellEffects** (56 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (38 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **PlayerSpellRepository** (37 connections) — `server/persistence/repositories/player_spell_repository.py`
- **lifespan_magic.py** (35 connections) — `server/app/lifespan_magic.py`
- **MagicService** (30 connections) — `server/game/magic/magic_service.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **SpellEffectsDeps** (25 connections) — `server/game/magic/spell_effects.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **SpellEffectPlayer** (15 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **_initialize_magic_service()** (13 connections) — `server/app/lifespan_magic.py`
- **UUID** (12 connections)
- **PlayerPersistenceSpellPort** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **SpellEffectType** (10 connections) — `server/models/spell.py`
- **FastAPI** (9 connections)
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_corruption_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **._process_heal()** (8 connections) — `server/game/magic/spell_effects.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- *... and 147 more nodes in this community*

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (55 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (38 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (25 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (22 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (14 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (11 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (10 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (9 shared connections)
- [Container Open Events](Container_Open_Events.md) (6 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (5 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (5 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (5 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/spell.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 692 (88%)
- INFERRED: 91 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*