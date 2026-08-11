# Schemas Maps Map

> 256 nodes

## Key Concepts

- **DatabaseError** (434 connections) — `server/exceptions.py`
- **exceptions.py** (196 connections) — `server/exceptions.py`
- **log_and_raise()** (174 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (91 connections) — `server/database.py`
- **error_logging.py** (55 connections) — `server/utils/error_logging.py`
- **__init__.py** (32 connections) — `server/persistence/__init__.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **__init__.py** (28 connections) — `server/persistence/repositories/__init__.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **CreateItemInstanceInput** (23 connections) — `server/async_persistence_constants.py`
- **skill_service.py** (20 connections) — `server/game/skill_service.py`
- **item_instance_persistence.py** (20 connections) — `server/persistence/item_instance_persistence.py`
- **player_spell_repository.py** (20 connections) — `server/persistence/repositories/player_spell_repository.py`
- **emote_service.py** (19 connections) — `server/game/emote_service.py`
- **SkillRepository** (19 connections) — `server/persistence/repositories/skill_repository.py`
- **item_instance_persistence_async.py** (18 connections) — `server/persistence/item_instance_persistence_async.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **player_skill_repository.py** (18 connections) — `server/persistence/repositories/player_skill_repository.py`
- **PlayerSkillRepository** (17 connections) — `server/persistence/repositories/player_skill_repository.py`
- **profession_repository.py** (17 connections) — `server/persistence/repositories/profession_repository.py`
- **skill_repository.py** (17 connections) — `server/persistence/repositories/skill_repository.py`
- **ExperienceRepository** (16 connections) — `server/persistence/repositories/experience_repository.py`
- **health_repository.py** (16 connections) — `server/persistence/repositories/health_repository.py`
- **experience_repository.py** (15 connections) — `server/persistence/repositories/experience_repository.py`
- **item_repository.py** (14 connections) — `server/persistence/repositories/item_repository.py`
- *... and 231 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (92 shared connections)
- [Maps API Endpoints](Maps_API_Endpoints.md) (78 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (53 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (43 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (38 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (38 shared connections)
- [Player Save Preparer](Player_Save_Preparer.md) (27 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (25 shared connections)
- [Lucidity Event Dispatcher](Lucidity_Event_Dispatcher.md) (23 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (21 shared connections)
- [Room Map Viewer UI](Room_Map_Viewer_UI.md) (21 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (20 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`
- `server/async_persistence_room_loader.py`
- `server/database.py`
- `server/exceptions.py`
- `server/game/emote_service.py`
- `server/game/mechanics.py`
- `server/game/skill_service.py`
- `server/persistence/__init__.py`
- `server/persistence/item_instance_persistence.py`
- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/item_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/persistence/repositories/player_spell_repository.py`

## Audit Trail

- EXTRACTED: 1788 (82%)
- INFERRED: 395 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*