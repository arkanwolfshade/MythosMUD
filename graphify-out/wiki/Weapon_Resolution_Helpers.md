# Weapon Resolution Helpers

> 257 nodes · cohesion 0.01

## Key Concepts

- **__init__.py** (71 connections) — `server/models/__init__.py`
- **game.py** (42 connections) — `server/container/bundles/game.py`
- **GameBundle** (41 connections) — `server/container/bundles/game.py`
- **.initialize()** (35 connections) — `server/container/bundles/game.py`
- **PrototypeRegistry** (35 connections) — `server/game/items/prototype_registry.py`
- **SkillService** (35 connections) — `server/game/skill_service.py`
- **ItemPrototypeModel** (28 connections) — `server/game/items/models.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **MythosChronicle** (27 connections) — `server/time/time_service.py`
- **get_mythos_chronicle()** (24 connections) — `server/time/time_service.py`
- **resolve_weapon_attack_from_equipped()** (22 connections) — `server/game/weapons.py`
- **skill_service.py** (20 connections) — `server/game/skill_service.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **prototype_registry.py** (19 connections) — `server/game/items/prototype_registry.py`
- **PrototypeRegistryError** (19 connections) — `server/game/items/prototype_registry.py`
- **SkillRepository** (19 connections) — `server/persistence/repositories/skill_repository.py`
- **player_skill_repository.py** (18 connections) — `server/persistence/repositories/player_skill_repository.py`
- **test_weapons.py** (18 connections) — `server/tests/unit/game/test_weapons.py`
- **MythosTickScheduler** (18 connections) — `server/time/tick_scheduler.py`
- **PlayerSkill** (17 connections) — `server/models/player_skill.py`
- **PlayerSkillRepository** (17 connections) — `server/persistence/repositories/player_skill_repository.py`
- **skill_repository.py** (17 connections) — `server/persistence/repositories/skill_repository.py`
- **item_factory.py** (14 connections) — `server/game/items/item_factory.py`
- **ItemPrototype** (14 connections) — `server/models/item.py`
- **tick_scheduler.py** (14 connections) — `server/time/tick_scheduler.py`
- *... and 232 more nodes in this community*

## Relationships

- [Realtime Connection Impl](Realtime_Connection_Impl.md) (49 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (44 shared connections)
- [Metadata Npc](Metadata_Npc.md) (19 shared connections)
- [Quest Flow Integration](Quest_Flow_Integration.md) (17 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (16 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (14 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (11 shared connections)
- [Command Alias Handling](Command_Alias_Handling.md) (11 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (10 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (8 shared connections)
- [App Lifespan Management](App_Lifespan_Management.md) (7 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (6 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/dependencies.py`
- `server/game/instance_manager.py`
- `server/game/items/__init__.py`
- `server/game/items/component_hooks.py`
- `server/game/items/constants.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`
- `server/game/items/models.py`
- `server/game/items/prototype_registry.py`
- `server/game/level_service.py`
- `server/game/skill_service.py`
- `server/game/weapons.py`
- `server/models/__init__.py`
- `server/models/item.py`
- `server/models/player_skill.py`
- `server/models/skill.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`

## Audit Trail

- EXTRACTED: 1136 (90%)
- INFERRED: 131 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*