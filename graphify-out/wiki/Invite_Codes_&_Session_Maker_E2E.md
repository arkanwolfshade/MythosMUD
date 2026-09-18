# Invite Codes & Session Maker (E2E)

> 186 nodes

## Key Concepts

- **get_session_maker()** (87 connections) — `server/database.py`
- **Skill** (25 connections) — `server/models/skill.py`
- **SkillRepository** (24 connections) — `server/persistence/repositories/skill_repository.py`
- **PlayerSkillRepository** (21 connections) — `server/persistence/repositories/player_skill_repository.py`
- **skill_service.py** (21 connections) — `server/game/skill_service.py`
- **player_skill_repository.py** (19 connections) — `server/persistence/repositories/player_skill_repository.py`
- **skill_repository.py** (18 connections) — `server/persistence/repositories/skill_repository.py`
- **test_skill_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **QuestInstanceRepository** (14 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **SkillUseLogRepository** (12 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **models/skill.py** (12 connections) — `server/models/skill.py`
- **test_player_skill_repository.py** (12 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **PlayerSkill** (11 connections) — `server/models/player_skill.py`
- **.create()** (10 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **player_skill.py** (10 connections) — `server/models/player_skill.py`
- **test_skill_use_log_repository.py** (10 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **_row_to_skill()** (9 connections) — `server/persistence/repositories/skill_repository.py`
- **Any** (9 connections)
- **.get_by_player_and_quest()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_active_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **.list_completed_by_player()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **_row_to_quest_instance()** (8 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **asyncio** (8 connections)
- *... and 161 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (116 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (23 shared connections)
- [Community 122](Community_122.md) (7 shared connections)
- [Community 378](Community_378.md) (7 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (5 shared connections)
- [Community 100](Community_100.md) (5 shared connections)
- [Community 226](Community_226.md) (5 shared connections)
- [Database Manager](Database_Manager.md) (4 shared connections)
- [Community 333](Community_333.md) (4 shared connections)
- [Community 1087](Community_1087.md) (3 shared connections)
- [Community 543](Community_543.md) (2 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (2 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/game/skill_service.py`
- `server/models/player_skill.py`
- `server/models/skill.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/quest_instance_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- `server/tests/unit/persistence/test_quest_instance_repository.py`
- `tools/invite_tools/check_invites.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 476 (93%)
- INFERRED: 38 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*