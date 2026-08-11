# Optimization Archive Modernization

> 464 nodes

## Key Concepts

- **DatabaseError** (434 connections) — `server/exceptions.py`
- **log_and_raise()** (174 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (91 connections) — `server/database.py`
- **async_persistence.py** (74 connections) — `server/async_persistence.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **__init__.py** (28 connections) — `server/persistence/repositories/__init__.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **CreateItemInstanceInput** (23 connections) — `server/async_persistence_constants.py`
- **container_query_helpers_async.py** (23 connections) — `server/persistence/container_query_helpers_async.py`
- **container_repository.py** (23 connections) — `server/persistence/repositories/container_repository.py`
- **test_quest_instance_repository.py** (22 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **QuestInstance** (21 connections) — `server/models/quest.py`
- **player_effect_repository.py** (21 connections) — `server/persistence/repositories/player_effect_repository.py`
- **skill_service.py** (20 connections) — `server/game/skill_service.py`
- **HealthRepository** (20 connections) — `server/persistence/repositories/health_repository.py`
- **player_spell_repository.py** (20 connections) — `server/persistence/repositories/player_spell_repository.py`
- **QuestInstanceRepository** (20 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- **quest_instance_repository.py** (19 connections) — `server/persistence/repositories/quest_instance_repository.py`
- **SkillRepository** (19 connections) — `server/persistence/repositories/skill_repository.py`
- **item_instance_persistence_async.py** (18 connections) — `server/persistence/item_instance_persistence_async.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **player_skill_repository.py** (18 connections) — `server/persistence/repositories/player_skill_repository.py`
- **GameMechanicsService** (17 connections) — `server/game/mechanics.py`
- **PlayerSkillRepository** (17 connections) — `server/persistence/repositories/player_skill_repository.py`
- *... and 439 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (74 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (73 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (72 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (62 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (30 shared connections)
- [Player Save Preparer](Player_Save_Preparer.md) (28 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (27 shared connections)
- [Draggable Panel UI](Draggable_Panel_UI.md) (26 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (25 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (22 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (20 shared connections)
- [Maps API Endpoints](Maps_API_Endpoints.md) (14 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `monitoring/webhook-receiver.py`
- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/async_persistence_direct_queries.py`
- `server/database.py`
- `server/exceptions.py`
- `server/game/mechanics.py`
- `server/game/movement_service.py`
- `server/game/skill_service.py`
- `server/models/quest.py`
- `server/persistence/container_persistence_async.py`
- `server/persistence/container_query_helpers_async.py`
- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/container_repository.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/item_repository.py`
- `server/persistence/repositories/player_effect_repository.py`

## Audit Trail

- EXTRACTED: 2373 (84%)
- INFERRED: 463 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*