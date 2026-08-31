# log_and_raise

> 144 nodes

## Key Concepts

- **log_and_raise()** (189 connections) — `server/utils/error_logging.py`
- **test_container_persistence_extended_row_helpers.py** (54 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **container_persistence.py** (53 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_crud.py** (42 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **persistence/container_helpers.py** (24 connections) — `server/persistence/container_helpers.py`
- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **get_container()** (19 connections) — `server/persistence/container_persistence.py`
- **delete_container()** (13 connections) — `server/persistence/container_persistence.py`
- **get_decayed_containers()** (13 connections) — `server/persistence/container_query_helpers.py`
- **_build_container_data_from_row()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_entity_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_room_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **parse_jsonb_column()** (11 connections) — `server/persistence/container_helpers.py`
- **_after_container_insert()** (11 connections) — `server/persistence/container_persistence.py`
- **_log_and_resolve_created_container()** (11 connections) — `server/persistence/container_persistence.py`
- **PsycopgConnection** (11 connections)
- **_insert_container_row()** (10 connections) — `server/persistence/container_persistence.py`
- **UUID** (10 connections)
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **_seed_new_container_items()** (9 connections) — `server/persistence/container_persistence.py`
- **_create_engine_or_raise()** (8 connections) — `server/database.py`
- **update_container_items()** (8 connections) — `server/persistence/container_helpers.py`
- **_run_container_update_execute()** (8 connections) — `server/persistence/container_persistence.py`
- *... and 119 more nodes in this community*

## Relationships

- [ContainerData](ContainerData.md) (80 shared connections)
- [DatabaseError](DatabaseError.md) (31 shared connections)
- [ValidationError](ValidationError.md) (18 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (16 shared connections)
- [get_session_maker](get_session_maker.md) (13 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (12 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (10 shared connections)
- [MovementService](MovementService.md) (9 shared connections)
- [GameMechanicsService](GameMechanicsService.md) (8 shared connections)
- [ContainerComponent](ContainerComponent.md) (8 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (8 shared connections)
- [error_logging.py](error_logging.py.md) (7 shared connections)

## Source Files

- `server/database.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/persistence/container_query_helpers.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 580 (96%)
- INFERRED: 23 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*