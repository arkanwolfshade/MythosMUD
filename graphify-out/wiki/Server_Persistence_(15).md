# Server Persistence (15)

> 19 nodes

## Key Concepts

- **container_helpers.py** (26 connections) — `server/persistence/container_helpers.py`
- **update_container_items()** (10 connections) — `server/persistence/container_helpers.py`
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **_coerce_row_quantity()** (7 connections) — `server/persistence/container_helpers.py`
- **build_update_query()** (6 connections) — `server/persistence/container_helpers.py`
- **_item_dict_from_contents_row()** (5 connections) — `server/persistence/container_helpers.py`
- **UUID** (3 connections)
- **test_coerce_row_quantity()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **_metadata_dict_from_cell()** (2 connections) — `server/persistence/container_helpers.py`
- **PsycopgConnection** (2 connections)
- **datetime** (2 connections)
- **PsycopgCursor** (1 connections)
- **Composed** (1 connections)
- **Helper functions for container persistence operations.** (1 connections) — `server/persistence/container_helpers.py`
- **Normalize quantity/position from DB row cells; bool -> 1 (not coerce_int(False)=** (1 connections) — `server/persistence/container_helpers.py`
- **Fetch container items directly from normalized tables.      Queries container_** (1 connections) — `server/persistence/container_helpers.py`
- **Update container items using stored procedures.      Args:         cursor: Da** (1 connections) — `server/persistence/container_helpers.py`
- **Build SQL update query for container.      Args:         updates: List of upd** (1 connections) — `server/persistence/container_helpers.py`
- **Row quantity/position coercion matches item quantity rules (PR #461 / int_coerci** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Relationships

- [Server Persistence (5)](Server_Persistence_%285%29.md) (11 shared connections)
- [Server Services](Server_Services.md) (3 shared connections)
- [Server Persistence (2)](Server_Persistence_%282%29.md) (3 shared connections)
- [Server Admin](Server_Admin.md) (2 shared connections)
- [Server Persistence](Server_Persistence.md) (2 shared connections)
- [Server Utils](Server_Utils.md) (2 shared connections)
- [Server Persistence (9)](Server_Persistence_%289%29.md) (2 shared connections)
- [Server Persistence (16)](Server_Persistence_%2816%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Api](Server_Api.md) (1 shared connections)
- [Server Persistence (7)](Server_Persistence_%287%29.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 81 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*