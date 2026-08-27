# TargetResolutionService

> 110 nodes

## Key Concepts

- **SkillService** (35 connections) — `server/game/skill_service.py`
- **SkillRepository** (26 connections) — `server/persistence/repositories/skill_repository.py`
- **PlayerSkillRepository** (21 connections) — `server/persistence/repositories/player_skill_repository.py`
- **skill_service.py** (21 connections) — `server/game/skill_service.py`
- **skills.py** (19 connections) — `server/api/skills.py`
- **skill_repository.py** (19 connections) — `server/persistence/repositories/skill_repository.py`
- **test_skill_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **skills_commands.py** (16 connections) — `server/commands/skills_commands.py`
- **skill_use_log_repository.py** (15 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **test_player_skill_repository.py** (13 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **SkillUseLogRepository** (12 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **get_skills_catalog()** (12 connections) — `server/api/skills.py`
- **test_skill_use_log_repository.py** (11 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **_row_to_skill()** (9 connections) — `server/persistence/repositories/skill_repository.py`
- **Any** (9 connections)
- **players/skill.py** (9 connections) — `server/schemas/players/skill.py`
- **asyncio** (8 connections)
- **UUID** (7 connections)
- **SkillListResponse** (6 connections) — `server/schemas/players/skill.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **asyncio** (6 connections)
- **PlayerSkillEntry** (5 connections) — `server/schemas/players/skill.py`
- *... and 85 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (43 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (26 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (13 shared connections)
- [CacheManager](CacheManager.md) (11 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (11 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (2 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (2 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (2 shared connections)
- [main](main.md) (1 shared connections)
- [test_logging_processors.py](test_logging_processors.py.md) (1 shared connections)
- [canonical_room_id_impl](canonical_room_id_impl.md) (1 shared connections)

## Source Files

- `server/api/skills.py`
- `server/commands/skills_commands.py`
- `server/dependencies.py`
- `server/game/skill_service.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/schemas/players/skill.py`
- `server/tests/unit/api/test_skills.py`
- `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`

## Audit Trail

- EXTRACTED: 294 (90%)
- INFERRED: 32 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*