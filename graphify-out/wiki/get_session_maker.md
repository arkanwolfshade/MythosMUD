# get_session_maker

> 93 nodes

## Key Concepts

- **get_session_maker()** (97 connections) — `server/database.py`
- **ContainerRepository** (25 connections) — `server/persistence/repositories/container_repository.py`
- **container_query_helpers_async.py** (25 connections) — `server/persistence/container_query_helpers_async.py`
- **container_repository.py** (24 connections) — `server/persistence/repositories/container_repository.py`
- **test_container_repository.py** (22 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_container_query_helpers_async.py** (18 connections) — `server/tests/unit/persistence/test_container_query_helpers_async.py`
- **_build_container_data_from_row_async()** (14 connections) — `server/persistence/container_query_helpers_async.py`
- **get_decayed_containers_async()** (14 connections) — `server/persistence/container_query_helpers_async.py`
- **get_containers_by_entity_id_async()** (13 connections) — `server/persistence/container_query_helpers_async.py`
- **_container_data_to_dict()** (13 connections) — `server/persistence/repositories/container_repository.py`
- **get_containers_by_room_id_async()** (12 connections) — `server/persistence/container_query_helpers_async.py`
- **_sample_container_data()** (12 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **asyncio** (8 connections)
- **.create_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_entity_id()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_decayed_containers()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.update_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **Any** (7 connections)
- **asyncio** (7 connections)
- **check_invites.py** (7 connections) — `tools/invite_tools/check_invites.py`
- **_parse_jsonb()** (6 connections) — `server/persistence/container_query_helpers_async.py`
- **.get_containers_by_room_id()** (6 connections) — `server/persistence/repositories/container_repository.py`
- **.delete_container()** (5 connections) — `server/persistence/repositories/container_repository.py`
- **test_create_container()** (5 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- *... and 68 more nodes in this community*

## Relationships

- [persistence/container_persistence.py](persistence-container_persistence.py.md) (21 shared connections)
- [log_and_raise](log_and_raise.md) (17 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (14 shared connections)
- [PlayerRepository](PlayerRepository.md) (13 shared connections)
- [DatabaseError](DatabaseError.md) (12 shared connections)
- [database.py](database.py.md) (11 shared connections)
- [Player](Player.md) (9 shared connections)
- [persistence/repositories/__init__.py](persistence-repositories-__init__.py.md) (6 shared connections)
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) (6 shared connections)
- [player_effect_repository.py](player_effect_repository.py.md) (6 shared connections)
- [test_quest_instance_repository.py](test_quest_instance_repository.py.md) (6 shared connections)
- [SkillService](SkillService.md) (5 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `server/database.py`
- `server/persistence/container_query_helpers_async.py`
- `server/persistence/repositories/container_repository.py`
- `server/scripts/check_invite_status.py`
- `server/scripts/list_active_invites.py`
- `server/tests/unit/persistence/repositories/test_container_repository.py`
- `server/tests/unit/persistence/test_container_query_helpers_async.py`
- `tools/invite_tools/check_invites.py`

## Audit Trail

- EXTRACTED: 324 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*