# Chat Channel Logger

> 239 nodes

## Key Concepts

- **GameBundle** (45 connections) — `server/container/bundles/game.py`
- **game.py** (42 connections) — `server/container/bundles/game.py`
- **SkillService** (37 connections) — `server/game/skill_service.py`
- **test_skill_service.py** (36 connections) — `server/tests/unit/game/test_skill_service.py`
- **__init__.py** (28 connections) — `server/persistence/repositories/__init__.py`
- **ScheduleService** (28 connections) — `server/services/schedule_service.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **skill_service.py** (20 connections) — `server/game/skill_service.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **SkillRepository** (19 connections) — `server/persistence/repositories/skill_repository.py`
- **player_skill_repository.py** (18 connections) — `server/persistence/repositories/player_skill_repository.py`
- **RoomCacheService** (17 connections) — `server/caching/cache_service.py`
- **PlayerSkill** (17 connections) — `server/models/player_skill.py`
- **PlayerSkillRepository** (17 connections) — `server/persistence/repositories/player_skill_repository.py`
- **skill_repository.py** (17 connections) — `server/persistence/repositories/skill_repository.py`
- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **LevelService** (13 connections) — `server/game/level_service.py`
- **SkillUseLogRepository** (13 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **skill.py** (12 connections) — `server/models/skill.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **_occupation_slots_9()** (11 connections) — `server/tests/unit/game/test_skill_service.py`
- **Any** (10 connections)
- **player_skill.py** (10 connections) — `server/models/player_skill.py`
- *... and 214 more nodes in this community*

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (52 shared connections)
- [Client Event Store](Client_Event_Store.md) (34 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (15 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (14 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (12 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (8 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (8 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (8 shared connections)
- [Alias Command Models](Alias_Command_Models.md) (7 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (7 shared connections)
- [Npc Services Combat](Npc_Services_Combat.md) (6 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (6 shared connections)

## Source Files

- `scripts/bench_cache.py`
- `server/caching/cache_service.py`
- `server/container/bundles/game.py`
- `server/dependencies.py`
- `server/game/instance_manager.py`
- `server/game/level_service.py`
- `server/game/skill_service.py`
- `server/models/player_skill.py`
- `server/models/skill.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/services/schedule_service.py`
- `server/tests/unit/api/test_skills.py`
- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 921 (91%)
- INFERRED: 86 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*