# DatabaseError

> 324 nodes

## Key Concepts

- **DatabaseError** (254 connections) — `server/exceptions.py`
- **log_and_raise()** (192 connections) — `server/utils/error_logging.py`
- **container_persistence.py** (53 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_row_helpers.py** (53 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **ContainerData** (41 connections) — `server/persistence/container_data.py`
- **test_container_persistence_extended_crud.py** (41 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_container_persistence_async_helpers.py** (40 connections) — `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- **container_persistence_async.py** (35 connections) — `server/persistence/container_persistence_async.py`
- **server/persistence/__init__.py** (32 connections) — `server/persistence/__init__.py`
- **update_container()** (26 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_parse.py** (26 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **ContainerDataCore** (24 connections) — `server/persistence/container_data.py`
- **persistence/container_helpers.py** (24 connections) — `server/persistence/container_helpers.py`
- **container_query_helpers_async.py** (24 connections) — `server/persistence/container_query_helpers_async.py`
- **container_repository.py** (24 connections) — `server/persistence/repositories/container_repository.py`
- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **ContainerCreateParams** (20 connections) — `server/persistence/container_create_params.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **get_container()** (19 connections) — `server/persistence/container_persistence.py`
- **ContainerDataExtras** (18 connections) — `server/persistence/container_data.py`
- **test_container_query_helpers_async.py** (17 connections) — `server/tests/unit/persistence/test_container_query_helpers_async.py`
- **create_container_async()** (15 connections) — `server/persistence/container_persistence_async.py`
- **get_container_async()** (15 connections) — `server/persistence/container_persistence_async.py`
- **update_container_async()** (14 connections) — `server/persistence/container_persistence_async.py`
- *... and 299 more nodes in this community*

## Relationships

- [get_session_maker](get_session_maker.md) (46 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (34 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (25 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (25 shared connections)
- [DatabaseManager](DatabaseManager.md) (24 shared connections)
- [repositories/__init__.py](repositories-__init__.py.md) (24 shared connections)
- [get_logger](get_logger.md) (20 shared connections)
- [PlayerSkillRepository](PlayerSkillRepository.md) (16 shared connections)
- [ExplorationService](ExplorationService.md) (15 shared connections)
- [DialogueDefinitionRepository](DialogueDefinitionRepository.md) (10 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (10 shared connections)
- [player_spell_repository.py](player_spell_repository.py.md) (10 shared connections)

## Source Files

- `server/exceptions.py`
- `server/persistence/__init__.py`
- `server/persistence/container_create_params.py`
- `server/persistence/container_data.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/persistence/container_persistence_async.py`
- `server/persistence/container_query_helpers.py`
- `server/persistence/container_query_helpers_async.py`
- `server/persistence/item_instance_persistence.py`
- `server/persistence/repositories/container_repository.py`
- `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- `server/tests/unit/persistence/test_container_query_helpers_async.py`
- `server/tests/unit/test_container_persistence_sql_injection.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 1138 (89%)
- INFERRED: 140 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*