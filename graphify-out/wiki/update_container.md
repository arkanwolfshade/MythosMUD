# update_container

> 26 nodes

## Key Concepts

- **update_container()** (25 connections) — `server/persistence/container_persistence.py`
- **TestContainerPersistenceSQLInjection** (6 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **_create_mock_container_row()** (6 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **test_container_persistence_sql_injection.py** (6 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **.test_update_container_safe_column_names()** (4 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **.test_update_container_sql_injection_in_metadata()** (4 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **.test_update_container_uses_parameterized_queries()** (4 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **test_update_container_database_error()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_no_updates()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_not_found()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_success()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **.test_update_container_sql_injection_in_lock_state()** (3 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **test_update_container_wraps_psycopg2_error()** (2 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **UUID** (2 connections)
- **Apply item/lock/metadata updates; returns refreshed row or None if missing.** (1 connections) — `server/persistence/container_persistence.py`
- **Test update_container successfully updates container.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container returns None when container not found.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container handles database errors.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container with no updates provided (all None).** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Tests for SQL injection protection in container persistence operations. These…** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Test that update_container uses parameterized queries, not string concatenation.** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Test that column names are hardcoded, not from user input.** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Create a complete mock container row with all required columns.** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Test SQL injection protection in container persistence.** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Test that SQL injection in lock_state is prevented.** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- *... and 1 more nodes in this community*

## Relationships

- [persistence/container_persistence.py](persistence-container_persistence.py.md) (14 shared connections)
- [container_persistence_async.py](container_persistence_async.py.md) (4 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (1 shared connections)

## Source Files

- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- `server/tests/unit/test_container_persistence_sql_injection.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*