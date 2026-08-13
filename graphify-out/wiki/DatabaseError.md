# DatabaseError

> 361 nodes

## Key Concepts

- **DatabaseError** (167 connections) — `server/exceptions.py`
- **database.py** (79 connections) — `server/database.py`
- **error_logging.py** (55 connections) — `server/utils/error_logging.py`
- **GameBundle** (45 connections) — `server/container/bundles/game.py`
- **bundles/game.py** (42 connections) — `server/container/bundles/game.py`
- **SkillService** (37 connections) — `server/game/skill_service.py`
- **ScheduleEntry** (28 connections) — `server/schemas/calendar/calendar.py`
- **persistence/repositories/__init__.py** (28 connections) — `server/persistence/repositories/__init__.py`
- **Skill** (27 connections) — `server/models/skill.py`
- **ScheduleService** (27 connections) — `server/services/schedule_service.py`
- **schedule_service.py** (25 connections) — `server/services/schedule_service.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **holiday_service.py** (24 connections) — `server/services/holiday_service.py`
- **skill_service.py** (20 connections) — `server/game/skill_service.py`
- **InstanceManager** (19 connections) — `server/game/instance_manager.py`
- **SkillRepository** (19 connections) — `server/persistence/repositories/skill_repository.py`
- **get_asyncpg_server_settings_for_database_url()** (19 connections) — `server/database_config_helpers.py`
- **emote_service.py** (19 connections) — `server/game/emote_service.py`
- **MythosTickScheduler** (18 connections) — `server/time/tick_scheduler.py`
- **core.py** (18 connections) — `server/container/bundles/core.py`
- **item_instance_persistence_async.py** (18 connections) — `server/persistence/item_instance_persistence_async.py`
- **player_skill_repository.py** (18 connections) — `server/persistence/repositories/player_skill_repository.py`
- **rate_overrides.py** (18 connections) — `server/services/passive_lucidity_flux/rate_overrides.py`
- **PlayerSkillRepository** (17 connections) — `server/persistence/repositories/player_skill_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- *... and 336 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (95 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (55 shared connections)
- [get_session_maker](get_session_maker.md) (31 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (29 shared connections)
- [log_and_raise](log_and_raise.md) (28 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (24 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (23 shared connections)
- [MythosMUDError](MythosMUDError.md) (18 shared connections)
- [Player](Player.md) (17 shared connections)
- [get_async_session](get_async_session.md) (13 shared connections)
- [PlayerService](PlayerService.md) (12 shared connections)
- [DatabaseManager](DatabaseManager.md) (10 shared connections)

## Source Files

- `scripts/verify_and_load_seed.py`
- `server/container/bundles/core.py`
- `server/container/bundles/game.py`
- `server/container/utils.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/events/distributed_event_bus.py`
- `server/exceptions.py`
- `server/game/emote_service.py`
- `server/game/instance_manager.py`
- `server/game/level_service.py`
- `server/game/skill_service.py`
- `server/models/skill.py`
- `server/npc/lifecycle_manager.py`
- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/item_repository.py`
- `server/persistence/repositories/player_skill_repository.py`

## Audit Trail

- EXTRACTED: 1225 (93%)
- INFERRED: 88 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*