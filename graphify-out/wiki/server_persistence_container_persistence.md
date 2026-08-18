# server persistence container persistence

> 65 nodes

## Key Concepts

- **persistence/container_persistence.py** (54 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_row_helpers.py** (54 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **update_container()** (26 connections) — `server/persistence/container_persistence.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **get_container()** (19 connections) — `server/persistence/container_persistence.py`
- **delete_container()** (13 connections) — `server/persistence/container_persistence.py`
- **_after_container_insert()** (11 connections) — `server/persistence/container_persistence.py`
- **_log_and_resolve_created_container()** (11 connections) — `server/persistence/container_persistence.py`
- **PsycopgConnection** (11 connections)
- **_insert_container_row()** (10 connections) — `server/persistence/container_persistence.py`
- **UUID** (10 connections)
- **_run_container_update_execute()** (9 connections) — `server/persistence/container_persistence.py`
- **_seed_new_container_items()** (9 connections) — `server/persistence/container_persistence.py`
- **_InsertBindSource** (7 connections) — `server/persistence/container_persistence.py`
- **_CreateOutcome** (6 connections) — `server/persistence/container_persistence.py`
- **_as_opt_datetime()** (6 connections) — `server/persistence/container_persistence.py`
- **_as_uuid()** (6 connections) — `server/persistence/container_persistence.py`
- **_metadata_from_row()** (6 connections) — `server/persistence/container_persistence.py`
- **ContainerData** (6 connections)
- **_allowed_roles_from_row()** (5 connections) — `server/persistence/container_persistence.py`
- **_as_opt_uuid()** (5 connections) — `server/persistence/container_persistence.py`
- **_fetch_container_row_dict()** (5 connections) — `server/persistence/container_persistence.py`
- **_insert_bind_tuple()** (5 connections) — `server/persistence/container_persistence.py`
- **_validate_new_container_params()** (5 connections) — `server/persistence/container_persistence.py`
- *... and 40 more nodes in this community*

## Relationships

- [server persistence container data](server_persistence_container_data.md) (21 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (18 shared connections)
- [server persistence container query helpers](server_persistence_container_query_helpers.md) (18 shared connections)
- [composed](composed.md) (12 shared connections)
- [server async persistence asyncpersistencelayer create](server_async_persistence_asyncpersistencelayer_create.md) (6 shared connections)
- [server tests unit test container](server_tests_unit_test_container.md) (6 shared connections)
- [server container persistence container data](server_container_persistence_container_data.md) (4 shared connections)
- [server persistence container helpers parse](server_persistence_container_helpers_parse.md) (3 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server persistence container create params](server_persistence_container_create_params.md) (1 shared connections)
- [server tests unit persistence test](server_tests_unit_persistence_test.md) (1 shared connections)

## Source Files

- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 254 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*