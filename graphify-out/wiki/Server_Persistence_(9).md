# Server Persistence (9)

> 36 nodes

## Key Concepts

- **container_persistence_async.py** (33 connections) — `server/persistence/container_persistence_async.py`
- **get_container_async()** (16 connections) — `server/persistence/container_persistence_async.py`
- **create_container_async()** (13 connections) — `server/persistence/container_persistence_async.py`
- **Any** (11 connections)
- **_finalize_container_creation()** (11 connections) — `server/persistence/container_persistence_async.py`
- **update_container_async()** (11 connections) — `server/persistence/container_persistence_async.py`
- **fetch_container_items_async()** (10 connections) — `server/persistence/container_persistence_async.py`
- **_populate_container_items_async()** (9 connections) — `server/persistence/container_persistence_async.py`
- **validate_lock_state()** (8 connections) — `server/persistence/container_helpers.py`
- **AsyncSession** (8 connections)
- **delete_container_async()** (8 connections) — `server/persistence/container_persistence_async.py`
- **_call_create_container_procedure()** (7 connections) — `server/persistence/container_persistence_async.py`
- **_parse_jsonb()** (5 connections) — `server/persistence/container_persistence_async.py`
- **_validate_container_create_params()** (5 connections) — `server/persistence/container_persistence_async.py`
- **_build_item_dict()** (5 connections) — `server/persistence/container_persistence_async.py`
- **UUID** (5 connections)
- **_prepare_container_create_params()** (4 connections) — `server/persistence/container_persistence_async.py`
- **_row_to_mapping()** (4 connections) — `server/persistence/container_persistence_async.py`
- **_parse_item_metadata()** (4 connections) — `server/persistence/container_persistence_async.py`
- **ContainerData** (4 connections)
- **Validate lock_state parameter.      Args:         lock_state: Lock state to v** (1 connections) — `server/persistence/container_helpers.py`
- **Async container persistence operations.  Provides async implementations using SQ** (1 connections) — `server/persistence/container_persistence_async.py`
- **Parse JSONB value (same as container_helpers.parse_jsonb_column).** (1 connections) — `server/persistence/container_persistence_async.py`
- **Prepare params dict for create_container procedure call.** (1 connections) — `server/persistence/container_persistence_async.py`
- **Validate create_container params. Raises ValidationError on invalid input.** (1 connections) — `server/persistence/container_persistence_async.py`
- *... and 11 more nodes in this community*

## Relationships

- [Server Persistence (7)](Server_Persistence_%287%29.md) (12 shared connections)
- [Server Persistence (2)](Server_Persistence_%282%29.md) (10 shared connections)
- [Server Api](Server_Api.md) (7 shared connections)
- [Server Persistence](Server_Persistence.md) (6 shared connections)
- [Server Utils](Server_Utils.md) (4 shared connections)
- [Server Persistence (5)](Server_Persistence_%285%29.md) (4 shared connections)
- [Server Persistence (15)](Server_Persistence_%2815%29.md) (2 shared connections)
- [Server Admin](Server_Admin.md) (2 shared connections)
- [Server Persistence (14)](Server_Persistence_%2814%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence_async.py`

## Audit Trail

- EXTRACTED: 189 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*