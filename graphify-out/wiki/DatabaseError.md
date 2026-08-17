# DatabaseError

> 843 nodes

## Key Concepts

- **DatabaseError** (264 connections) — `server/exceptions.py`
- **Player** (231 connections) — `server/models/player.py`
- **log_and_raise()** (196 connections) — `server/utils/error_logging.py`
- **models/player.py** (98 connections) — `server/models/player.py`
- **get_session_maker()** (97 connections) — `server/database.py`
- **sqlalchemy.md** (89 connections) — `.claude/rules/sqlalchemy.md`
- **server/models/__init__.py** (86 connections) — `server/models/__init__.py`
- **database.py** (82 connections) — `server/database.py`
- **Base** (60 connections) — `server/models/base.py`
- **Profession** (53 connections) — `server/models/profession.py`
- **get_async_session()** (53 connections) — `server/database.py`
- **test_async_persistence_core.py** (41 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **rooms.py** (40 connections) — `server/api/rooms.py`
- **game_tick_death.py** (34 connections) — `server/app/game_tick_death.py`
- **persistence/repositories/__init__.py** (31 connections) — `server/persistence/repositories/__init__.py`
- **PlayerRepository** (30 connections) — `server/persistence/repositories/player_repository.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **player_repository.py** (29 connections) — `server/persistence/repositories/player_repository.py`
- **test_lucidity_models.py** (28 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **LucidityRepository** (27 connections) — `server/services/lucidity_repository.py`
- **test_world.py** (27 connections) — `server/tests/unit/models/test_world.py`
- **Skill** (26 connections) — `server/models/skill.py`
- **test_lucidity_repository.py** (25 connections) — `server/tests/unit/services/test_lucidity_repository.py`
- **LucidityExposureState** (24 connections) — `server/models/lucidity.py`
- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- *... and 818 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (204 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (99 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (51 shared connections)
- [AliasStorage](AliasStorage.md) (38 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (29 shared connections)
- [HealthRepository](HealthRepository.md) (24 shared connections)
- [NPCDefinition](NPCDefinition.md) (19 shared connections)
- [test_container_persistence_crud.py](test_container_persistence_crud.py.md) (19 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (19 shared connections)
- [test_item.py](test_item.py.md) (19 shared connections)
- [ConnectionManager](ConnectionManager.md) (18 shared connections)
- [ExplorationService](ExplorationService.md) (17 shared connections)

## Source Files

- `.claude/rules/sqlalchemy.md`
- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/alembic/versions/2025_11_12_add_item_tables.py`
- `server/api/rooms.py`
- `server/app/game_tick_death.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/commands/channel_commands.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/exceptions.py`
- `server/game/room_service.py`
- `server/game/skill_service.py`
- `server/metadata.py`
- `server/models/__init__.py`
- `server/models/base.py`

## Audit Trail

- EXTRACTED: 2557 (84%)
- INFERRED: 504 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*