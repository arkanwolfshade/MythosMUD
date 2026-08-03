# npc populate databases

> 116 nodes

## Key Concepts

- **DatabaseError** (440 connections) — `server/exceptions.py`
- **player_skill_repository.py** (18 connections) — `server/persistence/repositories/player_skill_repository.py`
- **profession_repository.py** (17 connections) — `server/persistence/repositories/profession_repository.py`
- **ExperienceRepository** (16 connections) — `server/persistence/repositories/experience_repository.py`
- **experience_repository.py** (15 connections) — `server/persistence/repositories/experience_repository.py`
- **.__init__()** (13 connections) — `server/async_persistence.py`
- **skill_use_log_repository.py** (13 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **spell_repository.py** (13 connections) — `server/persistence/repositories/spell_repository.py`
- **logging_processors.py** (12 connections) — `server/structured_logging/logging_processors.py`
- **ProfessionRepository** (11 connections) — `server/persistence/repositories/profession_repository.py`
- **fetch_professions()** (9 connections) — `server/async_persistence_direct_queries.py`
- **_row_to_profession()** (9 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_by_player_id()** (8 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.update_player_xp()** (7 connections) — `server/persistence/repositories/experience_repository.py`
- **.get_all_professions()** (7 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_profession_by_id()** (7 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_all_spells()** (7 connections) — `server/persistence/repositories/spell_repository.py`
- **.get_spell_by_id()** (7 connections) — `server/persistence/repositories/spell_repository.py`
- **populate_test_npc_databases.py** (6 connections) — `scripts/populate_test_npc_databases.py`
- **.gain_experience()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **.update_player_stat_field()** (6 connections) — `server/persistence/repositories/experience_repository.py`
- **_row_to_player_skill_with_skill()** (6 connections) — `server/persistence/repositories/player_skill_repository.py`
- **.delete_for_player()** (6 connections) — `server/persistence/repositories/player_skill_repository.py`
- **UUID** (6 connections)
- **.insert_many()** (6 connections) — `server/persistence/repositories/player_skill_repository.py`
- *... and 91 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (42 shared connections)
- [NATS Messaging](NATS_Messaging.md) (37 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (36 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (32 shared connections)
- [persistence container item](persistence_container_item.md) (32 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (24 shared connections)
- [player room persistence](player_room_persistence.md) (19 shared connections)
- [command inventory factories](command_inventory_factories.md) (17 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (16 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (15 shared connections)
- [dialogue definitions admin](dialogue_definitions_admin.md) (14 shared connections)
- [player model models](player_model_models.md) (13 shared connections)

## Source Files

- `scripts/populate_test_npc_databases.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/exceptions.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/profession_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/structured_logging/logging_processors.py`
- `server/tests/unit/game/test_player_service_mutations.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/services/test_player_respawn_service.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 516 (60%)
- INFERRED: 349 (40%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*