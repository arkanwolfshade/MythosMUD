# GameBundle

> 94 nodes

## Key Concepts

- **GameBundle** (52 connections) — `server/container/bundles/game.py`
- **bundles/game.py** (39 connections) — `server/container/bundles/game.py`
- **SkillService** (38 connections) — `server/game/skill_service.py`
- **._init_player_quest_layer()** (16 connections) — `server/container/bundles/game.py`
- **SkillUseLogRepository** (15 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **LevelService** (13 connections) — `server/game/level_service.py`
- **EmoteRepository** (13 connections) — `server/persistence/repositories/emote_repository.py`
- **._init_movement_layer()** (11 connections) — `server/container/bundles/game.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **Any** (9 connections)
- **._initialize_item_services()** (8 connections) — `server/container/bundles/game.py`
- **utils.py** (8 connections) — `server/container/utils.py`
- **decode_json_column()** (7 connections) — `server/container/utils.py`
- **UUID** (7 connections)
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **._init_emote_service()** (5 connections) — `server/container/bundles/game.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/game.py`
- **normalize_path_from_url_or_path()** (5 connections) — `server/container/utils.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- *... and 69 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (29 shared connections)
- [SkillRepository](SkillRepository.md) (18 shared connections)
- [get_logger](get_logger.md) (17 shared connections)
- [get_session_maker](get_session_maker.md) (8 shared connections)
- [RoomService](RoomService.md) (6 shared connections)
- [time.py](time.py.md) (6 shared connections)
- [PlayerService](PlayerService.md) (5 shared connections)
- [test_level_service.py](test_level_service.py.md) (5 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (5 shared connections)
- [EmoteService](EmoteService.md) (4 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (4 shared connections)
- [RoomCacheService](RoomCacheService.md) (3 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/game/level_service.py`
- `server/game/skill_service.py`
- `server/persistence/repositories/emote_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`

## Audit Trail

- EXTRACTED: 257 (87%)
- INFERRED: 39 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*