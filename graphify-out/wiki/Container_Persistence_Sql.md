# Container Persistence Sql

> 15 nodes · cohesion 0.17

## Key Concepts

- **_create_mock_container_row()** (6 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **TestContainerPersistenceSQLInjection** (6 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **test_container_persistence_sql_injection.py** (5 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **.test_update_container_safe_column_names()** (4 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **.test_update_container_sql_injection_in_metadata()** (4 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **.test_update_container_uses_parameterized_queries()** (4 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **.test_update_container_sql_injection_in_lock_state()** (3 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **UUID** (2 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Tests for SQL injection protection in container persistence operations.  These t** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Test that update_container uses parameterized queries, not string concatenation.** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Test that column names are hardcoded, not from user input.** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Create a complete mock container row with all required columns.** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Test SQL injection protection in container persistence.** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Test that SQL injection in lock_state is prevented.** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **Test that SQL injection in metadata_json is prevented.** (1 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`

## Relationships

- [[Container Persistence Layer]] (5 shared connections)

## Source Files

- `server/tests/unit/test_container_persistence_sql_injection.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
