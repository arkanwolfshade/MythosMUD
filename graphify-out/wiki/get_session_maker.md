# get_session_maker

> 138 nodes

## Key Concepts

- **get_session_maker()** (102 connections) — `server/database.py`
- **PlayerRepository** (32 connections) — `server/persistence/repositories/player_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **ContainerRepository** (25 connections) — `server/persistence/repositories/container_repository.py`
- **test_container_repository.py** (21 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **health_repository.py** (17 connections) — `server/persistence/repositories/health_repository.py`
- **generate_invites_db.py** (14 connections) — `tools/invite_tools/generate_invites_db.py`
- **_container_data_to_dict()** (13 connections) — `server/persistence/repositories/container_repository.py`
- **._validate_and_fix_player_room_with_persistence()** (12 connections) — `server/persistence/repositories/player_repository.py`
- **Player** (12 connections)
- **_sample_container_data()** (11 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **.get_player_by_id()** (9 connections) — `server/persistence/repositories/player_repository.py`
- **.get_active_players_by_user_id()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_player_by_name()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_batch()** (8 connections) — `server/persistence/repositories/player_repository.py`
- **asyncio** (8 connections)
- **.create_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_entity_id()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_decayed_containers()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.update_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.update_player_health()** (7 connections) — `server/persistence/repositories/health_repository.py`
- **.get_players_by_user_id()** (7 connections) — `server/persistence/repositories/player_repository.py`
- **.get_players_in_room()** (7 connections) — `server/persistence/repositories/player_repository.py`
- *... and 113 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (46 shared connections)
- [Player](Player.md) (20 shared connections)
- [DatabaseManager](DatabaseManager.md) (19 shared connections)
- [repositories/__init__.py](repositories-__init__.py.md) (14 shared connections)
- [PlayerSkillRepository](PlayerSkillRepository.md) (8 shared connections)
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) (6 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (6 shared connections)
- [player_spell_repository.py](player_spell_repository.py.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (5 shared connections)
- [test_player_repository.py](test_player_repository.py.md) (5 shared connections)
- [PlayerInventory](PlayerInventory.md) (5 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/persistence/repositories/container_repository.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/player_repository.py`
- `server/persistence/repositories/player_repository_mappers.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/tests/unit/persistence/repositories/test_container_repository.py`
- `tools/invite_tools/check_invites.py`
- `tools/invite_tools/generate_invites_db.py`

## Audit Trail

- EXTRACTED: 424 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*