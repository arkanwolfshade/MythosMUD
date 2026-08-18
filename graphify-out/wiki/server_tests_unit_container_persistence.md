# server tests unit container persistence

> 37 nodes

## Key Concepts

- **test_container_persistence.py** (21 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_container_data_init()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_container_data_to_dict()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_container_data_to_dict_with_all_fields()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_container_data_to_dict_with_datetimes()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_empty()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_invalid_json_metadata()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_missing_fields()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_missing_item_instance_id()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_non_dict_metadata()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_non_dict_row()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_string_metadata()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_fetch_container_items_with_items()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_dict()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_empty_string()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_invalid_json()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_list()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_none()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_string()** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **Test fetch_container_items with no items.** (2 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **Unit tests for container_persistence helpers and fetch_container_items. Tests…** (1 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **Test fetch_container_items skips rows with missing item_instance_id.** (1 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **Test fetch_container_items handles non-dictionary rows.** (1 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **Test fetch_container_items parses string metadata.** (1 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **Test fetch_container_items handles invalid JSON metadata.** (1 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- *... and 12 more nodes in this community*

## Relationships

- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [server container persistence container data](server_container_persistence_container_data.md) (1 shared connections)

## Source Files

- `server/tests/unit/container_persistence/test_container_persistence.py`

## Audit Trail

- EXTRACTED: 39 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*