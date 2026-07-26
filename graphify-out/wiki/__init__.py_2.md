# __init__.py

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

- [DatabaseError](DatabaseError.md) (49 shared connections)
- [get_logger](get_logger.md) (44 shared connections)
- [Base](Base.md) (19 shared connections)
- [datetime](datetime.md) (17 shared connections)
- [exceptions.py](exceptions.py.md) (16 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (14 shared connections)
- [dependencies.py](dependencies.py.md) (11 shared connections)
- [test_item.py](test_item.py.md) (11 shared connections)
- [ScheduleEntry](ScheduleEntry.md) (10 shared connections)
- [.create_instance](create_instance.md) (8 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [ExplorationService](ExplorationService.md) (6 shared connections)

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