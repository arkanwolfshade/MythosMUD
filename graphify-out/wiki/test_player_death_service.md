# test player death service

> 30 nodes

## Key Concepts

- **container_helpers.py** (26 connections) — `server/persistence/container_helpers.py`
- **item_instance_persistence.py** (14 connections) — `server/persistence/item_instance_persistence.py`
- **update_container_items()** (10 connections) — `server/persistence/container_helpers.py`
- **fetch_container_items()** (9 connections) — `server/persistence/container_helpers.py`
- **ensure_item_instance()** (9 connections) — `server/persistence/item_instance_persistence.py`
- **create_item_instance()** (8 connections) — `server/persistence/item_instance_persistence.py`
- **_coerce_row_quantity()** (7 connections) — `server/persistence/container_helpers.py`
- **build_update_query()** (6 connections) — `server/persistence/container_helpers.py`
- **_item_dict_from_contents_row()** (5 connections) — `server/persistence/container_helpers.py`
- **Any** (4 connections)
- **get_item_instance()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **item_instance_exists()** (4 connections) — `server/persistence/item_instance_persistence.py`
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
- **Item instance persistence operations.  As documented in the restricted archives,** (1 connections) — `server/persistence/item_instance_persistence.py`
- *... and 5 more nodes in this community*

## Relationships

- [disconnect grace period](disconnect_grace_period.md) (14 shared connections)
- [real time](real_time.md) (11 shared connections)
- [spell registry](spell_registry.md) (8 shared connections)
- [.initialize()](initialize%28%29.md) (4 shared connections)
- [world](world.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [datetime](datetime.md) (2 shared connections)
- [test player repository](test_player_repository.md) (1 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/item_instance_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 127 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*