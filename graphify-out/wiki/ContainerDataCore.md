# ContainerDataCore

> 40 nodes

## Key Concepts

- **container_persistence_async.py** (33 connections) — `server/persistence/container_persistence_async.py`
- **ContainerDataCore** (24 connections) — `server/persistence/container_data.py`
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
- **_build_item_dict()** (5 connections) — `server/persistence/container_persistence_async.py`
- **UUID** (5 connections)
- **test_update_container_uuid_string_conversion()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_items_only_prototype_id()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **_prepare_container_create_params()** (4 connections) — `server/persistence/container_persistence_async.py`
- **_row_to_mapping()** (4 connections) — `server/persistence/container_persistence_async.py`
- **_parse_item_metadata()** (4 connections) — `server/persistence/container_persistence_async.py`
- **ContainerData** (4 connections)
- **Identity and placement fields for a container row.** (1 connections) — `server/persistence/container_data.py`
- **Validate lock_state parameter.      Args:         lock_state: Lock state to v** (1 connections) — `server/persistence/container_helpers.py`
- **Async container persistence operations.  Provides async implementations using SQ** (1 connections) — `server/persistence/container_persistence_async.py`
- *... and 15 more nodes in this community*

## Relationships

- [ContainerData](ContainerData.md) (27 shared connections)
- [main()](main%28%29.md) (20 shared connections)
- [datetime](datetime.md) (12 shared connections)
- [fetch container items()](fetch_container_items%28%29.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (5 shared connections)
- [parse jsonb column()](parse_jsonb_column%28%29.md) (2 shared connections)

## Source Files

- `server/persistence/container_data.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence_async.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`

## Audit Trail

- EXTRACTED: 219 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*