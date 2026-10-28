# LoggingPatternLinter

> 127 nodes · cohesion 0.03

## Key Concepts

- **DatabaseError** (297 connections) — `server/exceptions.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **connection_manager_api.py** (25 connections) — `server/realtime/connection_manager_api.py`
- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- **ExperienceRepository** (23 connections) — `server/persistence/repositories/experience_repository.py`
- **Skill** (19 connections) — `server/models/skill.py`
- **player_skill_repository.py** (19 connections) — `server/persistence/repositories/player_skill_repository.py`
- **skill_repository.py** (18 connections) — `server/persistence/repositories/skill_repository.py`
- **experience_repository.py** (17 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_skill_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **SkillUseLogRepository** (15 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **PlayerSkill** (14 connections) — `server/models/player_skill.py`
- **test_emote_repository.py** (14 connections) — `server/tests/unit/persistence/repositories/test_emote_repository.py`
- **models/skill.py** (12 connections) — `server/models/skill.py`
- **test_player_skill_repository.py** (12 connections) — `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- **test_skill_use_log_repository.py** (10 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **fetch_user_by_username_case_insensitive()** (9 connections) — `server/async_persistence_direct_queries.py`
- **asyncio** (9 connections)
- **fetch_professions()** (8 connections) — `server/async_persistence_direct_queries.py`
- **asyncio** (8 connections)
- **._persist_stat_field_delta()** (7 connections) — `server/persistence/repositories/experience_repository.py`
- **populate_test_npc_databases.py** (6 connections) — `scripts/populate_test_npc_databases.py`
- **_row_to_player_skill_with_skill()** (6 connections) — `server/persistence/repositories/player_skill_repository.py`
- **asyncio** (6 connections)
- *... and 102 more nodes in this community*

## Relationships

- [endpoints.py](endpoints.py.md) (53 shared connections)
- [AttributeError](AttributeError.md) (35 shared connections)
- [Room](Room.md) (19 shared connections)
- [.profession_to_dict](profession_to_dict.md) (19 shared connections)
- [active_lucidity_service.py](active_lucidity_service.py.md) (14 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (14 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (11 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (10 shared connections)
- [test_event_publisher.py](test_event_publisher.py.md) (10 shared connections)
- [test_aggression.py](test_aggression.py.md) (8 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (8 shared connections)
- [✅ Phase 2 Async Persistence Migration - COMPLETE](✅_Phase_2_Async_Persistence_Migration_-_COMPLETE.md) (7 shared connections)

## Source Files

- `scripts/populate_test_npc_databases.py`
- `server/async_persistence_direct_queries.py`
- `server/dependencies.py`
- `server/exceptions.py`
- `server/game/skill_service.py`
- `server/models/player_skill.py`
- `server/models/skill.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/realtime/connection_manager_api.py`
- `server/tests/unit/persistence/repositories/test_emote_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`
- `server/tests/unit/persistence/repositories/test_player_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 474 (73%)
- INFERRED: 176 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*