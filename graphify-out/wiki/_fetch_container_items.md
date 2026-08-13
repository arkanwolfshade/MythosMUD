# _fetch_container_items

> 36 nodes

## Key Concepts

- **_fetch_container_items()** (25 connections) — `server/container_persistence/container_persistence.py`
- **test_fetch_container_items_empty()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_invalid_json_metadata()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_missing_fields()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_missing_item_instance_id()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_non_dict_metadata()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_non_dict_row()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_string_metadata()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_with_items()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_uuid_string_conversion()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_fetch_container_items_empty()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_invalid_json_metadata()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_missing_fields()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_missing_item_instance_id()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_non_dict_metadata()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_non_dict_row()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_string_metadata()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_success()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **Fetch container items directly from normalized tables. Queries…** (1 connections) — `server/container_persistence/container_persistence.py`
- **Test _fetch_container_items with no items.** (1 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **Test _fetch_container_items with items.** (1 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **Test _fetch_container_items skips rows with missing item_instance_id.** (1 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **Test _fetch_container_items handles non-dictionary rows.** (1 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **Test _fetch_container_items parses string metadata.** (1 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **Test _fetch_container_items handles invalid JSON metadata.** (1 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- *... and 11 more nodes in this community*

## Relationships

- [test_container_persistence.py](test_container_persistence.py.md) (9 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (9 shared connections)
- [container_persistence/container_persistence.py](container_persistence-container_persistence.py.md) (6 shared connections)

## Source Files

- `server/container_persistence/container_persistence.py`
- `server/tests/unit/container_persistence/test_container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`

## Audit Trail

- EXTRACTED: 50 (85%)
- INFERRED: 9 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*