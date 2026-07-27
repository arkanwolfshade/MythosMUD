# Game Service Bundle

> 151 nodes · cohesion 0.03

## Key Concepts

- **GameBundle** (41 connections) — `server/container/bundles/game.py`
- **ScheduleService** (39 connections) — `server/services/schedule_service.py`
- **game.py** (38 connections) — `server/container/bundles/game.py`
- **SkillService** (34 connections) — `server/game/skill_service.py`
- **.initialize()** (33 connections) — `server/container/bundles/game.py`
- **Skill** (31 connections) — `server/models/skill.py`
- **Any** (30 connections) — `server/container/bundles/game.py`
- **ApplicationContainer** (30 connections) — `server/container/bundles/game.py`
- **InstanceManager** (29 connections) — `server/game/instance_manager.py`
- **datetime** (29 connections) — `server/container/bundles/game.py`
- **Exception** (28 connections) — `server/container/bundles/game.py`
- **SkillRepository** (27 connections) — `server/persistence/repositories/skill_repository.py`
- **PlayerSkillRepository** (26 connections) — `server/persistence/repositories/player_skill_repository.py`
- **RoomCacheService** (22 connections) — `server/caching/cache_service.py`
- **SkillUseLogRepository** (22 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **main.py** (19 connections) — `server/container/main.py`
- **ItemPrototype** (17 connections) — `server/models/item.py`
- **LevelService** (16 connections) — `server/game/level_service.py`
- **normalize_environment()** (15 connections) — `server/utils/project_paths.py`
- **skill_service.py** (14 connections) — `server/game/skill_service.py`
- **Any** (14 connections) — `server/game/skill_service.py`
- **get_calendar_paths_for_environment()** (14 connections) — `server/utils/project_paths.py`
- **UUID** (12 connections) — `server/game/skill_service.py`
- **get_environment_data_dir()** (10 connections) — `server/utils/project_paths.py`
- **get_project_root()** (10 connections) — `server/utils/project_paths.py`
- *... and 126 more nodes in this community*

## Relationships

- [[NPC Admin API]] (57 shared connections)
- [[Weapon Resolution Helpers]] (23 shared connections)
- [[Application DI Bundles]] (19 shared connections)
- [[Distributed Event Bus]] (15 shared connections)
- [[SQLAlchemy Model Base]] (15 shared connections)
- [[Schedule Service Loader]] (14 shared connections)
- [[Cache and NPC Cache]] (13 shared connections)
- [[Async Persistence Layer]] (13 shared connections)
- [[Game Instance Manager]] (11 shared connections)
- [[Holiday Persistence Models]] (9 shared connections)
- [[Time Event Consumer]] (9 shared connections)
- [[Party Service Management]] (7 shared connections)

## Source Files

- `server/caching/cache_service.py`
- `server/container/bundles/game.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/dependencies.py`
- `server/game/instance_manager.py`
- `server/game/level_service.py`
- `server/game/skill_service.py`
- `server/models/item.py`
- `server/models/skill.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/services/schedule_service.py`
- `server/tests/unit/api/test_skills.py`
- `server/tests/unit/utils/test_project_paths.py`
- `server/utils/project_paths.py`

## Audit Trail

- EXTRACTED: 641 (68%)
- INFERRED: 295 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
