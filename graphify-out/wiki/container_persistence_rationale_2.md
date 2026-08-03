# container persistence rationale

> 14 nodes

## Key Concepts

- **test_persistence_container_persistence.py** (8 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **test_parse_jsonb_column_none()** (3 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **test_parse_jsonb_column_string()** (3 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **test_parse_jsonb_column_dict()** (3 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **test_parse_jsonb_column_empty_string()** (3 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **test_parse_jsonb_column_list()** (3 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **test_parse_jsonb_column_invalid_json()** (3 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **Unit tests for persistence.container_persistence module.  This module tests the** (1 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **Test parsing None JSONB column.** (1 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **Test parsing string JSONB column.** (1 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **Test parsing dict JSONB column.** (1 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **Test parsing empty string JSONB column.** (1 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **Test parsing list JSONB column.** (1 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **Test parsing invalid JSON string.** (1 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`

## Relationships

- [Database Config](Database_Config.md) (6 shared connections)
- [persistence container item](persistence_container_item.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_persistence_container_persistence.py`

## Audit Trail

- EXTRACTED: 27 (82%)
- INFERRED: 6 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*