# Persistence Container Extended

> 19 nodes · cohesion 0.15

## Key Concepts

- **container_helpers.py** (25 connections) — `server/persistence/container_helpers.py`
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **update_container_items()** (8 connections) — `server/persistence/container_helpers.py`
- **_coerce_row_quantity()** (7 connections) — `server/persistence/container_helpers.py`
- **build_update_query()** (6 connections) — `server/persistence/container_helpers.py`
- **_item_dict_from_contents_row()** (5 connections) — `server/persistence/container_helpers.py`
- **test_coerce_row_quantity()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **UUID** (3 connections) — `server/persistence/container_helpers.py`
- **_metadata_dict_from_cell()** (2 connections) — `server/persistence/container_helpers.py`
- **datetime** (2 connections) — `server/persistence/container_helpers.py`
- **PsycopgConnection** (2 connections) — `server/persistence/container_helpers.py`
- **Composed** (1 connections) — `server/persistence/container_helpers.py`
- **Helper functions for container persistence operations.** (1 connections) — `server/persistence/container_helpers.py`
- **Fetch container items directly from normalized tables.      Queries container_** (1 connections) — `server/persistence/container_helpers.py`
- **Update container items using stored procedures.      Args:         cursor: Da** (1 connections) — `server/persistence/container_helpers.py`
- **Build SQL update query for container.      Args:         updates: List of upd** (1 connections) — `server/persistence/container_helpers.py`
- **Normalize quantity/position from DB row cells; bool -> 1 (not coerce_int(False)=** (1 connections) — `server/persistence/container_helpers.py`
- **Row quantity/position coercion matches item quantity rules (PR #461 / int_coerci** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **PsycopgCursor** (1 connections) — `server/persistence/container_helpers.py`

## Relationships

- [[Container Persistence Layer]] (10 shared connections)
- [[NPC Admin API]] (7 shared connections)
- [[Container Data Models]] (5 shared connections)
- [[Integer Coercion Utils]] (3 shared connections)
- [[Persistence Item Instance]] (2 shared connections)
- [[Container Persistence Queries]] (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 80 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
