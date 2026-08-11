# Coverage Disconnect Grace

> 11 nodes

## Key Concepts

- **delete_container()** (14 connections) — `server/persistence/container_persistence.py`
- **test_delete_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_success()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_not_found()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_uuid_string_conversion()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_false_and_psycopg_error()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **Delete by id; True if a row was removed. Raises DatabaseError on failure.** (1 connections) — `server/persistence/container_persistence.py`
- **Test delete_container successfully deletes container.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test delete_container returns False when container not found.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test delete_container handles database errors.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test delete_container handles UUID to string conversion.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`

## Relationships

- [Maps API Endpoints](Maps_API_Endpoints.md) (5 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (5 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Draggable Panel UI](Draggable_Panel_UI.md) (1 shared connections)

## Source Files

- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 32 (91%)
- INFERRED: 3 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*