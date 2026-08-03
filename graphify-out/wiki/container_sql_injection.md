# container sql injection

> 41 nodes

## Key Concepts

- **test_container_persistence_extended_crud.py** (41 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **get_container()** (19 connections) — `server/persistence/container_persistence.py`
- **delete_container()** (14 connections) — `server/persistence/container_persistence.py`
- **test_create_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_room_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_entity_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_decayed_containers_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_decayed_containers_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_not_found()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_room_id_empty()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_decayed_containers_none_time()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_success()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_not_found()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_uuid_string_conversion()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_fetch_container_items_uuid_string_conversion()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_wraps_psycopg2_error()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **test_delete_container_false_and_psycopg_error()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **test_get_container_returns_none_when_row_missing()** (2 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **Load one container by id, or None. Raises DatabaseError on psycopg failure.** (1 connections) — `server/persistence/container_persistence.py`
- **Delete by id; True if a row was removed. Raises DatabaseError on failure.** (1 connections) — `server/persistence/container_persistence.py`
- **Unit tests for container persistence: CRUD, queries, and UUID conversion paths.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- *... and 16 more nodes in this community*

## Relationships

- [persistence container item](persistence_container_item.md) (21 shared connections)
- [Database Config](Database_Config.md) (15 shared connections)
- [follow service game](follow_service_game.md) (11 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (11 shared connections)
- [monitoring dashboard rationale](monitoring_dashboard_rationale.md) (6 shared connections)

## Source Files

- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 144 (91%)
- INFERRED: 14 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*