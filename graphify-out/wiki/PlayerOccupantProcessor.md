# PlayerOccupantProcessor

> 32 nodes

## Key Concepts

- **update_container()** (26 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_sql_injection.py** (6 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **_create_mock_container_row()** (6 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **TestContainerPersistenceSQLInjection** (6 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **test_update_container_uuid_string_conversion()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_items_missing_item_instance_id()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_items_only_prototype_id()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **.test_update_container_sql_injection_in_metadata()** (4 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **.test_update_container_uses_parameterized_queries()** (4 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **.test_update_container_safe_column_names()** (4 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **test_update_container_not_found()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_no_updates()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_wraps_psycopg2_error()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **.test_update_container_sql_injection_in_lock_state()** (3 connections) — `server/tests/unit/test_container_persistence_sql_injection.py`
- **UUID** (2 connections)
- **Apply item/lock/metadata updates; returns refreshed row or None if missing.** (1 connections) — `server/persistence/container_persistence.py`
- **Test update_container successfully updates container.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container returns None when container not found.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container handles database errors.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container with no updates provided (all None).** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container handles UUID to string conversion.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container skips items without item_instance_id or prototype_id.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test update_container handles items with only prototype_id (no item_instance_id)** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- *... and 7 more nodes in this community*

## Relationships

- [disconnect grace period](disconnect_grace_period.md) (17 shared connections)
- [spell registry](spell_registry.md) (8 shared connections)
- [real time](real_time.md) (4 shared connections)
- [datetime](datetime.md) (1 shared connections)

## Source Files

- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- `server/tests/unit/test_container_persistence_sql_injection.py`

## Audit Trail

- EXTRACTED: 104 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*