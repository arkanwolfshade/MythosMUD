# composed

> 20 nodes

## Key Concepts

- **persistence/container_helpers.py** (26 connections) — `server/persistence/container_helpers.py`
- **ensure_item_instance()** (12 connections) — `server/persistence/item_instance_persistence.py`
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **update_container_items()** (8 connections) — `server/persistence/container_helpers.py`
- **_coerce_row_quantity()** (7 connections) — `server/persistence/container_helpers.py`
- **build_update_query()** (6 connections) — `server/persistence/container_helpers.py`
- **_item_dict_from_contents_row()** (5 connections) — `server/persistence/container_helpers.py`
- **UUID** (3 connections)
- **_metadata_dict_from_cell()** (2 connections) — `server/persistence/container_helpers.py`
- **test_ensure_item_instance_calls_create()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **datetime** (2 connections)
- **PsycopgConnection** (2 connections)
- **Composed** (1 connections)
- **PsycopgCursor** (1 connections)
- **Helper functions for container persistence operations.** (1 connections) — `server/persistence/container_helpers.py`
- **Fetch container items directly from normalized tables. Queries…** (1 connections) — `server/persistence/container_helpers.py`
- **Update container items using stored procedures. Args: cursor: Database cursor…** (1 connections) — `server/persistence/container_helpers.py`
- **Build SQL update query for container. Args: updates: List of update clauses…** (1 connections) — `server/persistence/container_helpers.py`
- **Normalize quantity/position from DB row cells; bool -> 1 (not…** (1 connections) — `server/persistence/container_helpers.py`
- **Ensure an item instance exists in the database, creating it if necessary.** (1 connections) — `server/persistence/item_instance_persistence.py`

## Relationships

- [server persistence container persistence](server_persistence_container_persistence.md) (12 shared connections)
- [server async persistence asyncpersistencelayer create](server_async_persistence_asyncpersistencelayer_create.md) (7 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (4 shared connections)
- [server models player player apply](server_models_player_player_apply.md) (3 shared connections)
- [server persistence container query helpers](server_persistence_container_query_helpers.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server persistence container data](server_persistence_container_data.md) (2 shared connections)
- [server persistence container helpers parse](server_persistence_container_helpers_parse.md) (2 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/item_instance_persistence.py`
- `server/tests/unit/persistence/test_item_instance_persistence.py`

## Audit Trail

- EXTRACTED: 63 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*