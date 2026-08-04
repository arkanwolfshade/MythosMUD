# auth users rationale

> 120 nodes

## Key Concepts

- **container_persistence.py** (54 connections) — `server/persistence/container_persistence.py`
- **test_container_persistence_extended_row_helpers.py** (53 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **container_helpers.py** (26 connections) — `server/persistence/container_helpers.py`
- **update_container()** (26 connections) — `server/persistence/container_persistence.py`
- **_container_data_from_row()** (20 connections) — `server/persistence/container_persistence.py`
- **create_container()** (19 connections) — `server/persistence/container_persistence.py`
- **get_container()** (19 connections) — `server/persistence/container_persistence.py`
- **delete_container()** (14 connections) — `server/persistence/container_persistence.py`
- **parse_jsonb_column()** (11 connections) — `server/persistence/container_helpers.py`
- **_InsertBindSource** (11 connections) — `server/persistence/container_persistence.py`
- **_insert_container_row()** (11 connections) — `server/persistence/container_persistence.py`
- **PsycopgConnection** (11 connections)
- **_log_and_resolve_created_container()** (11 connections) — `server/persistence/container_persistence.py`
- **_seed_new_container_items()** (11 connections) — `server/persistence/container_persistence.py`
- **update_container_items()** (10 connections) — `server/persistence/container_helpers.py`
- **UUID** (10 connections)
- **_CreateOutcome** (10 connections) — `server/persistence/container_persistence.py`
- **_after_container_insert()** (10 connections) — `server/persistence/container_persistence.py`
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **_run_container_update_execute()** (9 connections) — `server/persistence/container_persistence.py`
- **validate_lock_state()** (8 connections) — `server/persistence/container_helpers.py`
- **_coerce_row_quantity()** (7 connections) — `server/persistence/container_helpers.py`
- **build_update_query()** (6 connections) — `server/persistence/container_helpers.py`
- **_as_uuid()** (6 connections) — `server/persistence/container_persistence.py`
- **_as_opt_datetime()** (6 connections) — `server/persistence/container_persistence.py`
- *... and 95 more nodes in this community*

## Relationships

- [persistence container item](persistence_container_item.md) (54 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (36 shared connections)
- [Loot Generation](Loot_Generation.md) (11 shared connections)
- [player requests schemas](player_requests_schemas.md) (5 shared connections)
- [commands party examples](commands_party_examples.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (3 shared connections)
- [persistence container extended](persistence_container_extended.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- `server/tests/unit/test_container_persistence_sql_injection.py`

## Audit Trail

- EXTRACTED: 600 (95%)
- INFERRED: 29 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*