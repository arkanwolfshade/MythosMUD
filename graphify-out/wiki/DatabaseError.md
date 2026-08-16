# DatabaseError

> 84 nodes

## Key Concepts

- **DatabaseError** (262 connections) — `server/exceptions.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **skill_repository.py** (19 connections) — `server/persistence/repositories/skill_repository.py`
- **experience_repository.py** (17 connections) — `server/persistence/repositories/experience_repository.py`
- **test_experience_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_skill_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_skill_use_log_repository.py** (11 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **asyncio** (10 connections)
- **_row_to_skill()** (9 connections) — `server/persistence/repositories/skill_repository.py`
- **fetch_professions()** (8 connections) — `server/async_persistence_direct_queries.py`
- **asyncio** (8 connections)
- **populate_test_npc_databases.py** (7 connections) — `scripts/populate_test_npc_databases.py`
- **.update_player_xp()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.get_all_skills()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_id()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_key()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **main()** (5 connections) — `scripts/populate_test_npc_databases.py`
- **.gain_experience()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_stat_field()** (5 connections) — `server/persistence/repositories/experience_repository.py`
- **get_npc_data_from_source()** (4 connections) — `scripts/populate_test_npc_databases.py`
- **populate_database()** (4 connections) — `scripts/populate_test_npc_databases.py`
- **.__init__()** (4 connections) — `server/persistence/repositories/experience_repository.py`
- **test_update_player_stat_field_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- **test_update_player_xp_player_not_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_experience_repository.py`
- *... and 59 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (25 shared connections)
- [log_and_raise](log_and_raise.md) (21 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (19 shared connections)
- [SkillService](SkillService.md) (18 shared connections)
- [ExplorationService](ExplorationService.md) (15 shared connections)
- [Player](Player.md) (15 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [NPCDefinition](NPCDefinition.md) (12 shared connections)
- [get_session_maker](get_session_maker.md) (12 shared connections)
- [persistence/repositories/__init__.py](persistence-repositories-__init__.py.md) (9 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (8 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (8 shared connections)

## Source Files

- `scripts/populate_test_npc_databases.py`
- `server/async_persistence_direct_queries.py`
- `server/dependencies.py`
- `server/exceptions.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/skill_repository.py`
- `server/tests/unit/persistence/repositories/test_experience_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`

## Audit Trail

- EXTRACTED: 313 (66%)
- INFERRED: 159 (34%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*