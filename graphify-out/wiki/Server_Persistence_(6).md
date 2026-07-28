# Server Persistence (6)

> 60 nodes

## Key Concepts

- **_parse_jsonb_column()** (28 connections) — `server/container_persistence/container_persistence.py`
- **test_container_persistence_extended_parse.py** (26 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_persistence_container_persistence.py** (8 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **test_parse_jsonb_column_none()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_string()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_dict()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_empty_string()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_list()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_invalid_json()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_parse_jsonb_column_empty_list()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_parse_jsonb_column_empty_dict()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_parse_jsonb_column_string_list()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_parse_jsonb_column_string_dict()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_parse_jsonb_column_with_default()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_parse_jsonb_column_falsy_value()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_parse_jsonb_column_falsy_empty_string()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_parse_jsonb_column_falsy_empty_list()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_parse_jsonb_column_falsy_empty_dict()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_success()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_empty()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_missing_item_instance_id()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_non_dict_row()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_string_metadata()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_invalid_json_metadata()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_fetch_container_items_non_dict_metadata()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- *... and 35 more nodes in this community*

## Relationships

- [Server Container Persistence](Server_Container_Persistence.md) (20 shared connections)
- [Server Persistence (2)](Server_Persistence_%282%29.md) (7 shared connections)
- [Server Persistence (5)](Server_Persistence_%285%29.md) (2 shared connections)

## Source Files

- `server/container_persistence/container_persistence.py`
- `server/tests/unit/container_persistence/test_container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- `server/tests/unit/persistence/test_persistence_container_persistence.py`

## Audit Trail

- EXTRACTED: 143 (79%)
- INFERRED: 38 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*